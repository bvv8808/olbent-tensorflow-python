import os
print(os.getcwd())

def getItemList():
    itemList = []
    f = open('./data/allOfItem.txt' , 'r')
    while True:
        line = f.readline()
        if not line:
            break

        itemList.append(line.replace('\n', ''))

    f.close()

    return itemList

getItemList()