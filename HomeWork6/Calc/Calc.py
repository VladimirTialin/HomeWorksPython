'''
41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
*Пример:* 
2+2 => 4; 
1+2*3 => 7; 
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
 *Пример:* 
1+2*3 => 7; 
(1+2)*3 => 9;
'''
import re
def OperationPriority(text):
    if text[0]=='(' or text.find("(")==(-1): return text
    else:
        for i in range(len(text)):
            if text[i]=='(':
                symbol=text[i-1]
                temp=text[0:(i-1)]
                text=text[i:len(text)]
                return text+symbol+temp
def FormatText(text):
    text=re.sub("[-|+|*|/|(|)|a-z|а-я]",' ',text)
    return [int(i) for i in text.split()]
def FormatText1(text):
    text=re.sub("[0-9]",' ',text)
    return [i for i in text.split()]

def Calc(text,list):
    try:
        result=list[0]
        text=re.sub("[0-9]",'',text)
        for i in range(len(text)):
            match text[i]:
                case '+':
                    result+=list[i+1]
                case '-':
                    result-=list[i+1]
                case '*':
                    result*=list[i+1]
                case '/':
                    if result==0:
                        result='Делить на ноль невозможно!'
                    else:
                        result/=list[i+1]
        return result
    except:
        return 'Ошибка ввода выражения!'

print('К А Л Ь К У Л Я Т О Р\n') 
text=input('Введите выражение: ')
print(text)
text=text.replace(' ','')
n=FormatText(text)
z=FormatText1(text)

for i in range(len(z)):
    if z[i]=='*':
        result=n[i]
        result*=n[i+1]
for i in range(len(z)):
        
    if z[i]=='/':
        result=n[i]
        result/=n[i+1]
for i in range(len(z)):   
            
    if z[i]=='+':
        result=n[i]
        result+=n[i+1]
for i in range(len(z)): 
              
    if z[i]=='-':
        result=n[i]
        result-=n[i+1]    

print(result)
    
#textPriority=OperationPriority(text)
#print(f'{text}={Calc(textPriority,FormatText(textPriority))}')