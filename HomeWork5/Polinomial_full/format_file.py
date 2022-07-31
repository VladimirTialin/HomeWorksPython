# Форматируем многочлен для удобства работы
def FormatFile(file):
    file=file.replace(' ','')
    count=0
    oneX=0
    for i in range(len(file)):
        if file[i]=='*': count+=1
        if file[i]=='x' and file[i-1]=='+' :oneX+=1
        if file[i]=='x' and file[i-1]==int(file[i-1]):
            file[i].replace('x','*x^1')
        else:break
    if oneX!=0 or file[0]=='x':
        file=file.replace('+x','+1*x^1')
    if count==0: file=file.replace('x','*x')
    return file.replace('+',' ')\
             .replace('*',' ')\
             .replace('x^','x^ ')\
             .replace('-',' -').split()
# Создаем словарь с ключами и значениями переменных
def UserDict(temp):
    usDict={}
    for i in range(len(temp)):
        if temp[i]=='x^':
            key=int(temp[i+1])
            usDict[key]=int(temp[i-1])
        elif temp[i]=='x':
            usDict[1]=int(temp[i-1])
        else:
            usDict[0]=int(temp[i])
    return usDict
def ResultOutput(dict):
    result = ''
    sign=' + '
    for key, value in dict.items():
        if value<0:
            sign=' - ' 
            value*=(-1)
        if key>1: result += str(value)+sign+'x^'+str(key)+sign
        else:
            match key:
                case 1: result +=  str(value)+'x'
                case 0: result += sign+str(value)
    return result  