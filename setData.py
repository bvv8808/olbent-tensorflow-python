
from modules.db.loadTrain import loadTrainData
from modules.handleData.makeCsvToPredict import makeCsvToPredict
from modules.handleData.setAllOfItem import setAllOfItem
from modules.db.loadAllItem import loadAllItem



itemList = loadAllItem()    # 등록된 모든 아이템(기간 종료된 상품 제외, 카테고리값 전처리 전)
setAllOfItem(itemList)      # data/allOfItem.txt작성, data/categoryDict.txt갱신
makeCsvToPredict()          # data/predict_dataset.csv에 예측할 데이터 작성

trainList = loadTrainData()
f = open('./data/initial_dataset.csv', 'w')
f.write('age,gender,category,price,action\n') # data/initial_dataset.csv
for t in trainList:
    f.write("{age},{gender},{category},{price},{action}\n".format(age=t['age'], gender=t['gender'], category=t['category'], price=t['price'], action=t['action']))
