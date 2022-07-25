'''
Вычислить результат деления двух чисел c заданной точностью d
    Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
from decimal import Decimal
def InputNumber():
    try:
        number=(input('Введите точность округления числа pi(например:0,001):'))
        if number.find(',')==True:
            number=number.replace(',','.')
        number=Decimal(number)
        return number
    except:
        print('Ошибка ввода! Попробуйте еще раз!\n')
        return InputNumber()
def Pi():
    x=1
    pi=0
    for i in range(10**6):
        if i%2==0:
            pi+=4/x
        else:
            pi-=4/x
        x+=2 
    return pi
def RoundPi(d):
    count=1
    if Decimal(10**(-10))<=d<=10**(-1):
        while d<1:
            d*=10
            count*=10        
    else:
        print('Ошибка! Такой точностью я не обладаю!!! Повторите ввод.')
        return RoundPi(InputNumber())
    return int(Pi()*count)/count
print(f'При заданной точности pi = {RoundPi(InputNumber())}')