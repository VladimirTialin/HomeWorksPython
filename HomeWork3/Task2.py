'''
Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
    список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
    список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
    список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
    список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
    список: [], ищем: "123", ответ: -1
    
    
    {"Список1": ["qwe", "asd", "zxc", "qwe", "ertqwe"], "Список2":
["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "Список3":
["йцу", "фыв", "ячс", "цук", "йцукен"], "Список4":
["123", "234", 123, "567"], "Список5": []}
'''
import json

def FindPositionStr(list):
    findWord=input(' ищем: ')
    try:
        for i in range(len(list)):
            if findWord==list[i]:
                result=i
                if result==0: result=-1
        return f'Ответ: слово "{findWord}" находится на позиции списка по индексом [{result}]\n'
    except:
        return f'Ответ: слово "{findWord}" находится на позиции списка по индексом [-1]\n'
UserLibrary={}
with open('C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork3/data.json', 'r', encoding='utf-8') as f:
    UserLibrary = json.load(f)

    for x,y in UserLibrary.items():
        print(x,y,end='')
        print(FindPositionStr(y))