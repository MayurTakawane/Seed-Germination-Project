import os
import sys
import pandas as pd
from src.exception import customException
from src.logger import logging
from src.utils import load_object
from dataclasses import dataclass

@dataclass
class predictionPipelineConfig:
    preprocessor_object_path = os.path.join('artifacts','preprocessor.pkl')
    model_object_path = os.path.join('artifacts','model.pkl')


class predictPipeline:
    def __init__(self):
        self.predict_pipeline_config = predictionPipelineConfig()

    def prediction(self,new_data_X_test):
        try:
            logging.info(f"New data : \n{new_data_X_test}")
            preprocessor = load_object(os.path.join('artifacts','preprocessor.pkl'))
            model = load_object(os.path.join('artifacts','model.pkl'))

            data_transform = preprocessor.transform(new_data_X_test)
            pred = model.predict(data_transform)
            return pred
        except Exception as e:
            logging.info("Error occured in predicton function in predictPipeline class in prediction_pipeline.py")
            raise customException(e,sys)
        
class customData:
    def __init__(self,Area:float,X:float,Y:float,XM:float,YM:float,Perimeter:float,BX:float,BY:float,Width:float,Height:float):
        self.Area = Area
        self.X = X
        self.Y = Y
        self.XM = XM
        self.YM = YM
        self.Perimeter = Perimeter
        self.BX = BX
        self.BY = BY
        self.Width = Width
        self.Height = Height

    def convert_data_into_dataframe(self):
        try:
            data_dict = {
                'Area' : [self.Area],
                'X' : [self.X],
                'Y' : [self.Y],
                'XM' : [self.XM],
                'YM' : [self.YM],
                'Perimeter' : [self.Perimeter],
                'BX' : [self.BX],
                'BY' : [self.BY],
                'Width' : [self.Width],
                'Height' : [self.Height]
            }

            df = pd.DataFrame(data_dict)
            return df
        except Exception as e:
            logging.info("Error occured in converting dataframe in prediction_pipeline.py")


