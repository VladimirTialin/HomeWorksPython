from game_condition import *

result=game()
if not result:
    print('Ничья.')
else: print(f'Игра окончена! Победил {result}! Он забирает все конфеты!')