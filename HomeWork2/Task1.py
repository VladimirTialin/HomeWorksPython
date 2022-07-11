'''
 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
*Пример:*
- 6782 -> 23
- 0,56 -> 11
'''

def RealNumber():
    try:
        number=input('Введите число: ')
        if float(number)==True:
            return float(number)
        else:
            number=number.replace('.','')
            return float(number)
    except:
        print('Ошибка! Введите вещественное число, в качестве разделителя используйте ".": ')
        return RealNumber()
def SumElements(number):
    result = 0
    while number > 0:
        result = result +number% 10
        number = number // 10
    return result
inputNumber=RealNumber()
print(f'Сумма элементов вещественных числе = {round(SumElements(inputNumber))}')