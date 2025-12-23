# Soft-Anchored Clustering under Heterogeneous Credibility

Reference implementation for the method described in:

**Soft-Anchored Clustering under Heterogeneous Credibility: A Probabilistic Framework for Spatial Data with Uncertain Constraints**

*Leonardo Giannini, Nicola Nescatelli*



---

## Overview

This repository provides the reference Python implementation of the Soft-Anchored Clustering framework, which addresses spatial clustering problems where observations and constraints have heterogeneous reliability.

The method combines:
- Credibility-weighted heteroscedastic mixture models
- Soft spatial regularization with credibility-dependent coupling
- Probabilistic soft constraints
- Uncertainty quantification (entropy, ignorance, posterior assignment confidence)

---

## Installation

```bash
pip install -r requirements.txt
```

Requires Python ≥3.9 and standard scientific packages (numpy, scipy, scikit-learn, pandas).

---

## Reproducibility

All numerical results reported in the manuscript can be reproduced using fixed configurations and random seeds.

**Example (synthetic dataset):**

```bash
python run_repro.py run --dataset synthetic --out results/synthetic --K 3 --seeds 20
python run_repro.py summarize --input results/synthetic --out tables/synthetic
```

The `summarize` command generates the mean±std statistics and relative improvements reported in the paper.

**For complete reproduction instructions**, including data format specification, ERT dataset usage, and ablation studies, see:

📖 **[docs/REPRODUCTION_DETAILS.md](docs/REPRODUCTION_DETAILS.md)**

---

## Data Format

Experiments use NumPy `.npz` archives with fields:
- `X`: (n, d) feature matrix
- `S`: (n, 2) spatial coordinates
- `anchors`: (m,) anchor indices (optional)
- `y_anchor`: (m,) anchor labels (optional)
- `constraints`: (q, 4) constraint array (optional)

Complete specification: [docs/DATA_FORMAT.md](docs/DATA_FORMAT.md)

CSV conversion utility: `scripts/csv_to_npz.py`

---

## Correspondence to Manuscript

| Manuscript Section | Script | Dataset |
|--------------------|--------|---------|
| Table 1 (ERT results) | `run_repro.py --dataset ert` | ERT (private) |
| Table 2 (Ablations) | `run_repro.py --dataset ert --ablation` | ERT (private) |
| Anisotropic extension | `run_repro.py --dataset ert --anisotropic` | ERT (private) |
| Synthetic experiment | `run_repro.py --dataset synthetic` | Generated |
| Negative control | `run_repro.py --dataset iris` | Iris (public) |

All experiments use R=20 independent runs with predefined seeds.

---

## Repository Structure

```
├── run_repro.py                          # Main reproducibility script
├── supplement_soft_anchored_repro.py     # Supplementary analyses
├── requirements.txt                      # Python dependencies
├── docs/
│   ├── DATA_FORMAT.md                    # Data format specification
│   └── REPRODUCTION_DETAILS.md           # Detailed reproduction guide
└── scripts/
    └── csv_to_npz.py                     # CSV conversion utility
```

---

## Citation

If you use this code, please cite:

```bibtex
@article{giannini2025soft,
  title={Soft-Anchored Clustering under Heterogeneous Credibility: A Probabilistic Framework for Spatial Data with Uncertain Constraints},
  author={Giannini, Leonardo and Nescatelli, Nicola},
  journal={Computers \& Geosciences},
  year={2025},
  note={Under review}
}
```

---

## License

MIT

---

## Contact

For questions regarding the method or implementation: 
- Nicola Nescatelli: nicola@plantiverse.it
- Leonardo Giannini: leonardo.giannini@uniroma1.it
