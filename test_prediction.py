from src.pipeline.predict_pipeline import (
    CustomData,
    PredictPipeline
)

data = CustomData(
    gender="Male",
    senior_citizen="No",
    partner="Yes",
    dependents="No",
    phone_service="Yes",
    multiple_lines="No",
    internet_service="Fiber optic",
    online_security="No",
    online_backup="Yes",
    device_protection="No",
    tech_support="No",
    streaming_tv="Yes",
    streaming_movies="Yes",
    contract="Month-to-month",
    paperless_billing="Yes",
    payment_method="Electronic check",
    tenure_months=5,
    monthly_charges=80,
    total_charges=400,
    cltv=3500
)

pred_df = data.get_data_as_dataframe()

print("\nINPUT DATA")
print(pred_df)

predict_pipeline = PredictPipeline()

result = predict_pipeline.predict(pred_df)

print("\nRAW PREDICTION :", result)

if result[0] == 1:
    print("\nFINAL PREDICTION : Customer Will Churn")
else:
    print("\nFINAL PREDICTION : Customer Will Not Churn")