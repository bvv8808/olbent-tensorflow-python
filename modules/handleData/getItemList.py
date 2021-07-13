

def getItemList():
    itemList = []
    f = open('./data/allOfItem.txt' , 'r')
    while True:
        line = f.readline()
        if not line:
            break
        if line.count('id,category,')==1:
            continue

        # print(line)
        l = line.replace('\n', '')
        arr = l.split(',')
        # # id, category, price
        itemList.append((arr[0], float(arr[1]), arr[2]))

    f.close()

    return itemList
