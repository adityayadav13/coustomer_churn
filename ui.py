import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")

st.title("📉 Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", min_value=0, step=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

contract = st.selectbox(
    "Contract Type",
    [0, 1, 2],
    format_func=lambda x: ["Month-to-month", "One year", "Two year"][x]
)

payment_method = st.selectbox(
    "Payment Method",
    [0, 1, 2, 3],
    format_func=lambda x: ["Electronic check", "Mailed check",
                           "Bank transfer", "Credit card"][x]
)

internet_service = st.selectbox(
    "Internet Service",
    [0, 1, 2],
    format_func=lambda x: ["No", "DSL", "Fiber optic"][x]
)

tech_support = st.selectbox("Tech Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
online_security = st.selectbox("Online Security", [0, 1], format_func=lambda x: "Yes" if x else "No")

support_calls = st.number_input("Support Calls", min_value=0, step=1)

if st.button("🔍 Predict Churn"):
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

    response = requests.post("https://coustomer-churn.onrender.com/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Churn Probability: {result['churn_probability']}")

        if result["churn_prediction"] == 1:
            st.error("⚠️ High risk of churn")
        else:
            st.success("🟢 Customer likely to stay")
