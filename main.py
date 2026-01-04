from fastapi import FastAPI

import joblib
import numpy as np

model = joblib.load("model.pkl")

app = FastAPI()

@app.post("/predict")
def predict_churn(data: dict):

    # Convert input to model format
    features = np.array([[
        data.tenure,
        data.monthly_charges,
        data.total_charges,
        data.contract,
        data.payment_method,
        data.internet_service,
        data.tech_support,
        data.online_security,
        data.support_calls
    ]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return {
                "customer_id": data.customer_id,
                "churn_prediction": int(prediction),
                "churn_probability": round(float(probability), 4)
            }
