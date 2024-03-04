import os
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from dataclasses import dataclass
from src.exception import customException
from src.logger import logging
from src.utils import evalute_model,save_object

@dataclass
class modelTrainingConfig:
    model_trainer_path = os.path.join('artifacts','model.pkl')

class modelTraining:
    def __init__(self):
        self.model_trainer_config = modelTrainingConfig()

    def initiate_model_training(self,X_train,y_train,X_test,y_test):

        try:

            models = {
                "random_forest":RandomForestClassifier(n_estimators=50,max_depth=3,criterion='gini',oob_score=True),
                "logistic_regression":LogisticRegression(),
                "decision_tree":DecisionTreeClassifier()
            }

            model_report = evalute_model(X_train,y_train,X_test,y_test,models)
            print('\n====================================================================================\n')
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # get best model score form report
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.model_trainer_path,
                object=best_model
            )
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customException(e,sys)
