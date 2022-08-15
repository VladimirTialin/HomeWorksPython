from game_field import *
import game_win as gw
import get_user as gu
from bot import *
def game():
    name1=gu.UserName()
    num=int(input('Режим игры:\n1. Против другого игрока\n2. Против бота - Игоря!'))
    match num:
        case 1: name2=gu.UserName()
        case 2: name2='Игорь'
    
    print(f'Битва началась! {name1} vs {name2}')
    count=0
    while True:
        DrawField()
        if count%2==0:
           gu.GetFromUser(name1,'X')
        else:
            if name2=='Игорь': step_bot()
            else: gu.GetFromUser(name2,'O')
        if count>3:
            win=gw.Winner(field)
            if win:
                DrawField()
                if win=='X':
                    print(f'Битва окончена: {name1} - победил!')
                else: print(f'Битва окончена: {name2} - победил!')
                break
        count+=1
        if count>7:
            DrawField()
            print('Ничья!')
            break