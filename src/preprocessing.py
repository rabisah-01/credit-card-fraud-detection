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

    df = pd.read_csv(csv_path)

    print(f"✅ Dataset loaded successfully: {csv_path}")
    print(f"📊 Dataset shape: {df.shape}")

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate transactions."""

    df = df.copy()

    before = len(df)

    df = df.drop_duplicates().reset_index(drop=True)

    after = len(df)

    removed = before - after

    print("✅ Data cleaning completed successfully")
    print(f"🗑️ Duplicate rows removed: {removed}")

    return df


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

    print("✅ Feature and target separation completed")
    print(f"📌 Feature shape (X): {X.shape}")
    print(f"🎯 Target shape (y): {y.shape}")

    return X, y


def preprocess_dataset(
    csv_path: str | Path,
) -> Tuple[pd.DataFrame, pd.Series]:
    """Load, clean, and split the dataset."""

    print("🚀 Starting dataset preprocessing...\n")

    df = load_data(csv_path)

    df = clean_data(df)

    X, y = split_features_target(df)

    print("\n🎉 Dataset preprocessing completed successfully!")

    return X, y