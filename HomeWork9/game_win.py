win=[(0,1,2),(3,4,5),(6,7,8),(0,0,0),(1,1,1),(2,2,2),(0,1,2),(2,1,0)]
def Winner(field): 
    for i in win:
        if (field[i[0]])==(field[i[1]])==(field[i[2]]):
            return field[i[0]]
    else: return False