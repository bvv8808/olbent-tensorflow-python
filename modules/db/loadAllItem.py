from modules.db.getConnection import getConnection
import datetime

def loadAllItem():
    now = str(datetime.datetime.now())[:19]
    con = getConnection()

    cursor = con.cursor() 

    sql = 'select distinct it_id, ca_id, it_price from g5_shop_item' + ' where it_4 > ' + "'"+now+"'"

    cursor.execute(sql) 
    items = cursor.fetchall()

    # result = []
    # for item in items:
    #     result.append(item)
    

    con.commit() 
    con.close() 
    return items
