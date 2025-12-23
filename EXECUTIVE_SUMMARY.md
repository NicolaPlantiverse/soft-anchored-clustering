# Executive Summary

This repository provides the reference Python implementation and full reproducibility material for the paper:

**Soft-Anchored Clustering under Heterogeneous Credibility:  
A Probabilistic Framework for Spatial Data with Uncertain Constraints**

The method addresses spatial clustering problems where observations, anchors, and constraints have heterogeneous and uncertain reliability.

---

## Scientific Contribution

The framework introduces three key ideas:

1. **Credibility-aware heteroscedastic modeling**  
   Observation credibility directly modulates noise levels in a probabilistic mixture model, with background regularization preventing numerical degeneracy.

2. **Soft spatial regularization under uncertainty**  
   Spatial coupling and pairwise constraints are enforced probabilistically, with credibility-weighted penalties that tolerate imperfect or conflicting information.

3. **Uncertainty diagnostics beyond labels**  
   The method outputs entropy, ignorance, and posterior assignment confidence (PAC) maps, separating ambiguity from lack of information.

An optional anisotropic extension captures directional continuity using geometry-derived structure, without introducing additional tuned hyperparameters.

---

## Repository Contents

The repository includes:
- Reference Python implementation of the method
- Scripts to reproduce all tables and metrics reported in the manuscript
- Fixed random seeds and configurations (R = 20 runs per experiment)
- A documented `.npz` data format specification
- Conversion utilities for CSV-based datasets
- Synthetic and public datasets for independent verification

Private field data (ERT) are not redistributed, but full experimental protocols and surrogate data generation are provided.

---

## Reproducibility

All numerical results reported in the manuscript (means, standard deviations, relative improvements) are generated directly from this codebase.

- No cherry-picking: all runs are included
- Exact replication is possible up to floating-point precision
- Each manuscript table corresponds to a specific script and configuration

Detailed reproduction instructions are provided in `docs/REPRODUCTION_DETAILS.md`.

---

## Intended Audience

This repository is intended for:
- Reviewers evaluating methodological soundness and reproducibility
- Researchers working on spatial clustering, constrained clustering, or uncertainty-aware learning
- Practitioners in geosciences and related spatial domains

--- 
 
