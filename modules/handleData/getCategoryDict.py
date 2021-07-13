def getCategoryDict():
    f = open('./data/categoryDict.txt', 'r')

    d = {}
    while True:
        line = f.readline()
        if not line:
            break

        line = line.replace('\n', '')
        arr = line.split(',')
        if len(arr) != 2:
            continue

        d[arr[0]] = arr[1]

    f.close()

    return d
