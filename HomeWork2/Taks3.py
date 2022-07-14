number=int(input('Введите любое чило:'))
def FilList(number):
    for i in range (1, number+1):
        list=[(1+1/i)**i]
        print(f'{i}:{list}', end='')
        if i<number: print(', ',end='')
FilList(number)