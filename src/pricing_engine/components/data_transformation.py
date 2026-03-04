# import os
# import sys
# import numpy as np
# import pandas as pd
# from pathlib import Path
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.pipeline import Pipeline
# from pricing_engine.entity.config_entity import DataTransformationConfig
# from pricing_engine.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact
# from pricing_engine.exception import CustomException
# from pricing_engine.logger import logging
# from pricing_engine.utils.common import read_yaml, save_object # save_object ফাংশনটি utils-এ থাকতে হবে

# class DataTransformation:
#     def __init__(self, data_ingestion_artifact: DataIngestionArtifact, 
#                  data_transformation_config: DataTransformationConfig):
#         try:
#             self.data_ingestion_artifact = data_ingestion_artifact
#             self.data_transformation_config = data_transformation_config
#             self.schema_config = read_yaml(Path("config/schema.yaml"))
#         except Exception as e:
#             raise CustomException(e, sys)

#     def get_data_transformer_object(self):
#         try:
#             numerical_columns = self.schema_config.numerical_columns
#             categorical_columns = self.schema_config.categorical_columns

#             num_pipeline = Pipeline(steps=[
#                 ("imputer", SimpleImputer(strategy="median")),
#                 ("scaler", StandardScaler())
#             ])

#             cat_pipeline = Pipeline(steps=[
#                 ("imputer", SimpleImputer(strategy="most_frequent")),
#                 ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")),
#                 ("scaler", StandardScaler(with_mean=False))
#             ])

#             preprocessor = ColumnTransformer([
#                 ("num_pipeline", num_pipeline, numerical_columns),
#                 ("cat_pipeline", cat_pipeline, categorical_columns)
#             ])

#             return preprocessor
#         except Exception as e:
#             raise CustomException(e, sys)

#     # def initiate_data_transformation(self) -> DataTransformationArtifact:
#     #     try:
#     #         logging.info("Starting Data Transformation...")
#     #         train_df = pd.read_csv(self.data_ingestion_artifact.trained_file_path)
#     #         test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

#     #         input_feature_train_df = train_df.drop(columns=["price"], axis=1) # price হলো টার্গেট
#     #         target_feature_train_df = train_df["price"]

#     #         input_feature_test_df = test_df.drop(columns=["price"], axis=1)
#     #         target_feature_test_df = test_df["price"]

#     #         preprocessing_obj = self.get_data_transformer_object()
            
#     #         # ফিটিং এবং ট্রান্সফরমেশন
#     #         input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
#     #         input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

#     #         train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
#     #         test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#     #         # ফাইল সেভ করা
#     #         os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_file_path), exist_ok=True)
#     #         np.save(self.data_transformation_config.transformed_train_file_path, train_arr)
#     #         np.save(self.data_transformation_config.transformed_test_file_path, test_arr)

#     #         os.makedirs(os.path.dirname(self.data_transformation_config.transformed_object_file_path), exist_ok=True)
#     #         save_object(self.data_transformation_config.transformed_object_file_path, preprocessing_obj)

#     #         return DataTransformationArtifact(
#     #             transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
#     #             transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
#     #             transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
#     #         )
#     #     except Exception as e:
#     #         raise CustomException(e, sys)
#     def initiate_data_transformation(self) -> DataTransformationArtifact:
#         try:
#             logging.info("Starting Data Transformation...")
#             train_df = pd.read_csv(self.data_ingestion_artifact.trained_file_path)
#             test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

#             input_feature_train_df = train_df.drop(columns=["price"], axis=1)
#             target_feature_train_df = train_df["price"]

#             input_feature_test_df = test_df.drop(columns=["price"], axis=1)
#             target_feature_test_df = test_df["price"]

#             preprocessing_obj = self.get_data_transformer_object()
            
#             # Fitting and Transformation
#             input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
#             input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

#             # সমাধান: Sparse Matrix কে Dense Array তে রূপান্তর করা
#             # এটি নিশ্চিত করবে যে ইনপুট ফিচারের আকার এবং টার্গেট ডাটার আকার মিলবে
#             input_feature_train_arr = input_feature_train_arr.toarray() if hasattr(input_feature_train_arr, "toarray") else input_feature_train_arr
#             input_feature_test_arr = input_feature_test_arr.toarray() if hasattr(input_feature_test_arr, "toarray") else input_feature_test_arr

#             # এখন ডাটা জোড়া দেওয়া (Concatenate) সম্ভব হবে
#             train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
#             test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#             # ফাইল সেভ করা (আগের মতোই থাকবে)
#             os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_file_path), exist_ok=True)
#             np.save(self.data_transformation_config.transformed_train_file_path, train_arr)
#             np.save(self.data_transformation_config.transformed_test_file_path, test_arr)

