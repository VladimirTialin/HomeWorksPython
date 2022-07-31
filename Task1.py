'''
41. Создайте программу для игры в "Крестики-нолики".

42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:

aaaabbcaa
Sample Output 1:

a4b2c1a2
Sample Input 2:

abc
Sample Output 2:

a1b1c1

'''
def func():
        UserMsg='Ошибка! Введите число от "0" или "X": '
        add=(input('Ходите: '))
        if add=='0' or add=='x' or add=='х':
            return add
        else:
            print(UserMsg,end='')
            return func()
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
def CoordinateSelection():
    a=int(input())
    b=int(input())
    return a,b
User1=NameUsers('Игрок 1')
User2=NameUsers('Игрок 2')
firstMove=StartUsers(User1,User2)
def func2(a,b):
    pole=['_', '_', '_' ], ['_', '_', '_' ], ['_', '_', '_' ]
    for i in range(0, len(pole)):
        for i2 in range(0, len(pole[i])):
            print(pole[i][i2], end=' ')

    if firstMove==User1:
        
