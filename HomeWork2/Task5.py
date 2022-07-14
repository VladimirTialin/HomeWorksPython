list=[1,7,9,0]
def DelMaxEl(list,max):
    return list.remove(max)
def FindMax(list):
    max=list[0]
    for i in list:
        if max<i:max=i
    return max
DelMaxEl(list,FindMax(list))
print(FindMax(list))