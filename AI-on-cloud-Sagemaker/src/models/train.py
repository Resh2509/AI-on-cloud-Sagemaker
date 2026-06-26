import pandas as pd
import joblib

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# =====================================================
# Paths
# =====================================================

DATA_PATH = Path("data/processed/cleaned_data.csv")
ARTIFACTS_PATH = Path("artifacts")

# =====================================================
# Load Dataset
# =====================================================

def load_data():
    return pd.read_csv(DATA_PATH)

# =====================================================
# Split Dataset
# =====================================================

def split_data(df):

    X = df.drop("Churn", axis=1)

    y = df["Churn"].map({
        "No": 0,
        "Yes": 1
    })

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

# =====================================================
# Detect Column Types
# =====================================================

def get_column_types(X):

    categorical_columns = X.select_dtypes(
        include=["object","string"]
    ).columns.tolist()

    numerical_columns = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    return categorical_columns, numerical_columns

# =====================================================
# Create Preprocessor
# =====================================================

def create_preprocessor(cat_cols, num_cols):

    preprocessor = ColumnTransformer(

        transformers=[

            (
                "numeric",
                StandardScaler(),
                num_cols
            ),

            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                cat_cols
            )

        ]

    )

    return preprocessor

# =====================================================
# Available Models
# =====================================================

def get_models():

    return {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000,
                random_state=42
            ),

        "Random Forest":
            RandomForestClassifier(
                random_state=42
            ),

        "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=42
            ),

        "XGBoost":
            XGBClassifier(
                eval_metric="logloss",
                random_state=42
            )

    }

# =====================================================
# Evaluation
# =====================================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    return {

        "Accuracy": accuracy_score(y_test, predictions),

        "Precision": precision_score(y_test, predictions),

        "Recall": recall_score(y_test, predictions),

        "F1": f1_score(y_test, predictions)

    }

# =====================================================
# Main
# =====================================================

def main():

    print("=" * 50)
    print("AI on Cloud using AWS SageMaker")
    print("Model Training Pipeline")
    print("=" * 50)

    print("\nLoading dataset...")

    df = load_data()

    print(f"Dataset Shape: {df.shape}")

    X_train, X_test, y_train, y_test = split_data(df)

    cat_cols, num_cols = get_column_types(X_train)

    print("\nCategorical Columns:")
    print(cat_cols)

    print("\nNumerical Columns:")
    print(num_cols)

    preprocessor = create_preprocessor(
        cat_cols,
        num_cols
    )

    models = get_models()

    best_pipeline = None
    best_model_name = None
    best_f1 = 0

    print("\nStarting Training...\n")

    for name, model in models.items():

        print("-" * 50)
        print(f"Training: {name}")

        pipeline = Pipeline(

            steps=[

                ("preprocessor", preprocessor),

                ("classifier", model)

            ]

        )

        pipeline.fit(
            X_train,
            y_train
        )

        metrics = evaluate_model(
            pipeline,
            X_test,
            y_test
        )

        print(f"Accuracy : {metrics['Accuracy']:.4f}")
        print(f"Precision: {metrics['Precision']:.4f}")
        print(f"Recall   : {metrics['Recall']:.4f}")
        print(f"F1 Score : {metrics['F1']:.4f}")

        if metrics["F1"] > best_f1:

            best_f1 = metrics["F1"]
            best_pipeline = pipeline
            best_model_name = name

    joblib.dump(
        best_pipeline,
        ARTIFACTS_PATH / "churn_pipeline.pkl"
    )

    joblib.dump(
        X_test,
        ARTIFACTS_PATH / "X_test.pkl"
    )

    joblib.dump(
        y_test,
        ARTIFACTS_PATH / "y_test.pkl"
    )

    print("\n" + "=" * 50)
    print("Training Completed Successfully")
    print("=" * 50)

    print(f"\nBest Model : {best_model_name}")
    print(f"Best F1 Score : {best_f1:.4f}")

    print("\nArtifacts Saved:")

    print("✔ churn_pipeline.pkl")
    print("✔ X_test.pkl")
    print("✔ y_test.pkl")


if __name__ == "__main__":
    main()