import streamlit as st
import pandas as pd

from src.pipeline.predict_pipeline import (
    CustomData,
    PredictPipeline
)

st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    layout="wide"
)

st.title("📊 Telco Customer Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure_months = st.number_input("Tenure Months", min_value=0.0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)
cltv = st.number_input("CLTV", min_value=0.0)

if st.button("Predict Churn"):

    data = CustomData(
        gender=gender,
        senior_citizen=senior_citizen,
        partner=partner,
        dependents=dependents,

        phone_service="Yes",
        multiple_lines="No",

        internet_service="Fiber optic",
        online_security="No",
        online_backup="No",
        device_protection="No",
        tech_support="No",
        streaming_tv="No",
        streaming_movies="No",

        contract="Month-to-month",
        paperless_billing="Yes",
        payment_method="Electronic check",

        tenure_months=tenure_months,
        monthly_charges=monthly_charges,
        total_charges=total_charges,
        cltv=cltv
    )

    pred_df = data.get_data_as_dataframe()

    pipeline = PredictPipeline()

    result = pipeline.predict(pred_df)

    if result[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Not Churn")