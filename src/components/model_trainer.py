import os
import sys

from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class ModelTrainerConfig:

    trained_model_file_path = os.path.join(
        "models",
        "model.pkl"
    )


class ModelTrainer:

    def __init__(self):

        self.model_trainer_config = (
            ModelTrainerConfig()
        )

    def initiate_model_trainer(
        self,
        train_array,
        test_array
    ):

        try:

            logging.info(
                "Model Training Started"
            )

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            model = LogisticRegression(
                C=0.2,
                penalty="l2",
                max_iter=5000,
                random_state=42
            )

            model.fit(
                X_train,
                y_train
            )

            y_pred = model.predict(
                X_test
            )

            accuracy = accuracy_score(
                y_test,
                y_pred
            )

            logging.info(
                f"Model Accuracy : {accuracy}"
            )

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logging.info(
                "Model Saved Successfully"
            )

            return accuracy

        except Exception as e:

            raise CustomException(
                e,
                sys
            )