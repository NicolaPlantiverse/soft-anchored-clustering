#!/usr/bin/env python3
"""
csv_to_npz.py

Small utility to convert a CSV table into the repository's `.npz` format.

Typical usage
-------------
python scripts/csv_to_npz.py \
  --csv data.csv \
  --out data.npz \
  --x-cols log_res,chargeability \
  --s-cols east,north

Optional: anchors and constraints
---------------------------------
- anchors can be provided as a CSV/TSV with a single column of 0-based indices.
- constraints can be provided as a CSV with columns: i, j, type, rho
  where type=1 (must-link) or type=0 (cannot-link), rho in [0,1].

This script is intentionally conservative: it does not try to "guess" columns.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Optional

import numpy as np
import pandas as pd


def _split_cols(s: str) -> List[str]:
    return [c.strip() for c in s.split(",") if c.strip()]


def load_anchors(path: Path) -> np.ndarray:
    df = pd.read_csv(path, header=None)
    a = df.iloc[:, 0].to_numpy(dtype=int)
    if a.ndim != 1:
        raise ValueError("anchors file must contain a single column of indices")
    return a


def load_constraints(path: Path) -> np.ndarray:
    df = pd.read_csv(path)
    required = {"i", "j", "type", "rho"}
    if not required.issubset(df.columns):
        raise ValueError(f"constraints file must include columns {sorted(required)}")
    arr = df[["i", "j", "type", "rho"]].to_numpy()
    return arr


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Convert CSV to NPZ format used by this repository.")
    p.add_argument("--csv", required=True, type=Path, help="Input CSV file.")
    p.add_argument("--out", required=True, type=Path, help="Output .npz path.")
    p.add_argument("--x-cols", required=True, type=str, help="Comma-separated feature (amplitude) column names.")
    p.add_argument("--s-cols", required=True, type=str, help="Comma-separated coordinate column names (exactly 2).")
    p.add_argument("--anchors", type=Path, default=None, help="Optional file with 0-based anchor indices (one per line).")
    p.add_argument("--y-anchor-col", type=str, default=None, help="Optional column name with anchor labels (only for diagnostics).")
    p.add_argument("--constraints", type=Path, default=None, help="Optional constraints CSV with columns i,j,type,rho.")
    args = p.parse_args(argv)

    df = pd.read_csv(args.csv)
    x_cols = _split_cols(args.x_cols)
    s_cols = _split_cols(args.s_cols)

    if len(s_cols) != 2:
        raise ValueError("--s-cols must contain exactly 2 column names")

    for c in x_cols + s_cols:
        if c not in df.columns:
            raise ValueError(f"Column '{c}' not found in CSV columns: {list(df.columns)}")

    X = df[x_cols].to_numpy(dtype=float)
    S = df[s_cols].to_numpy(dtype=float)

    n = X.shape[0]
    payload = {"X": X, "S": S}

    if args.anchors is not None:
        anchors = load_anchors(args.anchors).astype(int)
        if anchors.min(initial=0) < 0 or anchors.max(initial=0) >= n:
            raise ValueError("anchors indices are out of bounds for X/S length")
        payload["anchors"] = anchors

        # Optional: y_anchor extracted from a column in the main CSV
        if args.y_anchor_col is not None:
            if args.y_anchor_col not in df.columns:
                raise ValueError(f"y-anchor-col '{args.y_anchor_col}' not found in CSV")
            # Expect anchor labels aligned by observation index; take only anchor entries
            y = df[args.y_anchor_col].to_numpy()
            payload["y_anchor"] = y[anchors].astype(int)

    if args.constraints is not None:
        C = load_constraints(args.constraints)
        if C.shape[1] != 4:
            raise ValueError("constraints array must have 4 columns: i,j,type,rho")
        # basic validation
        i = C[:, 0].astype(int)
        j = C[:, 1].astype(int)
        if i.min(initial=0) < 0 or j.min(initial=0) < 0 or i.max(initial=0) >= n or j.max(initial=0) >= n:
            raise ValueError("constraint indices i/j are out of bounds")
        payload["constraints"] = C

    args.out.parent.mkdir(parents=True, exist_ok=True)
    np.savez(args.out, **payload)
    print(f"Wrote {args.out} with keys: {sorted(payload.keys())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
