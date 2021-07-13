def hexToDec(origin: str):
    # 최댓값: 69904
    originLen = len(origin)

    result = 0
    for i in range(0, originLen):
        cur = origin[originLen - i - 1]
        curDec = 0
        curAscii = ord(cur)
        if curAscii >= 97 and curAscii <= 102:
            curDec  = curAscii - 86
        elif curAscii >= 48 and curAscii <= 57:
            curDec = curAscii - 48
        
        result += curDec * pow(16, i)
        
    return result
