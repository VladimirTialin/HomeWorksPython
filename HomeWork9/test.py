from random import randint
move='XO'
playerSymbol = move[randint(0, 1)]
botSymbol = ""
if (playerSymbol == "O"):
    botSymbol = "X"
else:
    botSymbol = "O"
print(botSymbol)