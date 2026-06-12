from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import (
    CustomData,
    PredictPipeline
)

application = Flask(__name__)

app = application


@app.route("/")
def index():

    return render_template(
        "home.html"
    )


@app.route("/prediction")
def prediction_page():

    return render_template(
        "predict.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    data = CustomData(

        gender=request.form.get(
            "gender"
        ),

        senior_citizen=request.form.get(
            "senior_citizen"
        ),

        partner=request.form.get(
            "partner"
        ),

        dependents=request.form.get(
            "dependents"
        ),

        phone_service=request.form.get(
            "phone_service"
        ),

        multiple_lines=request.form.get(
            "multiple_lines"
        ),

        internet_service=request.form.get(
            "internet_service"
        ),

        online_security=request.form.get(
            "online_security"
        ),

        online_backup=request.form.get(
            "online_backup"
        ),

        device_protection=request.form.get(
            "device_protection"
        ),

        tech_support=request.form.get(
            "tech_support"
        ),

        streaming_tv=request.form.get(
            "streaming_tv"
        ),

        streaming_movies=request.form.get(
            "streaming_movies"
        ),

        contract=request.form.get(
            "contract"
        ),

        paperless_billing=request.form.get(
            "paperless_billing"
        ),

        payment_method=request.form.get(
            "payment_method"
        ),

        tenure_months=float(
            request.form.get(
                "tenure_months"
            )
        ),

        monthly_charges=float(
            request.form.get(
                "monthly_charges"
            )
        ),

        total_charges=float(
            request.form.get(
                "total_charges"
            )
        ),

        cltv=float(
            request.form.get(
                "cltv"
            )
        )
    )

    pred_df = data.get_data_as_dataframe()

    print("\n==============================")
    print("INPUT DATA")
    print(pred_df)
    print("==============================\n")

    predict_pipeline = PredictPipeline()

    result = predict_pipeline.predict(
        pred_df
    )

    print("RAW PREDICTION :", result)

    prediction = (
        "Customer Will Churn"
        if result[0] == 1
        else
        "Customer Will Not Churn"
    )

    print("FINAL PREDICTION :", prediction)
    print("==============================\n")

    return render_template(
        "result.html",
        prediction=prediction
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        debug=True
    )