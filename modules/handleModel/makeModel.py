from modules.handleData.getDataset import getTrainDataSet
from modules.handleData.getItemMap import getItemMap
from modules.handleModel.trainModel import *
from tensorflow.keras.models import save_model
def make():


    ## 모든 item_id를 고유한 정수로 매핑한 딕셔너리(itemMap) 생성
    # - {id1: 0, id2: 1, ...}
    itemMap = getItemMap()

    ## item_id를 정수인코딩한 훈련데이터 로딩
    # - user_age, user_gender, item_id
    # -        21           0       0
    # -        38           1       3
    # -        19           0       2
    (trainData, trainLabels) = getTrainDataSet(itemMap)

    ## 모델 생성 및 훈련 후, 훈련된 모델 반환
    trainedModel = train(trainData, trainLabels)
    save_model(trainedModel, './saved_model')

    return trainedModel