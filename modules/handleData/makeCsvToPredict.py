from .getItemList import *

def makeCsvToPredict(items: list = []):
    try:
        if not items:
            items = getItemList()
        
        f = open("./data/predict_dataset.csv", 'w')

        f.write('user_age,user_gender,item_id\n')

        for age in range(10, 100):
            for gender in range(0, 2):
                for item in items:
                    f.write("{age},{gender},{item}\n".format(age=age, gender=gender, item=item))

        f.close()

        return True
    except:
        print('### Error in making csv to predict ###')
        return False
