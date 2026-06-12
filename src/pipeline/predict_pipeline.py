import os
import sys

import pandas as pd

from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:

    def __init__(self):
        pass

    def predict(self, features):

        try:

            model_path = os.path.join(
                "models",
                "model.pkl"
            )

            preprocessor_path = os.path.join(
                "models",
                "preprocessor.pkl"
            )

            model = load_object(
                model_path
            )

            preprocessor = load_object(
                preprocessor_path
            )

            data_scaled = preprocessor.transform(
                features
            )

            prediction = model.predict(
                data_scaled
            )

            return prediction

        except Exception as e:

            raise CustomException(
                e,
                sys
            )


class CustomData:

    def __init__(
        self,
        gender,
        senior_citizen,
        partner,
        dependents,
        phone_service,
        multiple_lines,
        internet_service,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        contract,
        paperless_billing,
        payment_method,
        tenure_months,
        monthly_charges,
        total_charges,
        cltv
    ):

        self.gender = gender
        self.senior_citizen = senior_citizen
        self.partner = partner
        self.dependents = dependents
        self.phone_service = phone_service
        self.multiple_lines = multiple_lines
        self.internet_service = internet_service
        self.online_security = online_security
        self.online_backup = online_backup
        self.device_protection = device_protection
        self.tech_support = tech_support
        self.streaming_tv = streaming_tv
        self.streaming_movies = streaming_movies
        self.contract = contract
        self.paperless_billing = paperless_billing
        self.payment_method = payment_method
        self.tenure_months = tenure_months
        self.monthly_charges = monthly_charges
        self.total_charges = total_charges
        self.cltv = cltv

    def get_data_as_dataframe(self):

        custom_data_input_dict = {

            "Gender": [self.gender],

            "Senior Citizen": [self.senior_citizen],

            "Partner": [self.partner],

            "Dependents": [self.dependents],

            "Phone Service": [self.phone_service],

            "Multiple Lines": [self.multiple_lines],

            "Internet Service": [self.internet_service],

            "Online Security": [self.online_security],

            "Online Backup": [self.online_backup],

            "Device Protection": [self.device_protection],

            "Tech Support": [self.tech_support],

            "Streaming TV": [self.streaming_tv],

            "Streaming Movies": [self.streaming_movies],

            "Contract": [self.contract],

            "Paperless Billing": [self.paperless_billing],

            "Payment Method": [self.payment_method],

            "Tenure Months": [self.tenure_months],

            "Monthly Charges": [self.monthly_charges],

            "Total Charges": [self.total_charges],

            "CLTV": [self.cltv]
        }

        return pd.DataFrame(
            custom_data_input_dict
        )