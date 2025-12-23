# Soft-Anchored Clustering (reproducibility package)

This repository contains a reference implementation and an end-to-end reproducibility workflow for:

**Soft-Anchored Clustering under Heterogeneous Credibility: A Probabilistic Framework for Spatial Data with Uncertain Constraints**

The method targets spatial datasets where:
- observations have heterogeneous reliability (credibility),
- a subset of high-confidence points (“anchors”) may be available,
- spatial contiguity is desirable,
- pairwise constraints may be uncertain and should be handled softly.

## Quick start

### 1) Create an environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the full reproducibility suite

```bash
python run_repro.py run --out results
```

This will:
- run the included demos/synthetic experiments,
- regenerate the tables (mean ± std across repeated seeds),
- export diagnostic maps when applicable.

## Inputs

Experiments use a standard **`.npz`** container with (at minimum):

- `X`: `(n, d)` feature matrix (amplitude features)
- `S`: `(n, 2)` spatial coordinates

Optional fields:
- `anchors`: `(m,)` integer indices (0-based) of anchor points
- `y_anchor`: `(m,)` labels for anchors (optional, used only for diagnostics like LOAO when available)
- `constraints`: `(q, 4)` constraints encoded as `(i, j, type, rho)` where:
  - `type = 1` for must-link, `type = 0` for cannot-link
  - `rho ∈ [0, 1]` is the constraint credibility (optional; defaults may be derived from node credibility)

Full specification: see `docs/DATA_FORMAT.md`.

### CSV to NPZ helper

If you start from CSV, use:

```bash
python scripts/csv_to_npz.py --csv your_data.csv --out your_data.npz --x-cols x1,x2,x3 --s-cols east,north
```

See `python scripts/csv_to_npz.py --help` for options (anchors and constraints supported).

## Outputs

Runs typically write:
- `z`: hard cluster assignments
- `mu, Sigma`: fitted component parameters (when using Gaussian components)
- `c` and `c_eff`: prior credibility and effective credibility (with background floor)
- `H`: local label entropy (ambiguity proxy)
- `PAC`: posterior assignment confidence derived from normalized local entropy
- `I`: ignorance map `I = 1 - c_eff` (low prior information)

Notes:
- `PAC` is a *diagnostic certainty proxy* induced by the model’s objective under a local-conditional approximation; it is **not calibrated accuracy** unless you calibrate it against labeled data.

## Correspondence: manuscript results ↔ commands

The paper reports results as repeated runs with fixed seeds. The reference runner exposes the corresponding datasets via:

```bash
python run_repro.py run --dataset ert        --out results/ert
python run_repro.py run --dataset synthetic  --out results/synthetic
python run_repro.py run --dataset iris       --out results/iris
```

If you have the (possibly restricted) ERT field dataset, place it as described in the paper/repository notes and run the `ert` target.

## Data availability

- A redistributable synthetic dataset and a small public demo dataset are included.
- If the ERT field dataset cannot be redistributed, the repository still provides the full protocol, format specification, and a surrogate generator to validate the workflow structure.

## Citation

If you use this code, please cite the associated manuscript.

## License

MIT
