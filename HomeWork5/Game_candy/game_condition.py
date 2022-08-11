from param import *
def game():
     print(intro)
     candy=number_of_candies('Введите количество конфет: ')
     maxStep=max_candies_step(candy)
     ending=EndingOfTheWord(candy)
     user1=name_users('Игрок 1')
     enemy=UserSetting()
     users=[user1,enemy]
     comment='Берите конфеты: '
     temp=start_users()
     while candy > 0:
          print(f'{users[temp%2]}, {comment}',end='')
          if users[temp%2]=='Гоша':
               step=EasyBot(maxStep)
               print(step)
          if users[temp%2]=='Петрович':
               step=MegaBot(candy,maxStep)
               print(step)          
          else:
               step = int(input())
          if step > candy or step > maxStep:
               print(f' Можно взять не более {maxStep} конфет{ending}, у нас всего {candy} конфет{ending}')
               if users[temp%2]=='Гоша':
                    step=EasyBot(maxStep)
                    print(step)
               if users[temp%2]=='Петрович':
                    step=MegaBot(candy,maxStep)
                    print(step)          
               else:
                    step = int(input())
          candy = candy - step
          if candy > 0: print(f'Осталось {candy} конфет{ending}')
          else: print('Конфет больше нет.')
          temp +=1
     return users[not temp%2]

        
        