import joblib
import pandas as pd


PIPELINE = joblib.load("artifacts/churn_pipeline.pkl")


def get_risk(probability):

    if probability < 0.30:
        return "Low"

    elif probability < 0.70:
        return "Medium"

    return "High"


def predict(customer):

    df = pd.DataFrame([customer])

    prediction = PIPELINE.predict(df)[0]

    probability = PIPELINE.predict_proba(df)[0][1]

    result = {

        "prediction": (
            "Customer is likely to churn"
            if prediction == 1
            else "Customer is likely to stay"
        ),

        "probability": round(float(probability), 4),

        "risk_level": get_risk(probability)

    }

    return result