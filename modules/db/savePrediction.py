from modules.db.getConnection import getConnection

def savePrediction(prediction: list):
    con = getConnection()

    cursor = con.cursor() 

    # 테이블 초기화
    sql = 'truncate table custom_recommend'
    cursor.execute(sql)


    sql = 'insert into custom_recommend values '
    listLength = len(prediction)
    for i in range(listLength):
        p = prediction[i]
        sql += "({age}, {gender}, {itemId}, {action})".format(age=p['age'], gender=p['gender'], itemId=p['item'], action=p['action'])

        if i < listLength-1:
            sql += ', '
        

    cursor.execute(sql)

    con.commit() 
    con.close() 
