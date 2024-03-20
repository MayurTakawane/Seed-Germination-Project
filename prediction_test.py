from src.pipeline.prediction_pipeline import predictPipeline,customData
from src.logger import logging
import numpy as np
import pandas as pd

data = pd.read_csv('get_data/excelData/Results.csv')
data = data.drop(columns=' ')

area = []
x = []
y = []
xm = []
ym = []
perim = []
bx = []
by = []
width = []
height = []

i = 0
while(len(data) > 0):
    area.append(data['Area'][i])
    x.append(data['X'][i])
    y.append(data['Y'][i])
    xm.append(data['XM'][i])
    ym.append(data['YM'][i])
    perim.append(data['Perim.'][i])
    bx.append(data['BX'][i])
    by.append(data['BY'][i])
    width.append(data['Width'][i])
    height.append(data['Height'][i])
    data.drop([i],axis=0)
    i = i + 1
    if i == 100:
        break

i = 0
while(i < 100):
    data=customData(    
        Area = float(np.round(area[i])),
        X = float(np.round(x[i])),
        Y = float(np.round(y[i])),
        XM = float(np.round(xm[i])),
        YM = float(np.round(ym[i])),
        Perimeter = float(np.round(perim[i])),
        BX = float(np.round(bx[i])),
        BY = float(np.round(by[i])),
        Width = float(np.round(width[i])),
        Height = float(np.round(height[i]))
    )
    dataframe = data.convert_data_into_dataframe()
    # print(dataframe)
    pred = predictPipeline()
    results = pred.prediction(dataframe)
    if results == 'yes':
        print(f'Result ===> The Seed {i} will Grow')
    else:
        print(f'Result ===> The Seed {i} will not Grow')
    print(results)
    i = i + 1

## Project status all done just do UI and after that train model properly
    
# Result after running above code 
'''
   Area     X     Y    XM    YM  Perimeter    BX    BY  Width  Height
0  70.0  10.0  10.0  20.0  40.0       20.0  20.0  20.0  100.0    20.0
Result ===> The Seed will Grow

'''