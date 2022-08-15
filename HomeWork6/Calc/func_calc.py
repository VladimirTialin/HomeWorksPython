# умножение
def Multi(list): 
    for i in range(len(list)):
        if list[i] == '*':
            list[i+1]=float(list[i-1])*float(list[i+1])
            list.pop(i)
            list.pop(i-1)
            break
    if('*' in list): return Multi(list)
    return list

# деление
def Div(list):
    try:
        for i in range(len(list)):
            if list[i] == '/':
                list[i+1]=float(list[i-1])/float(list[i+1])
                list.pop(i)
                list.pop(i-1)
                break
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
        exit(0)
    if('/' in list): return Div(list)
    return list


# сложение
def Sum(list):
    for i in range(len(list)):
        if list[i] == '+':
            list[i+1]=float(list[i-1])+float(list[i+1])
            list.pop(i)
            list.pop(i-1)
            break
    if('+' in list): return Sum(list)
    return list

# вычитание
def Sub(list):
    for i in range(len(list)):
        if list[i] == '-':
            list[i+1]=float(list[i-1])-float(list[i+1])
            list.pop(i)
            list.pop(i-1)
            break
    if('-' in list): return Sub(list)
    return list

# вычисление значений
def Calc(list):
    while len(list)>1:
        list=Multi(list) 
        list=Div(list)
        list=Sum(list)
        list=Sub(list)
    return list[0]