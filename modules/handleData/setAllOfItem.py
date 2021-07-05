from .makeCsvToPredict import makeCsvToPredict

def setAllOfItem(itemIds: list):
    f = open('./data/allOfItem.txt', 'w')
    for id in itemIds:
        f.write(str(id)+'\n')
    
    f.close()

    ## 예측 데이터도 함께 생성
    makeCsvToPredict(itemIds)
    
    return