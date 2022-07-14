'''
Дополнительно:
Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек отбрасывается.
Требуется определить: через сколько лет вклад составит не менее Y рублей.
Пример:
100
10
200
Вывод:
8
'''
x=100
p=10
y=200
def AnnualInterest(money,bid):
    income=((money*bid*365)/365)/100
    money+=income
    return money
def CashX2(money,bid):
    Cash=AnnualInterest(money,bid)
    count=0
    while Cash<=Cash*2:
        count+=1
    return count

print(CashX2(x,p))