import json
import pymysql

def getConnection():
    f = open('./modules/db/config.json', 'r')
    arrJson = f.readlines()
    j = json.loads(''.join(arrJson))
    
    f.close()
    return pymysql.connect(host=j['host'], user=j['user'], password=j['password'], db=j['db'], charset='utf8')
