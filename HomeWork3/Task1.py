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

'''
Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
    список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
    список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
    список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
    список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
    список: [], ищем: "123", ответ: -1
'''
import json
def FindPositionStr(list):
    findWord=input('Введите искомое слово: ')
    try:
        for i in range(len(list)):
            if findWord==list[i]:
                result=i
                if result==0: result=-1
        return f': {list}, ищем {findWord}, ответ: {result}'
    except:
        return f': {list}, ищем {findWord}, ответ: -1'
def PrintLibrary(): 
    UserLibrary={}
    with open('data.json') as text:
        UserLibrary=json.load(text)
    for x,y in UserLibrary.items():
        return x,FindPositionStr(y)
print(PrintLibrary())
{"Список1": ["qwe", "asd", "zxc", "qwe", "ertqwe"], "Список2":
["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "Список3":
["йцу", "фыв", "ячс", "цук", "йцукен"], "Список4":
["123", "234", 123, "567"], "Список5": []}