import os
import sys
from dataclasses import dataclass
import numpy as np
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from pricing_engine.exception import CustomException
from pricing_engine.logger import logging
from pricing_engine.utils.common import save_object
from pricing_engine.entity.config_entity import ModelTrainerConfig
from pricing_engine.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, 
                 data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)

    def evaluate_models(self, X_train, y_train, X_test, y_test, models):
        try:
            report = {}
            for i in range(len(list(models))):
                model = list(models.values())[i]
                model.fit(X_train, y_train)
                y_test_pred = model.predict(X_test)
                test_model_score = r2_score(y_test, y_test_pred)
                report[list(models.keys())[i]] = test_model_score
            return report
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Loading transformed training and testing data")
            train_array = np.load(self.data_transformation_artifact.transformed_train_file_path)
            test_array = np.load(self.data_transformation_artifact.transformed_test_file_path)

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "RandomForest": RandomForestRegressor(),
                "XGBoost": XGBRegressor()
            }

            model_report: dict = self.evaluate_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models
            )

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found with acceptable R2 score")

            logging.info(f"Best found model on both training and testing dataset: {best_model_name}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            return ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                r2_score=best_model_score
            )

        except Exception as e:
            raise CustomException(e, sys)