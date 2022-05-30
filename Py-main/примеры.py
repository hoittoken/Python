#4.5
def power(val, n):
    if n==0: return 1
    if n==1: return val
    val*=power(val,n-1)
    return val
print(power(25,0))
print(power(-5,4))
#4.6
def is_leap(year):
    if year%400==0: return True
    elif year%100==0: return False
    elif year%4==0: return True
    else: return False
print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))
#4.7
def check_date(day, month, year):
    def is_leap(year):
        if year%400==0: return True
        elif year%100==0: return False
        elif year%4==0: return True
        else: return False
    if type(day)!=int or type(month)!=int or type(year)!=int or year < 1900 or year > 2022 or month < 1 or month > 12 or day < 1 or day > 31: return False
    elif (month==4 and day==31) or (month==6 and day==31) or (month==9 and day==31) or (month==11 and day==31): return False
    elif is_leap(year)==False and month == 2 and day>28: return False
    elif is_leap(year)==True and month == 2 and day>29: return False
    else: return True
print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))
#Генераторы
def mygen():
    i=7
    print('hello')
    while i>0:
        i-=1
        yield i
gen = mygen()
for i in gen:
    print(i, end='fff')
print()
#map()
main_link = 'https://www.kommersant.ru'
docs = ['//doc/5041434?query=data%20science',
    '//doc/5041567?query=data%20science',
    '//doc/4283670?query=data%20science',
    '//doc/3712659?query=data%20science',
    '//doc/4997267?query=data%20science',
    '//doc/4372673?query=data%20science',
    '//doc/3779060?query=data%20science',
    '//doc/3495410?query=data%20science',
    '//doc/4308832?query=data%20science',
    '//doc/4079881?query=data%20science']
links=list(map(lambda x:main_link+x,docs))
print(links)
#filter
nums=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%3==0,nums)))
print()
def family(*args):
    family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"]
    #ваш код здесь. используйте функцию filter()
    return list(filter(lambda x: x in family_list,args))

#вызов функции
print(family(
    'newborn registration',
    'parking permit',
    'maternity capital',
    'tax benefit',
    'medical policy'
    ))
#6.3
reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]

filtred=list(filter(lambda x: x[4]>2000, reg))
def rep(line):
    return (line[0]+' '+line[1][:1:]+'.',line[2],line[3],line[4])
print(list(map(rep,filtred)))
#Decorations
def simple_decorator(func):
    def decorated_function(*args, **kwargs):
        print("Positional:", args)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return decorated_function
@simple_decorator
def root(val, n=2):
    res = val ** (1/n)
    return res
print(root(25))
#7.3
def logger(name):
    def decorated_func(func):  
        print(name+': Function '+func.__name__+' started')
        result=func
        print(name+': Function '+func.__name__+' finished')
        return result
    return decorated_func
@logger('MainLogger')
def root(val, n=2):
    res = val ** (1/n)
    return res 
print(root(25))
#2.5
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
def get_unique_words(text):
    text=text.lower()
    for i in text:
        if i in punctuation_list:
            text=text.replace(i,'')
    text_set=set(text.split())
    text_clean=list(text_set)
    text_clean.sort()
    return text_clean

print(get_unique_words(text_example))
#2.6
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    text=text.lower()
    for i in text:
        if i in punctuation_list:
            text=text.replace(i,'')
    text=text.split()
#блок подсчета
    c=0
    c_max=0
    for y in text:
        c=text.count(y)
        if c>c_max:
            c_max=c
            max_y=y
    return (max_y,c_max)

