from func_calc import Calc
def FuncPriority(list):
    temp=[]
    begin=list.index('(')
    end=list.index(')')
    for i in range(begin+1,end):
        temp.append(list[i])
    for i in range(end,begin-1,-1):
        list.pop(i)
    priority=Calc(temp)
    list.insert(begin,priority)
    if('(' in list): return FuncPriority(list)
    return list

def ResCalc(list): 
    if ('(' in list):
        list=FuncPriority(list)   
    result=Calc(list)
    if result==(int(result)):
        result=int(result)
    else: result
    return round(result,2)