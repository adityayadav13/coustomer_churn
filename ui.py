import streamlit as st
import requests

# ---------------------------
# CONFIG
# ---------------------------
API_URL = "https://coustomer-churn.onrender.com/predict"

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# ---------------------------
# HEADER
# ---------------------------
st.title("📉 Customer Churn Prediction")
st.caption("Predict whether a customer is likely to churn using ML")

st.divider()

# ---------------------------
# INPUT FORM
# ---------------------------
with st.form("churn_form"):
    tenure = st.number_input("Tenure (months)", min_value=0, step=1)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0)

    contract = st.selectbox(
        "Contract Type",
        options=[0, 1, 2],
        format_func=lambda x: ["Month-to-month", "One year", "Two year"][x]
    )

    payment_method = st.selectbox(
        "Payment Method",
        options=[0, 1, 2, 3],
        format_func=lambda x: [
            "Electronic check",
            "Mailed check",
            "Bank transfer",
            "Credit card"
        ][x]
    )

    internet_service = st.selectbox(
        "Internet Service",
        options=[0, 1, 2],
        format_func=lambda x: ["No", "DSL", "Fiber optic"][x]
    )

    tech_support = st.radio("Tech Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
    online_security = st.radio("Online Security", [0, 1], format_func=lambda x: "Yes" if x else "No")

    support_calls = st.number_input("Support Calls (Last Month)", min_value=0, step=1)

    submit = st.form_submit_button("🔍 Predict")

# ---------------------------
# PREDICTION
# ---------------------------
if submit:
    payload = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "contract": contract,
        "payment_method": payment_method,
        "internet_service": internet_service,
        "tech_support": tech_support,
        "online_security": online_security,
        "support_calls": support_calls
    }

    with st.spinner("Predicting..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:
                result = response.json()

                prob = result["churn_probability"]
                pred = result["churn_prediction"]

                st.success("Prediction Completed ✅")
                st.metric("Churn Probability", f"{prob * 100:.2f}%")

                if pred == 1:
                    st.error("⚠️ High risk of customer churn")
                else:
                    st.succes
