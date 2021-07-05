from modules.db.getConnection import getConnection

def loadAllItem():
    con = getConnection()

    cursor = con.cursor() 

    sql = 'select distinct it_id from g5_shop_item'
    cursor.execute(sql) 
    ids = cursor.fetchall()

    result = []
    for id in ids:
        result.append(int(id[0]))
    

    con.commit() 
    con.close() 
    return result
