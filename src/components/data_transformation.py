import os
import sys

import pandas as pd
import numpy as np

from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:

    preprocessor_obj_file_path = os.path.join(
        "models",
        "preprocessor.pkl"
    )


class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(
        self,
        train_path,
        test_path
    ):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info(
                "Train and Test Data Loaded"
            )

            columns_to_drop = [
                "CustomerID",
                "Count",
                "Country",
                "State",
                "City",
                "Zip Code",
                "Lat Long",
                "Latitude",
                "Longitude",
                "Churn Value",
                "Churn Score",
                "Churn Reason"
            ]

            train_df.drop(
                columns=columns_to_drop,
                inplace=True
            )

            test_df.drop(
                columns=columns_to_drop,
                inplace=True
            )

            train_df["Churn Label"] = train_df[
                "Churn Label"
            ].map({
                "No": 0,
                "Yes": 1
            })

            test_df["Churn Label"] = test_df[
                "Churn Label"
            ].map({
                "No": 0,
                "Yes": 1
            })

            target_column = "Churn Label"

            X_train = train_df.drop(
                columns=[target_column]
            )

            y_train = train_df[target_column]

            X_test = test_df.drop(
                columns=[target_column]
            )

            y_test = test_df[target_column]

            cat_cols = X_train.select_dtypes(
                include="object"
            ).columns

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "cat",
                        OneHotEncoder(
                            handle_unknown="ignore"
                        ),
                        cat_cols
                    )
                ],
                remainder="passthrough"
            )

            X_train = preprocessor.fit_transform(
                X_train
            )

            X_test = preprocessor.transform(
                X_test
            )

            train_arr = np.c_[
                X_train,
                np.array(y_train)
            ]

            test_arr = np.c_[
                X_test,
                np.array(y_test)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )

            logging.info(
                "Preprocessor Saved Successfully"
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)