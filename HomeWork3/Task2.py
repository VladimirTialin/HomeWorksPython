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
UserLibrary={}
with open('data.json', 'r', encoding='utf-8') as f:
    UserLibrary=json.load(f)
for x,y in UserLibrary.items():
    print(x,FindPositionStr(y))