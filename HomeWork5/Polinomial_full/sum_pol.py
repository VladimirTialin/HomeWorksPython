def SumDict(dict1, dict2):
    resDict = {}
    for i in range(len(dict1)+len(dict2)):
        if i in dict1.keys() and i not in dict2.keys():
            resDict[i]=dict1[i]
        elif i in dict2.keys() and i not in dict1.keys():
            resDict[i]=dict2[i]
    for key, value in dict1.items():
                dict2[key] = dict2.get(key, 0) + value
    resDict.update(dict2)
    return dict(reversed(sorted(resDict.items(), key=lambda x:x[0])))