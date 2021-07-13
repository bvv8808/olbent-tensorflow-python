from .getItemList import *

def makeCsvToPredict(items: list = []):
    try:
        if not items:
            items = getItemList()
        
        f = open("./data/predict_dataset.csv", 'w')

        f.write('age,gender,category,price,item_id\n')

        for age in range(10, 100):
            for gender in range(0, 2):
                for item in items:
                    f.write("{age},{gender},{ca1},{price},{id}\n".format(age=age, gender=gender, ca1=item[1], price=item[2], id=item[0]))

        f.close()

        return True
    except:
        print('### Error in making csv to predict ###')
        return False
