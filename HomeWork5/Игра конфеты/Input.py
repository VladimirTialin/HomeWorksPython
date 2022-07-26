from random import random


def InputNum():
    try:
        UserMsg='Ошибка! Введите число от 1 до 28: '
        number=int(input())
        if 0<number<29:
            return number
        else:
            print(UserMsg,end='')
            return InputNum()
    except:
        print(UserMsg,end='')
        return InputNum()
def StartUsers(x,y):
    import random
    check=(random.randint(0,2))
    if check==1:
        return x
    else:
        return y
def NameUsers(userNum=''):
    User=input(userNum+'. Введите свое имя: ')
    return User
    
    

