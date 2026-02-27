import sys
from pricing_engine.logger import logging
from pricing_engine.exception import CustomException

try:
    logging.info("Testing the logging setup...")
    result = 10 / 0
except Exception as e:
    raise CustomException(e, sys)