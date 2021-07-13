def filterPrediction(mode: str, predictResult):
    filtered = []
    print(mode)
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
        
        
    elif mode=='top': # 확률이 0.2 이하인 결과들 제외
        for p in predictResult:
            if p['action'] > 0.2:
                filtered.append(p)

    else: # 각 연령+성별마다 상위 10개씩만 취함
        sortedResult = sorted(predictResult, key=lambda p: (p['age'], p['gender'], -p['action']))
        # print(sortedResult[:100])
        cnt = 0
        curSection = '{age}/{gender}'.format(age=predictResult[0]['age'], gender=predictResult[0]['gender'])
        for p in sortedResult:
            section = '{age}/{gender}'.format(age=p['age'], gender=p['gender'])
            if section==curSection and cnt==10:
                continue
            elif section==curSection:
                cnt += 1
                filtered.append(p)
            elif section!=curSection:
                curSection = section
                cnt = 1
                filtered.append(p)

    return filtered