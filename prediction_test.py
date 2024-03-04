from src.pipeline.prediction_pipeline import predictPipeline,customData
from src.logger import logging
import numpy as np
# 79.683	207.517	16.666	207.517	16.666	33.718	202.295	11.274	10.210	10.636
# 90.905	156.462	17.018	156.462	17.018	35.471	151.242	11.274	10.636	11.274
data=customData(
    Area = float(90),
    X = float(16),
    Y = float(455),
    XM = float(200),
    YM = float(100),
    Perimeter = float(30),
    BX = float(100),
    BY = float(100),
    Width = float(20),
    Height = float(20)
)
dataframe = data.convert_data_into_dataframe()
print(dataframe)

pred = predictPipeline()
results = pred.prediction(dataframe)
if results == 'yes':
    print('Result ===> The Seed will Grow')
else:
    print('Result ===> The Seed will not Grow')

print(results)

## Project status all done now only create app with flask 
    
# Result after running above code 
'''
   Area     X     Y    XM    YM  Perimeter    BX    BY  Width  Height
0  70.0  10.0  10.0  20.0  40.0       20.0  20.0  20.0  100.0    20.0
Result ===> The Seed will Grow

'''