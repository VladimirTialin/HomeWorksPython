win=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
def Winner(field): 
    for i in win:
        if (field[i[0]-1])==(field[i[1]-1])==(field[i[2]-1]):
            return field[i[1]-1]
    else: return False