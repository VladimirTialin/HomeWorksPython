def FormatText(text):
    import re
    resultStr=re.sub(r'[^\w\s]','',text)
    resultStr=resultStr.lower()
    tempStr=resultStr.split()
    return tempStr
def Counter(list):
    library={}
    for i in list:
        if library.get(i,None):
            library[i]+=1
        else:
            library[i]=1
        result=library.items()
    return dict(result)
path='C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork3/UserText.txt'
file=open(path,encoding="utf-8")
text=file.read()
for x,y in Counter(FormatText(text)).items():
    print(f'{x}: ',y)
file.close()