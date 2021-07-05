from tensorflow import keras
import pandas as pd
from ..handleData.getDataset import getPredictDataSet
from ..handleData.getItemMap import getItemMap


def predictAction(model: keras.Model=None, itemMap: dict=getItemMap()):

  if not model:
    model = keras.models.load_model('./saved_model', compile=True)
  # 정수인코딩한 item_id를 디코딩하기 위한 itemMap
  

  dataToPredict = getPredictDataSet(itemMap)

  prediction = model.predict(dataToPredict)
  
  reversedItemMap = {}
  for k in itemMap:
    reversedItemMap[itemMap[k]] = k

  resultList = []
  for i in range(len(dataToPredict)):
      currentDataRow = dataToPredict.iloc[i]
      p = prediction[i]

      result = {
        'age': currentDataRow['user_age'],
        'gender': currentDataRow['user_gender'],
        'item': reversedItemMap[currentDataRow['item_id']],
        'action': p[0]
      }
      resultList.append(result)    
  

  return resultList