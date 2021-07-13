from modules.handleData.getDataset import getTrainDataSet
from modules.handleModel.trainModel import *
from tensorflow.keras.models import save_model
def make():

    # 훈련시킬 데이터, 라벨 로드
    (trainData, trainLabels) = getTrainDataSet()


    ## 모델 생성 및 훈련 후, 훈련된 모델 반환
    trainedModel = train(trainData, trainLabels)
    save_model(trainedModel, './saved_model')

    return trainedModel