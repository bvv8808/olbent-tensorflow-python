from tensorflow import keras
import pandas as pd
from ..handleData.getDataset import getPredictDataSet

def predictAction(model: keras.Model=None):

  if not model:
    model = keras.models.load_model('./saved_model', compile=True)
  # 정수인코딩한 item_id를 디코딩하기 위한 itemMap
  

  (dataToPredict, itemIds) = getPredictDataSet()

  # print(dataToPredict[:20])

  prediction = model.predict(dataToPredict)
  
  # print(prediction[:20])

  resultList = []
  for i in range(len(dataToPredict)):
      currentDataRow = dataToPredict.iloc[i]
      p = prediction[i]

      result = {
        'age': currentDataRow['age']*100,
        'gender': currentDataRow['gender'],
        'item': itemIds[i],
        'action': p[0]
      }
      resultList.append(result)    
  

  return resultList
  # return []