def DecodeRLE(text):
    count = ''
    result = ''
    for i in text:
        if i.isdigit():
            count += i 
        else:
            result += i * int(count)
            count = ''
    return result 

def EncodeRLE(text):
    result = ''
    temp = ''
    count = 1
    for i in text:
        if i != temp:
            if temp:
                result += str(count) + temp
            count = 1
            temp = i
        else:
            count += 1
    return result

def UserReadFile(file):
 with open(file, 'r') as data:
    return data.read()