from game_field import *
def GetFromUser(player,symbol):
    numbers='123456789'
    move='XO'    
    while True:
        getSymbol=input(f'{player}. Ваш ход: {symbol}? ')
        if not (getSymbol in numbers) or 1<int(getSymbol)>9:
            print('Ошибка! Повторите ввод!')
            continue
        getSymbol=int(getSymbol)
        if str(field[getSymbol-1]) in move:
            print('Клетка занята! Выберите другую клетку.')
            continue
        field[getSymbol-1] = symbol
        break
def UserName():
    return input('Введите имя игрока: ')
     