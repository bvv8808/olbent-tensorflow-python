
from modules.db.loadTrain import loadTrainData
from modules.handleData.makeCsvToPredict import makeCsvToPredict
from modules.handleData.setAllOfItem import setAllOfItem
from modules.db.loadAllItem import loadAllItem

def setData():

    itemList = loadAllItem()
    setAllOfItem(itemList) # data/allOfItem.txt
    makeCsvToPredict(itemList) # data/predict_dataset.csv

    trainList = loadTrainData()
    f = open('./data/initial_dataset2.csv', 'w')
    f.write('user_age,user_gender,item_id,action\n') # data/initial_dataset2.csv
    for t in trainList:
        f.write("{age},{gender},{itemId}\n".format(age=t['age'], gender=t['gender'], itemId=t['item']))
    

    return

setData()
