import itertools
def CountGame():  
    try: 
        n = int(input('Количесвтво игр: '))
        if n>0:
            return n
        else:
            return CountGame()
    except:
        print('Ошибка ввода! Повторите еще раз!')
        return CountGame()
def StatGame(list):
    vs= [(x[0], x[2]) for x in list]
    result = set(itertools.chain.from_iterable(vs))
    statGame = {club: [0, 0, 0, 0, 0] for club in result}
    for team1, goolTeam1, team2, goolTeam2 in list:
        statGame[team1][0] += 1
        statGame[team2][0] += 1
        if int(goolTeam1) > int(goolTeam2):
            statGame[team1][1] += 1
            statGame[team1][4] += 3
            statGame[team2][3] += 1
        elif int(goolTeam1) < int(goolTeam2):
            statGame[team2][1] += 1
            statGame[team2][4] += 3
            statGame[team1][3] += 1
        elif int(goolTeam1) == int(goolTeam2):
            statGame[team1][2] += 1
            statGame[team1][4] += 1
            statGame[team2][2] += 1
            statGame[team2][4] += 1 
    [print('{}:    {}'.format(res, ' '.join(map(str, statGame[res])))) for res in result]
n=CountGame()   
print('Формат ввода.Команда 1;кол-во голов;Команда 2; кол-во голов:')
try:
    list = [input().split(';') for x in range(n)]
    (StatGame(list))
except:
    print('Неверный формат ввода данных. Повторите ввод!')