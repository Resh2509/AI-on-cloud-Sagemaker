import streamlit as st
import pandas as pd

from utils import (
    format_probability,
    format_timestamp,
    risk_color,
    prediction_icon
)


def show_header():

    st.title("☁️ AI on Cloud using AWS SageMaker")

    st.subheader("Customer Churn Prediction Dashboard")

    st.markdown("---")


def show_sidebar():

    st.sidebar.title("📊 Project Information")

    st.sidebar.write("**Model:** Logistic Regression")

    st.sidebar.write("**Dataset:** IBM Telco Customer Churn")

    st.sidebar.write("**Backend:** FastAPI")

    st.sidebar.write("**Database:** SQLite")

    st.sidebar.write("**Frontend:** Streamlit")

    st.sidebar.write("**Deployment:** AWS SageMaker (Planned)")


def show_prediction(result):

    st.markdown("## Prediction Result")

    icon = prediction_icon(result["prediction"])

    st.success(f"{icon} {result['prediction']}")

    st.metric(

        "Probability",

        format_probability(result["probability"])

    )

    st.metric(

        "Risk Level",

        f"{risk_color(result['risk_level'])} {result['risk_level']}"

    )


def show_history(history):

    st.markdown("---")

    st.subheader("Prediction History")

    if not history:

        st.info("No prediction history available.")

        return

    df = pd.DataFrame(history)

    df["probability"] = df["probability"].apply(
        format_probability
    )

    df["risk_level"] = df["risk_level"].apply(
        lambda x: f"{risk_color(x)} {x}"
    )

    df["created_at"] = df["created_at"].apply(
        format_timestamp
    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )