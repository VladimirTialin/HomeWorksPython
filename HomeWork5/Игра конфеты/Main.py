from tabnanny import check
from Input import *
print('ИГРА С КОНФЕТАМИ.\nНа столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\nЗа один ход можно забрать не более чем 28 конфет.\nПроигрывает тот, кому все конфеты оппонента достаются сделавшему последний ход.')
User1=NameUsers('Игрок 1')
User2=NameUsers('Игрок 2')
firstMove=StartUsers(User1,User2)
print(f'Первый ход делает {firstMove}!\nСколько конфет хотите взять?')
temp=moveUser1=moveUser2=candiesUser1=candiesUser2=0
while candiesUser1+candiesUser2<10:
        if firstMove==User1:
            print(User1+'! Ваш ход: ',end='')
            user1Check=InputNum()
            temp+=user1Check
            moveUser1+=1
            candiesUser1+=user1Check
            firstMove=User2
            print(f'{User1} ходов: {moveUser1} конфет {candiesUser1}')
        elif firstMove==User2:
            print(User2+'! Ваш ход: ',end='')
            user2Check=InputNum()
            temp+=user2Check
            moveUser2+=1
            candiesUser2+=user2Check
            firstMove=User1
            print(f'{User2} ходов: {moveUser2} конфет {candiesUser2}')          
        if 10<=temp+candiesUser1:
                lost=candiesUser1+candiesUser2
                move=moveUser2
                Win=User2
                lostUser=User1    
        else:
                lost=candiesUser1+candiesUser2
                Win=User1
                move=moveUser1
                lostUser=User2  
print(f'{Win} - Вы победили за {move} ходов!')
print(f'{lostUser} - Вы проиграли, у Вас {lost} конфет!')


    