from game_win import win
from game_field import field

def find_line(sumCross,sumZero):
    step = ""
    for line in win:
        o = 0
        x = 0
        for i in range(3):
            if field[line[i]-1] == "O":
                o = o + 1
            if field[line[i]]-1 == "X":
                x = x + 1
        if o == sumZero and x == sumCross:
            for i in range(3):
                if field[line[i]-1] != "O" and field[line[i]-1] != "X":
                    step = field[line[i]-1]              
    return step

def step_bot():        
    step = ""
    step = find_line(2,0)
    if step == "":
        step = find_line(0,2)
    if step == "":
        step = find_line(1,0)
    if step == "":
        if field[4] != "X" and field[4] != "O":
            step = 5
    if step == "":
        if field[0] != "X" and field[0] != "O":
            step = 1           
    return step
