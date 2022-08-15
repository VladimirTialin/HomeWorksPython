from IO import *
from func_priority import ResCalc
print(intro)
def PrintExp(count=3):
    try:
        exp=UserExp()
        if len(exp)==1: return f'{exp} = {exp}'
        else:
            list=exp.split()
            if list[0]=='-':
                list[1]=float(list[1])*(-1)
                list.pop(0)
        return f'{exp} = {ResCalc(list)}'
    except ValueError or TypeError:
        if count==0: return 'Д О   С В И Д А Н И Я !' 
        else:
            print(f'\033[31mОшибка:\n1. Вы попытались ввести текст!\n2. Неверно ввели выражение!\nПопробейте еще раз!\033[0m\n\033[32mОсталось попыток: {count}\033[0m')
            return PrintExp(count-1)