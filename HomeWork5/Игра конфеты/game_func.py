from param import start_users, user_step,ending_of_word
def play_game(candy, max_candy, players):
    count=start_users()
    while candy > 0:
        if count==0: 
            print(f'{players[0]} - ходите: ',end='')
            step_game = user_step(max_candy)
            count=1
        else:
            print(f'{players[1]} - ходите: ',end='')
            step_game = user_step(max_candy)
            count=0
        candy-=step_game
        if candy > 0: print(f'Осталось {candy} конфет'+ending_of_word(candy))
        else: print('Ирга окончена!')
    return players[not count]