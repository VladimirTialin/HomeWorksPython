list=[1,3,0,1,2,36,6,5,4,3]
def find_of_sequence(list):
    list=sorted(set(list))
    result=[]
    min_num=list[0]
    for i in range(len(list)-1):
        if list[i+1]-list[i]!=1:
            result=[min(list),list[i]]
            break
        else:result=[min(list),max(list)]
    return result

print(f'{list} => {find_of_sequence(list)}')
