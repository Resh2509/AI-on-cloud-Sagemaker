import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/cleaned_data.csv")
OUTPUT_FILE = Path("data/processed/ml_ready_data.csv")


def load_data():
    return pd.read_csv(INPUT_FILE)


def feature_engineering(df):

    # Convert target variable
    df["Churn"] = df["Churn"].map({
        "No": 0,
        "Yes": 1
    })

    # One-hot encode categorical columns
    df = pd.get_dummies(
        df,
        drop_first=True
    )

    return df


def save_data(df):
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )


def main():

    print("Loading cleaned data...")

    df = load_data()

    print("Performing feature engineering...")

    df = feature_engineering(df)

    print("Saving ML-ready dataset...")

    save_data(df)

    print("Final Shape:")
    print(df.shape)


if __name__ == "__main__":
    main()