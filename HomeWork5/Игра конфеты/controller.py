from IO import info
from param import*
from game_func import play_game
def game():
    print(info)
    players=[name_users('Игрок 1'),name_users('Игрок 2')]
    n= int(input('Сколько конфет будем разыгрывать?\n '))
    m= int(input('Сколько максимально будем брать конфет за один ход?\n '))
    users_game=(play_game(n,m,players))
    if not users_game: return 'Победила дружба!'
    else: return f'Победил {users_game}! Ему достаются все конфеты!'