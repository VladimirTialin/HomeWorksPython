# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.   
from work_to_file import ImportFile,ExportFile
from format_file import *
from sum_pol import SumDict
path1='C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork5/Polinomial_full/text1.txt'
path2='C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork5/Polinomial_full/text2.txt'
def LoadingPol():
    file1,file2=ImportFile(path1),ImportFile(path2)
    dict1=UserDict(FormatFile(file1))
    dict2=UserDict(FormatFile(file2))  
    sumPol=ResultOutput(SumDict(dict1,dict2))
    ExportFile(sumPol)
    return f'({file1}) + ({file2}) = {sumPol}'

