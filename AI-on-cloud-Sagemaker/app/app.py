import streamlit as st

from api_client import (
    predict_customer,
    get_prediction_history
)

from ui_components import (
    show_header,
    show_sidebar,
    show_prediction,
    show_history
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(

    page_title="Customer Churn Prediction",

    page_icon="☁️",

    layout="wide"

)

# --------------------------------------------------
# Header
# --------------------------------------------------

show_sidebar()

show_header()

# --------------------------------------------------
# Model Information
# --------------------------------------------------

st.info(
    """
Model: Logistic Regression

ROC-AUC Score: 0.8416

Dataset: IBM Telco Customer Churn
"""
)

# --------------------------------------------------
# Customer Form
# --------------------------------------------------

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

with col2:

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

with col4:

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

predict_button = st.button(
    "Predict Customer",
    use_container_width=True
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    customer_data = {

        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total

    }

    with st.spinner("Predicting..."):

        result = predict_customer(customer_data)

    if "error" in result:

        st.error(result["error"])

    else:

        show_prediction(result)

# --------------------------------------------------
# Prediction History
# --------------------------------------------------

history = get_prediction_history()

show_history(history)