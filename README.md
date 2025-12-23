Perfetto. Qui sotto trovi il README completo, già rifinito in stile riproducibilità accademica, coerente con il paper, copiabile e incollabile direttamente su GitHub, con licenza MIT esplicitata.
Ho rispettato i vincoli che hai dato: linguaggio sobrio, tempi verbali presente/passato/condizionale, niente terminologia che non gradisci, niente promesse future, niente tono marketing.

⸻


# Soft-Anchored Clustering (reproducibility package)

This repository provides a reference Python implementation and a complete reproducibility workflow for the paper:

**Soft-Anchored Clustering under Heterogeneous Credibility:  
A Probabilistic Framework for Spatial Data with Uncertain Constraints**

The framework addresses spatial clustering problems in which:
- observations exhibit heterogeneous reliability (credibility),
- a subset of high-confidence points (“anchors”) is available,
- spatial contiguity is desirable,
- pairwise constraints are uncertain and are handled in a soft probabilistic manner.

The repository is intended to enable independent researchers to reproduce the experimental results reported in the manuscript, subject only to numerical tolerances and hardware-dependent floating-point differences.

---

## Quick start

### 1) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

2) Run the reproducibility pipeline

python run_repro.py run --out results

This command executes the included experiments, reproduces the reported tables as averages over repeated runs with fixed random seeds, and exports diagnostic outputs when applicable.

⸻

Input data format

All experiments rely on a standardized .npz container with the following required fields:
	•	X: array of shape (n, d) containing amplitude features
	•	S: array of shape (n, 2) containing spatial coordinates

Optional fields:
	•	anchors: array of shape (m,) containing 0-based indices of anchor points
	•	y_anchor: array of shape (m,) containing anchor labels
(used only for diagnostic evaluations such as leave-one-anchor-out accuracy)
	•	constraints: array of shape (q, 4) encoding pairwise constraints as
(i, j, type, rho), where:
	•	type = 1 indicates a must-link constraint,
	•	type = 0 indicates a cannot-link constraint,
	•	rho ∈ [0, 1] denotes the constraint credibility
(if omitted, default values may be derived from node credibility)

A full and precise specification is provided in:

docs/DATA_FORMAT.md


⸻

CSV to NPZ conversion

A helper script is provided to convert CSV files into the required .npz format:

python scripts/csv_to_npz.py \
  --csv your_data.csv \
  --out your_data.npz \
  --x-cols x1,x2,x3 \
  --s-cols east,north

Additional options support anchors and constraints. See:

python scripts/csv_to_npz.py --help


⸻

Outputs

Typical runs generate the following outputs:
	•	z: hard cluster assignments
	•	mu, Sigma: fitted component parameters (for Gaussian components)
	•	c: prior credibility field
	•	c_eff: effective credibility with background regularization
	•	H: local label entropy (ambiguity proxy)
	•	PAC: posterior assignment confidence derived from normalized local entropy
	•	I: ignorance map defined as I = 1 - c_eff

Important note on interpretation

PAC represents a diagnostic certainty measure induced by the model objective under a local conditional approximation. It does not represent calibrated classification accuracy unless explicitly calibrated against labeled data.

⸻

Reproducing manuscript results

The manuscript reports results as averages over repeated runs with fixed random seeds. The reference runner exposes the corresponding experimental configurations as:

python run_repro.py run --dataset ert        --out results/ert
python run_repro.py run --dataset synthetic  --out results/synthetic
python run_repro.py run --dataset iris       --out results/iris

Each command reproduces the tables reported for the corresponding dataset using the same protocol described in the paper.

If the Electrical Resistivity Tomography (ERT) field dataset is available, it can be placed according to the repository instructions and evaluated using the ert configuration.

⸻

Data availability
	•	A fully redistributable synthetic dataset is included.
	•	A small public demonstration dataset is included for validation and inspection.

If the ERT field dataset cannot be publicly redistributed, the repository still provides:
	•	the complete experimental protocol,
	•	the full input data specification,
	•	a surrogate data generator that reproduces the spatial structure required to validate the workflow.

This ensures that the reproducibility pipeline can be independently verified without access to restricted field data.

⸻

Citation

If this code or workflow is used in academic work, please cite the associated manuscript.

⸻

License

This repository is released under the MIT License.
See the LICENSE file for details.

