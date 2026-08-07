from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd


TARGET_COLUMN = "Class"

FEATURE_COLUMNS = [
    "Time",
    *[f"V{i}" for i in range(1, 29)],
    "Amount",
]


def load_data(csv_path: str | Path) -> pd.DataFrame:
    """Load the credit-card CSV dataset."""

    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {csv_path}"
        )

    return pd.read_csv(csv_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate transactions."""

    df = df.copy()

    return df.drop_duplicates().reset_index(drop=True)


def split_features_target(
    df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Split the dataset into features X and target y.

    Features:
        Time, V1 ... V28, Amount

    Target:
        Class
    """

    missing = [
        column
        for column in FEATURE_COLUMNS + [TARGET_COLUMN]
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    X = df[FEATURE_COLUMNS].copy()
    y = df[TARGET_COLUMN].copy()

    return X, y


def preprocess_dataset(
    csv_path: str | Path,
) -> Tuple[pd.DataFrame, pd.Series]:
    """Load, clean, and split the dataset."""

    df = load_data(csv_path)

    df = clean_data(df)

    return split_features_target(df)