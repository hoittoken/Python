import random
print('''1 - камень 
2 - ножницы; 
3 - бумага''')
while True:
    num = input('Сыграем? Твой ход (для выхода введи end)')
    if num == 'end':
        break
    else:
        rand = random.randint(1,3)
        if (int(num) == 1 and rand == 1) or (int(num) == 2 and rand == 2) or (int(num) == 3 and rand == 3):
            print('Ничья')
        elif int(num) == 1 and rand == 2:
            print('Ты проиграл')
        elif int(num) == 1 and rand == 3:
            print('Я проиграл')
        elif int(num) == 2 and rand == 1:
            print('Я проиграл')
        elif int(num) == 2 and rand == 3:
            print('Ты проиграл')
        elif int(num) == 3 and rand == 1:
            print('Я проиграл')
        elif int(num) == 3 and rand == 2:
            print('Ты проиграл')