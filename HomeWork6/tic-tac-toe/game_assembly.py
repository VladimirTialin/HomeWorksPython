from game_field import *
import game_win as gw
import get_user as gu
def game():
    name1=gu.UserName()
    name2=gu.UserName()
    print(f'Битва началась! {name1} vs {name2}')
    count=0
    while True:
        DrawField()
        if count%2==0:
           gu.GetFromUser(name1,'X')
        else:
            gu.GetFromUser(name2,'O')
        if count>3:
            win=gw.Winner(field)
            if win:
                print('Вы победили!')
                break
        count+=1
        if count>7:
            DrawField()
            print('Ничья!')
            break