import os
import sys
from src.exception import customException
from src.logger import logging
import pickle
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import random
from flask import send_file

def save_object(file_path,object):
    try:
        # create directory
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        # dump object as pickle
        with open(file_path,"wb") as f:
            pickle.dump(object,f)

    except Exception as e:
        logging("Error ocurred in utils, function --> save object")
        raise customException
    
def evalute_model(X_train,y_train,X_test,y_test,models):
    
    try:

        report = {}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)
            
            y_pred=model.predict(X_test)
            
            accuracy=round(accuracy_score(y_test,y_pred)*100,2)
            
            report[list(models.keys())[i]]=accuracy
    
        return report
    
    except Exception as e:
        logging.info("Error occured in evalute_model function in utils")
        raise customException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as f:
            return pickle.load(f)
    except Exception as e:
        logging.info("Error occured in load_object function in utils")
        raise customException(e,sys)
    
def clean_results(results_dict):
    percentage = random.uniform(0.1, 0.4)
    num_no_results = int(len(results_dict) * percentage)
    no_result_keys = random.sample(list(results_dict.keys()), num_no_results)
    # Set the corresponding values to "no"
    for key in no_result_keys:
        results_dict[key] = 'no'
