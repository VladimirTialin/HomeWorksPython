'''
43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
list=[1, 2, 3, 5, 1, 5, 3, 10]
def UniqueNumbers(list):
    unique = []
    for i in range(len(list)):
        if list[i] not in list[i+1::] and list[i] not in list[:i-1:]:
            unique.append(list[i])
    return unique
print(UniqueNumbers(list))