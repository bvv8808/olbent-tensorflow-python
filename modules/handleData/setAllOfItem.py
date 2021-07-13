from modules.handleData.hexToDec import hexToDec
from .makeCsvToPredict import makeCsvToPredict

def setAllOfItem(items: list):
    ## id, ca1, price

    # categoryDict 여기서 불러오기
    # for문 돌면서 categoryDict도 갱신
    # allOfItem.txt에 저장 후 categoryDict도 다시 저장
    fc = open('./data/categoryDict.txt', 'r+')
    cDict = {}
    while True:
        line = fc.readline()
        if not line:
            break

        arr = line.split(',')
        cDict[arr[0]] = float(arr[1])
    
    f = open('./data/allOfItem.txt', 'w')
    f.write('id,category,price\n')
    for item in items:
        ca1 = 0
        if item[1] in cDict:
            ca1 = cDict[item[1]]
        else:
            newCa1 = 0
            if len(item[1]) == 4:
                newCa1 = hexToDec(item[1]) / 69904
            else:
                newCa1 = hexToDec(item[1]) / 272
            cDict[item[1]] = newCa1
            ca1 = newCa1
            fc.write('{caHex},{caDec}\n'.format(caHex= item[1], caDec= newCa1))
        
        

        
        f.write('{id},{ca1},{price}\n'.format(id=item[0], ca1=ca1, price=item[2]))

    
    f.close()
    fc.close()

    ## 예측 데이터도 함께 생성
    # makeCsvToPredict(itemIds)
    
    return