#             save_object(self.data_transformation_config.transformed_object_file_path, preprocessing_obj)

#             return DataTransformationArtifact(
#                 transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
#                 transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
#                 transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
#             )
#         except Exception as e:
#             raise CustomException(e, sys)
import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from pricing_engine.entity.config_entity import DataTransformationConfig
from pricing_engine.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact
from pricing_engine.exception import CustomException
from pricing_engine.logger import logging
from pricing_engine.utils.common import read_yaml, save_object

class DataTransformation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, 
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_config = data_transformation_config
            self.schema_config = read_yaml(Path("config/schema.yaml"))
        except Exception as e:
            raise CustomException(e, sys)

    def get_engineered_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        trials.ipynb থেকে ফিচার ইঞ্জিনিয়ারিং লজিকগুলো এখানে যুক্ত করা হয়েছে।
        """
        try:
            logging.info("Applying custom feature engineering logic...")
            
            # ১. তারিখ রূপান্তর
            date_cols = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
            for col in date_cols:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col])

            # ২. প্রডাক্ট ভলিউম (product_volume_cm3)
            df['product_volume_cm3'] = df['product_length_cm'] * df['product_height_cm'] * df['product_width_cm']

            # ৩. সময়ভিত্তিক ফিচার (Month, Weekend)
            if 'order_purchase_timestamp' in df.columns:
                df['purchase_month'] = df['order_purchase_timestamp'].dt.month
                df['is_weekend'] = df['order_purchase_timestamp'].dt.dayofweek.isin([5, 6]).astype(int)

            # ৪. ডেলিভারি ডিলে (delivery_delay)
            if 'order_delivered_customer_date' in df.columns and 'order_purchase_timestamp' in df.columns:
                df['delivery_time_actual'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
                df['delivery_time_estimated'] = (df['order_estimated_delivery_date'] - df['order_purchase_timestamp']).dt.days
                df['delivery_delay'] = df['delivery_time_actual'] - df['delivery_time_estimated']
                
                # মিসিং ভ্যালু হ্যান্ডলিং (মেডিয়ান দিয়ে)
                df['delivery_delay'] = df['delivery_delay'].fillna(df['delivery_delay'].median())

            # ৫. অপ্রয়োজনীয় কলাম ড্রপ (যা ট্রায়ালে করেছিলেন)
            cols_to_drop = [
                'order_id', 'product_id', 'seller_id', 'customer_id', 'customer_unique_id', 
                'review_id', 'shipping_limit_date', 'order_purchase_timestamp', 
                'order_approved_at', 'order_delivered_carrier_date', 
                'order_delivered_customer_date', 'order_estimated_delivery_date',
                'review_comment_title', 'review_comment_message', 'review_creation_date', 
                'review_answer_timestamp', 'product_category_name', 'customer_city', 'seller_city'
            ]
            df = df.drop(columns=[c for c in cols_to_drop if c in df.columns], axis=1)
            
            return df
        except Exception as e:
            raise CustomException(e, sys)

    def get_data_transformer_object(self):
        try:
            # স্কিমার নতুন নাম অনুযায়ী লোড করুন
            numerical_columns = self.schema_config.transformation_numerical_columns
            categorical_columns = self.schema_config.transformation_categorical_columns

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                ("scaler", StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info("Starting Data Transformation...")
            train_df = pd.read_csv(self.data_ingestion_artifact.trained_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # নতুন ফিচারগুলো তৈরি করা (Engineered Features)
            train_df = self.get_engineered_features(train_df)
            test_df = self.get_engineered_features(test_df)

            target_column_name = "price"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            preprocessing_obj = self.get_data_transformer_object()
            
            # Fitting and Transformation
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Sparse Matrix কে Dense Array তে রূপান্তর করা
            input_feature_train_arr = input_feature_train_arr.toarray() if hasattr(input_feature_train_arr, "toarray") else input_feature_train_arr
            input_feature_test_arr = input_feature_test_arr.toarray() if hasattr(input_feature_test_arr, "toarray") else input_feature_test_arr

            # Concatenation
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # ফাইল সেভ করা
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_train_file_path), exist_ok=True)
            np.save(self.data_transformation_config.transformed_train_file_path, train_arr)
            np.save(self.data_transformation_config.transformed_test_file_path, test_arr)

            save_object(self.data_transformation_config.transformed_object_file_path, preprocessing_obj)

            return DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)