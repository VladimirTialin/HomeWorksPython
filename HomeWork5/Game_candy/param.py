from random import randint

def number_of_candies(comment):
    try:
        n=int(input(comment))
        if n<1:
            print('Ошибка! Конфет не может быть меньше 1.')
            return number_of_candies(comment)
        else: return n
    except:
        if TypeError:
            print('Ошибка!Повторите ввод.')
            return number_of_candies(comment)
def max_candies_step(candy):
    try:
        n=int(input('Максимальное количество конфет за ход: '))
        if n<1 or n>(candy-1):
            print(f'Ошибка! Конфет не может быть меньше 1 или больше {candy}.')
            return max_candies_step(candy)   
        else: return n
    except:
        if TypeError:
            print('Ошибка!Повторите ввод.')
            return max_candies_step(candy)
        
def start_users():
    check=(randint(0,2))
    if check==1:
        return 0
    else:
        return 1

def name_users(userNum=''):
    User=input(userNum+'. Введите свое имя: ')
    return User
    
def EndingOfTheWord(candy):
    if candy%10 == 1 and 9 > candy > 10: ending = 'а'
    elif 1 < candy%10 < 5 and 9 > candy > 10: ending = 'ы'
    else: ending = ''
    return ending

intro=f'ИГРА С КОНФЕТАМИ.\
     \nНа столе лежит n - конфет. Играют два игрока делая ход друг после друга.\
     \nЗа один ход можно забрать не более чем k-конфет.\
     \nВсе конфеты оппонента достаются сделавшему последний ход.'

def EasyBot(maxStep):
    return (randint(1,maxStep))

def MegaBot(candy,maxStep):
    return candy % maxStep + 1

def UserSetting():
    try:
        newGame=int(input('Режим игры?\n1. Против игрока\n2. Против бота\n3. Против умного бота\n'))
        match newGame:
            case 1: return name_users('Игрок 2')
            case 2: return 'Гоша'
            case 3: return 'Петрович'
    except:
        print('Ошибка!Повторите ввод!')
        return UserSetting()
    