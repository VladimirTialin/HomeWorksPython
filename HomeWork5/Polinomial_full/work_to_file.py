def ImportFile(name):
    try:
        with open(name, 'r') as file:
            return file.read()
    except:
        print('Ошибка чтения файла! Файл не найден!')
def ExportFile(result):
    with open('C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork5/Polinomial_full/sumPolinomial.txt', 'w+') as file:
     return file.write(result)