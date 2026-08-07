from __future__ import annotations

import argparse
from pathlib import Path

import joblib

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
)
from sklearn.preprocessing import StandardScaler

from preprocessing import preprocess_dataset

from utils import (
    MODEL_PATH,
    RANDOM_STATE,
    DEFAULT_THRESHOLD,
    ensure_parent_directory,
)


def build_pipeline() -> Pipeline:
    """
    Create the StandardScaler + SMOTE + Random Forest pipeline.
    """

    pipeline = Pipeline(
        steps=[
            (
                "scaler",
                StandardScaler(),
            ),
            (
                "smote",
                SMOTE(
                    random_state=RANDOM_STATE
                ),
            ),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=RANDOM_STATE,
                    n_jobs=-1,
                ),
            ),
        ]
    )

    return pipeline



def train_model(
    data_path: str | Path,
    model_path: str | Path = MODEL_PATH,
):
    """
    Train and save the Random Forest + SMOTE model.
    """

    print("\n" + "=" * 65)
    print("🚀 CREDIT CARD FRAUD DETECTION MODEL TRAINING")
    print("=" * 65)


    # Load dataset
    print("\n📂 Loading dataset...")

    X, y = preprocess_dataset(
        data_path
    )

    print(
        f"✅ Dataset loaded successfully!"
    )

    print(
        f"   Features: {X.shape[1]}"
    )

    print(
        f"   Samples: {X.shape[0]}"
    )


    # Train-test split
    print("\n✂️ Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    print(
        "✅ Train-test split completed!"
    )

    print(
        f"   Training samples: {X_train.shape[0]}"
    )

    print(
        f"   Testing samples: {X_test.shape[0]}"
    )


    # Build pipeline
    print(
        "\n⚙️ Building ML pipeline..."
    )

    pipeline = build_pipeline()

    print(
        "✅ Pipeline created:"
    )

    print(
        "   StandardScaler → SMOTE → Random Forest"
    )


    # Train model
    print(
        "\n🤖 Training Random Forest model..."
    )

    pipeline.fit(
        X_train,
        y_train,
    )

    print(
        "✅ Model training completed!"
    )


    # Prediction probabilities
    print(
        "\n📊 Evaluating model performance..."
    )

    y_prob = pipeline.predict_proba(
        X_test
    )[:, 1]


    # Apply threshold
    y_pred = (
        y_prob >= DEFAULT_THRESHOLD
    ).astype(int)


    # ROC-AUC
    roc_auc = roc_auc_score(
        y_test,
        y_prob,
    )


    print("\n" + "-" * 65)
    print("📈 MODEL PERFORMANCE")
    print("-" * 65)

    print(
        f"ROC-AUC Score       : {roc_auc:.6f}"
    )

    print(
        f"Decision Threshold  : {DEFAULT_THRESHOLD:.2f}"
    )


    print(
        "\n📋 Classification Report:"
    )

    print(
        classification_report(
            y_test,
            y_pred,
        )
    )


    # Save model
    print(
        "\n💾 Saving trained model..."
    )

    model_path = Path(
        model_path
    )

    ensure_parent_directory(
        model_path
    )


    joblib.dump(
        pipeline,
        model_path,
    )


    print(
        "✅ Model saved successfully!"
    )

    print(
        f"   Location: {model_path}"
    )


    print("\n" + "=" * 65)

    print(
        "🎉 TRAINING COMPLETED SUCCESSFULLY!"
    )

    print("=" * 65 + "\n")


    return pipeline



def main():

    parser = argparse.ArgumentParser(
        description=(
            "Train Credit Card "
            "Fraud Detection Model"
        )
    )


    parser.add_argument(
        "--data",
        required=True,
        help="Path to creditcard.csv",
    )


    parser.add_argument(
        "--model",
        default=str(MODEL_PATH),
        help="Path to save trained model",
    )


    args = parser.parse_args()


    train_model(
        args.data,
        args.model,
    )



if __name__ == "__main__":
    main()
# terminal: python train.py --data "../data/creditcard.csv"