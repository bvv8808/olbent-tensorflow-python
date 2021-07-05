def filterPrediction(mode: str, predictResult):
    filtered = []
    if mode == 'item': # 각 아이템마다 상위 10개씩만 취함
        sortedResult = sorted(predictResult, key=lambda p: (p['item'], -p['action']))
        cnt = 0
        curSection = predictResult[0]['item']
        for p in sortedResult:
            section = p['item']
            if section==curSection and cnt==10:
                continue
            elif section==curSection:
                cnt += 1
                filtered.append(p)
            elif section!=curSection:
                curSection = section
                cnt = 1
                filtered.append(p)
        
    elif mode == 'user': # 각 연령+성별마다 상위 10개씩만 취함
        sortedResult = sorted(predictResult, key=lambda p: (p['age'], p['gender'], -p['action']))
        cnt = 0
        curSection = predictResult[0]['item']
        for p in sortedResult:
            section = p['item']
            if section==curSection and cnt==10:
                continue
            elif section==curSection:
                cnt += 1
                filtered.append(p)
            elif section!=curSection:
                curSection = section
                cnt = 1
                filtered.append(p)
    
    else: # 확률이 0.2 이하인 결과들 제외
        for p in predictResult:
            if p['action'] > 0.2:
                filtered.append(p)

    return filtered