print(get_most_frequent_word(text_example))
#2.7
def holes_count(number):
    holes={'0':1,'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1}
    counter=0
    for i in str(number):   
        counter+=holes[i]
    return(counter)
print(holes_count(123))
print(holes_count(8888))
#запрашивает у пользователя следующие данные : username, age, email о нескольких пользователях и собирает эти данные в структуру:
#[(1, {'username': user1, 'age': age1, 'email': email1}), (2, {'username': user2, 'age': age2, 'email': email2}), ... ]
#Первый элемент каждого кортежа — порядковый номер пользователя, второй элемент — словарь с данными.
#В итоге должен получиться список с кортежами.
#Далее необходимо провести аналитику (собрать данные о пользователях в словарь)
#{'username': [user1, user2, ...],
#'age': [age1, age2, ...],
#'email': [email1, email2, ...]}
num=0
func_list=list()
users=list()
ages=list()
emails=list()
def check(username, age, email):
    global num
    num+=1
    func_dict=dict({'username':username,'age':age,'email':email})
    global func_list
    local_tpl=(num,func_dict)    
    func_list.append(local_tpl)
    return func_list

check('Mike', 33, 'mike@gmail.com')
check('Alina', 28, 'alina@gmail.com')
check('Alla', 4, 'alla@gmail.com')

for i in func_list:
    users.extend([i[1]['username']])
    ages.extend([i[1]['age']])
    emails.extend([i[1]['email']])
new_dict={'username':users,'age':ages,'email':emails}
print(new_dict)
#4.4
def lucky_ticket(ticket_number):
    a=str(ticket_number)[0]+str(ticket_number)[1]+str(ticket_number)[2]
    b=str(ticket_number)[3]+str(ticket_number)[4]+str(ticket_number)[5]
    return True if a==b else False
print(lucky_ticket(111111))
print(lucky_ticket(123456))
#4.5
def fib_number(n):
    a=1
    b=1
    for i in range(1,n):
        a,b=b,a+b
    return b

print(fib_number(0))
print(fib_number(1))
print(fib_number(2))
#4.6
# Напишите функцию def even_numbers_in_matrix(), 
# которая получает на вход матрицу (список из списков) 
# и возвращает количество четных чисел в ней.

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]

def even_numbers_in_matrix(matrix):
    even_count=0
    for row in matrix:
        for num in row:
            if num%2==0: even_count+=1
    return even_count
print(even_numbers_in_matrix(matrix_example))
#4.7
matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]
def matrix_sum(matrix1, matrix2):
    if len(matrix1)!=len(matrix2):
        print('Error! Matrices dimensions are different!')
        return None
    for num in range(len(matrix1)):
        if len(matrix1[num])!=len(matrix2[num]):
            print('Error! Matrices dimensions are different!')
            return None
    matrix_sum=[]
    for i in range(len(matrix1)):
        line_tmp=[]
        for y in range(len(matrix1[i])):
            line_tmp.append((matrix1[i][y]+matrix2[i][y]))
        matrix_sum.append(line_tmp)        
    return matrix_sum
print(matrix_sum(matrix_example, matrix_example))
#4.8
str_example = 'aaabbccccdaa'
first_symbol = str_example[0]
count = 0
new_str = ''
for symbol in str_example:
    if symbol == first_symbol:
        count += 1
    else:
        new_str += first_symbol + str(count)
        first_symbol = symbol
        count = 1

new_str += first_symbol + str(count)
print(new_str)
#5.4
def distance_between_dots(x1,x2,y1,y2):
    try:
        coord=[x1,x2,y1,y2]
        for c in coord:
            if type(c)!=int and type(c)!=float:
                raise ValueError
    except ValueError:
        print('Argumets are not numbers!')
        return
    return((x2-x1)**2+(y2-y1)**2)**(1/2)
print(distance_between_dots(2,5,2,6))
#5.5
def get_mean(*args):
    try:
        for x in args:
            if type(x)!=int and type(x)!=float:
                raise ValueError
    except ValueError:
        print('Argumets are not numbers!')
        return
    n=0
    summ=0
    for arg in args:
        summ+=arg
        n+=1
    return summ/n
print(get_mean(20,10,0,101))
#5.6
mean=lambda *args:sum(args)/len(args)
print (mean(20,10,200,101))
#5.7
#декоратор проверяющий пользователя
users_list = ["admin", "ivan", "ivan_ivan"]
def user_auth(func):
    def wrapper():
        user = input("Enter username: ")
        if user in users_list:
            print("User authed")
            func()
        else:
            print("Unknown user!")
    return wrapper
@user_auth
def get_data_from_database():
    print("Super secure data from database")
get_data_from_database()
