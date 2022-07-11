'''
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

*Пример:*

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
def InputKoordinate():
    try:
        number=input()
        if int(number)!=0:
            return int(number)
    except:
        print('Ошибка ввода! Введено не целочисленное значение! Повторите ввод: ',end='')
        return InputKoordinate()   
def QuarterHardness(x,y):  
    if x>0 and y>0: result='1 четверть'
    if x<0 and y>0: result='2 четверть'
    if x<0 and y<0: result='3 четверть'
    if x>0 and y<0: result='4 четверть'
    return result
print('Введите x =', end=' ')
x=InputKoordinate()
print('Введите y =', end=' ')
y=InputKoordinate()  
print(f'x = {x}; y = {y} - > {QuarterHardness(x,y)}')


    