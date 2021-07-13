import pandas as pd
from sklearn.model_selection import train_test_split


def getTrainDataSet():
    data = pd.read_csv('./data/initial_dataset.csv')
    # data.pop('item_id')
    data['age'] = data['age'].map(lambda x: x/100)
    data['price'] = data['price'].map(lambda x: x/1000)
    labels = data.pop('action')
    

    X = data
    y = labels.values
    return (X, y)

def getPredictDataSet():
    data = pd.read_csv('./data/predict_dataset.csv')
    data['age'] = data['age'].map(lambda x: x/100)
    data['price'] = data['price'].map(lambda x: x/1000)
    ids = data.pop('item_id')
    return (data, ids)
