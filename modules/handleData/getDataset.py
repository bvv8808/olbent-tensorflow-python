from .getItemMap import getItemMap
import pandas as pd
from sklearn.model_selection import train_test_split


def getTrainDataSet(itemMap:dict=getItemMap()):
    data = pd.read_csv('./data/initial_dataset.csv')
    data.pop('action_hour')
    labels = data.pop('action')
    
    # print(data['item_id'])

    data['item_id'] = data['item_id'].map(lambda id: itemMap[str(id)])

    X = data
    y = labels.values


    return (X, y)

def getPredictDataSet(itemMap:dict):
    data = pd.read_csv('./data/predict_dataset.csv')
    data['item_id'] = data['item_id'].map(lambda id: itemMap[str(id)])
    return data
