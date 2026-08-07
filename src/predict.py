from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from preprocessing import FEATURE_COLUMNS

from utils import (
    DEFAULT_THRESHOLD,
    MODEL_PATH,
    load_model,
)


def predict_dataframe(
    df: pd.DataFrame,
    model_path: str | Path = MODEL_PATH,
    threshold: float = DEFAULT_THRESHOLD,
) -> pd.DataFrame:
    """
    Predict fraud probability and class
    for one or more transactions.
    """

    # Check required columns
    missing = [
        column
        for column in FEATURE_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required feature columns: {missing}"
        )

    # Load trained model
    model = load_model(
        model_path
    )

    print("✅ Model loaded successfully.")

    # Select features
    X = df[
        FEATURE_COLUMNS
    ].copy()

    # Get fraud probabilities
    probabilities = model.predict_proba(
        X
    )[:, 1]

    # Create result
    result = df.copy()

    result[
        "Fraud_Probability"
    ] = probabilities

    # Apply threshold
    result[
        "Prediction"
    ] = (
        probabilities >= threshold
    ).astype(int)

    # Convert prediction to readable label
    result[
        "Prediction_Label"
    ] = result[
        "Prediction"
    ].map(
        {
            0: "Legitimate",
            1: "Fraud",
        }
    )

    print("✅ Fraud prediction generated successfully.")

    return result


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Predict credit card fraud "
            "using Random Forest + SMOTE"
        )
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Input transaction CSV file",
    )

    parser.add_argument(
        "--model",
        default=str(MODEL_PATH),
        help="Path to trained model",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help="Fraud decision threshold",
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Optional output CSV file",
    )

    args = parser.parse_args()


    # Validate threshold
    if not 0 <= args.threshold <= 1:
        raise ValueError(
            "Threshold must be between 0 and 1."
        )


    input_path = Path(
        args.input
    )

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )


    # Load input data
    df = pd.read_csv(
        input_path
    )

    print(
        f"✅ Input data loaded successfully "
        f"({len(df)} transactions)."
    )


    # Make predictions
    result = predict_dataframe(
        df,
        model_path=args.model,
        threshold=args.threshold,
    )


    # Display predictions
    print(
        "\nPrediction Results:"
    )

    print(
        result[
            [
                "Fraud_Probability",
                "Prediction",
                "Prediction_Label",
            ]
        ].to_string(
            index=False
        )
    )


    # Save predictions if requested
    if args.output:

        result.to_csv(
            args.output,
            index=False,
        )

        print(
            f"\n✅ Predictions saved successfully to: "
            f"{args.output}"
        )


    print(
        "\n🎉 Random Forest + SMOTE fraud detection completed successfully!"
    )


if __name__ == "__main__":
    main()

# terminal: python predict.py --input "../data/creditcard.csv"