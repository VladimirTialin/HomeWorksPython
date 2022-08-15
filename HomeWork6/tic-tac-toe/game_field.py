field=list(range(1,10))
def DrawField():  
    line='-------------'
    print(line)
    for i in range(3):
        print( '|',field[0+i*3],'|',field[1+i*3],'|',field[2+i*3],'|')
    print(line)