# Форматируем многочлен для удобства работы
def FormatFile(file):
    import re
    file=re.sub("[ |*]",'',file)
    print(file)
    return file.replace('+x','+1 x').replace('-x','-1 x').replace('^','^ ').replace('-',' -').replace('x',' x').replace('+',' ').split()

def UserDict(temp):
    usDict={}
    for i in range(len(temp)):
        if temp[i]=='x^': 
            key=int(temp[i+1])
            if temp[0]=='x^': usDict[key]=1
            else:usDict[key]=int(temp[i-1])
        elif temp[i]=='x': usDict[1]=int(temp[i-1])
        else: usDict[0]=int(temp[i])
    return usDict

def ResultOutput(dict):
    result = ''
    sign=' + '
    for key, value in dict.items():
        if value<0:
            sign=' - ' 
            value*=(-1)
        if value==1 or value==0: value=''   
        if key>1:
            result += str(value)+'*x^'+str(key)+sign
        else:
            match key:
                case 1: result +=  str(value)+'*x'
                case 0: result += sign+str(value)
    return result  