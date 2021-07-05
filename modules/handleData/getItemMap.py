from .getItemList import *

def getItemMap(itemList=getItemList()):
    def convert(value, d):
        if value in d:
            return d[value]
        else:
            curKeyLength = len(d.keys())
            d[value] = curKeyLength
            return curKeyLength
            

    def mapping(origin):
        d = {}

        for value in origin:
            convert(value, d)
        
        return d

        
    

    itemMap = mapping(itemList)
    return itemMap
