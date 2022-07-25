#Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
def InputNumber():
    try:
        number=int(input('Введите число: '))
        if number>1: return number
        elif number==1:
            print(f'{number} - не является ни простым, ни составным числом!\n')
            return InputNumber()
        elif number<=0:
            print('Число должно быть больше 0.\n')
            return InputNumber()      
    except:
        print('Ошибка ввода! Повторите ввод.\n')
        return InputNumber()
def Factorize(number):
    ratio=2
    resultList=[]
    while number>1:
        if number%ratio==0:
            resultList.append(int(ratio))
            number/=ratio
        else: ratio+=1
    return resultList
def PrintMn(list):
    resultStr=''
    for i in range(len(list)):
        resultStr+=str(list[i])
        if i!=len(list)-1:
            resultStr+="·"
    return resultStr
number=InputNumber()
print(f'Я разложил ваше число на множители: {number} = {PrintMn(Factorize(number))}')
