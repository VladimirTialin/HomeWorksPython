#2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
from random import randint
def InputNumber():
    try:
        number=int(input('Введите число, для поиска его в списке: '))
        return number
    except:
        print('Ошибка ввода! Повторите ввод!\n')
        return InputNumber()
def RandomList():
    numbers = []
    for i in range(10):
        numbers.append(randint(-100, 100))
    print(numbers)
    return numbers
def FindNumber(list):
    number=InputNumber()
    for i in list:
        if i==number:
            return f'Искомое число {number} найдено в списке: List[{list.index(i)}] = {number}'     
    return f'Искомое число {number} не найдено!'
print(FindNumber(RandomList()))