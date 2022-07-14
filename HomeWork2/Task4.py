import time
def UserRandom():
    milSecond = int(round(time.time() * 10000))
    newRandom=str(milSecond)
    result=int(newRandom[10:-1])//10
    return result
print(f'Случайное число [ {UserRandom()} ]')