from func_rle import *
file1=UserReadFile('C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork6/RLE/decode.txt')
file2=UserReadFile('C:/Users/Владимир/Desktop/Python/HomeWorks/HomeWork6/RLE/encode.txt')
line='---------------------------'
encode='|       КОДИРОВАНИЕ       |'
decode='|      ДЕКОДИРОВАНИЕ      |'
print(f'{line}\n{encode}\n{line}')
print(f'Файл закодирован: {EncodeRLE(file2)}')
print(f'{line}\n{decode}\n{line}')
print(f'Файл раскодирован: {DecodeRLE(file1)}')
