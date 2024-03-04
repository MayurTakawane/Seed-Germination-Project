import os 
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import customException
from src.component.data_ingestion import dataIngestion
from src.component.data_transformation import dataTransformtion
from src.component.model_training import modelTraining


logging.info("-------Data Ingestion started-------")
data_ingestion = dataIngestion()
train_path,test_path = data_ingestion.initiate_data_ingestion()
logging.info("-------Data Ingestion successfull-------")
logging.info("=======================================================================")


logging.info("-------Data Transformation started-------")
data_transformation = dataTransformtion()
X_train,y_train,X_test,y_test,preprocessor_path = data_transformation.initiate_data_transformation(train_path,test_path)
logging.info("-------Data Transformation successfull-------")
logging.info("=======================================================================")


logging.info("-------Model Training started-------")
model_trainer = modelTraining()
model_trainer.initiate_model_training(X_train,y_train,X_test,y_test)
logging.info("-------Model Training successfull-------")
logging.info("=======================================================================")