
def start_users():
    import random
    check=(random.randint(0,2))
    if check==1:
        return 0
    else:
        return 1
     
def user_step(num):
        step_game = input()
        if not step_game.isdigit():
            print('Ошибка! Вы ввели текст, а нужно число: ',end='')
            return user_step(num)       
        elif int(step_game) > num and int(step_game) < 1:
            print(f'Вы можете взять не более {num} конфет{ending_of_word(num)} за ход: ',end='')
            return user_step(num) 
        elif  int(step_game)< 1:
            print('Не подкладывайте свои конфеты: ',end='')
            return user_step(num)
        elif int(step_game)<num:
            return int(step_game)
        
def name_users(userNum=''):
    User=input(userNum+'. Введите свое имя: ')
    return User

def ending_of_word(step):
    if step % 10 == 1 and 9 > step > 10: return 'а'
    elif 1 < step % 10 < 5 and 9 > step > 10: return 'ы'
    else: return '' 
    

