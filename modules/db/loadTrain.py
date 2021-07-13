from modules.db.getConnection import getConnection
from modules.handleData.getCategoryDict import getCategoryDict
from modules.handleData.hexToDec import hexToDec
from random import *
from datetime import datetime

def loadTrainData():
    thisYear = datetime.today().year
    dCategory = getCategoryDict()

    con = getConnection()

    cursor = con.cursor() 

    sql = 'SELECT * FROM train_dataset'
    cursor.execute(sql)
    fetchResult = cursor.fetchall()
    # itemId, gender, birth, category, price

    result = []
    for item in fetchResult:
        cur = {}


        # age
        if item[0] != '':
            age = thisYear - int(item[0].split('-')[0]) + 1
            cur['age'] = age
        else:
            cur['age'] = randint(19, 30)
        
        # gender
        if item[1] != '':
            cur['gender'] = int(item[1])
        else:
            cur['gender'] = randint(0, 1)

        # category
        if item[2] in dCategory:
            cur['category'] = dCategory[item[2]]
        else:
            cur['category'] = hexToDec(item[2])
        

        
        # price
        cur['price'] = item[3]

        # action
        cur['action'] = item[4]


        result.append(cur)

    # print(result)

    con.commit() 
    con.close() 

    return result
