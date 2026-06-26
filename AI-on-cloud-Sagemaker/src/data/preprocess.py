import pandas as pd
from pathlib import Path

# Paths
RAW_DATA = Path("data/raw/telco_churn.csv")
PROCESSED_DATA = Path("data/processed/cleaned_data.csv")


def load_data():
    df = pd.read_csv(RAW_DATA)
    return df


def clean_data(df):

    # Remove customer ID
    df = df.drop("customerID", axis=1)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

    return df


def save_data(df):
    df.to_csv(PROCESSED_DATA, index=False)


def main():

    print("Loading data...")

    df = load_data()

    print("Cleaning data...")

    df = clean_data(df)

    print("Saving cleaned dataset...")

    save_data(df)

    print("Done!")
    print(df.shape)


if __name__ == "__main__":
    main()