from __future__ import annotations

from pathlib import Path

import joblib


# Random seed used throughout the project
RANDOM_STATE = 42


# Optimized threshold obtained from
# RF + SMOTE threshold tuning
DEFAULT_THRESHOLD = 0.51


# Project directories
PROJECT_ROOT = Path(
    __file__
).resolve().parent

MODEL_DIR = (
    PROJECT_ROOT / "models"
)


# Saved model location
MODEL_PATH = (
    MODEL_DIR
    / "fraud_detection_rf_smote.joblib"
)


def ensure_parent_directory(
    path: str | Path,
) -> None:
    """
    Create the parent directory
    if it does not already exist.
    """

    Path(path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )


def load_model(
    model_path: str | Path = MODEL_PATH,
):
    """
    Load the trained fraud detection model.
    """

    model_path = Path(
        model_path
    )

    if not model_path.exists():

        raise FileNotFoundError(
            f"Model not found: {model_path}. "
            "Run train.py first."
        )

    return joblib.load(
        model_path
    )