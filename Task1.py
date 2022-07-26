import re
text1='3*x^3+5*x^2+10*x+11'
text2='7*x^2+55'
def FormatText(text):
    text=re.sub("[ |*|^|x|+]","",text)
    return text         
print(FormatText(text1))
#