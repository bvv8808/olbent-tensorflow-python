from modules.db.getConnection import getConnection
from random import *

def loadTrainData():

    con = getConnection()

    cursor = con.cursor() 

    sql = 'select it_id from custom_view_list'
    cursor.execute(sql)
    fetchResult = cursor.fetchall()

    result = []
    for item in fetchResult:
        result.append({'item': item[0], 'age':randint(0, 100), 'gender':randint(0, 2)})



    con.commit() 
    con.close() 

    return result
