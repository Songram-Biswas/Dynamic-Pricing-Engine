import sys
import pandas as pd
from pricing_engine.exception import CustomException
from pricing_engine.utils.common import load_object
from pathlib import Path

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = Path("artifact/model_trainer//model.pkl")
            preprocessor_path = Path("artifact/data_transformation/transformed_object/preprocessor.pkl")
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 review_score: float,
                 product_weight_g: float,
                 product_volume_cm3: float,
                 purchase_month: int,
                 is_weekend: int,
                 delivery_delay: float,
                 payment_value: float,
                 product_category_name_english: str,
                 order_status: str,
                 customer_state: str,
                 seller_state: str,
                 payment_type: str):
        
        self.review_score = review_score
        self.product_weight_g = product_weight_g
        self.product_volume_cm3 = product_volume_cm3
        self.purchase_month = purchase_month
        self.is_weekend = is_weekend
        self.delivery_delay = delivery_delay
        self.payment_value = payment_value
        self.product_category_name_english = product_category_name_english
        self.order_status = order_status
        self.customer_state = customer_state
        self.seller_state = seller_state
        self.payment_type = payment_type

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "review_score": [self.review_score],
                "product_weight_g": [self.product_weight_g],
                "product_volume_cm3": [self.product_volume_cm3],
                "purchase_month": [self.purchase_month],
                "is_weekend": [self.is_weekend],
                "delivery_delay": [self.delivery_delay],
                "payment_value": [self.payment_value],
                "product_category_name_english": [self.product_category_name_english],
                "order_status": [self.order_status],
                "customer_state": [self.customer_state],
                "seller_state": [self.seller_state],
                "payment_type": [self.payment_type]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)