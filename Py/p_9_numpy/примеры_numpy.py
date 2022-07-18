def brackets(line):
    from collections import deque
    open = deque()
    for bracket in line:
        if bracket == "(":
            open.append(bracket)
        try:
            if bracket == ")":
                open.pop()
        except IndexError:
            return False
    if not open:
        return True


def brackets_2(line):
    from collections import deque
    open = deque()
    for bracket in line:
        open.append(bracket)
    if open.count('(') == open.count(')'):
        return True
    else: return False
  
 

print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False """

""" from hidden import north, center, south
from collections import deque
from collections import Counter

d_north = deque()
d_center = deque()
d_south = deque()

for i in north:
    for j in i:
        d_north.append(j)
for i in center:
    for j in i:
        d_center.append(j)
for i in south:
    for j in i:
        d_south.append(j)

c_north = Counter(d_north)
c_center = Counter(d_center)
c_south = Counter(d_south)

nc = c_north+c_center
cs = c_center+c_south
sn = c_south+c_north

all = c_north+c_center+c_south """

#4.9 Создаём отсортированный список кафе по рейтингу
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]       

# Сначала отсортируем сам список по элементам -х[1] сортирует по убыванию 
ratings.sort(key=lambda x: (-x[1],x[0]))

from collections import OrderedDict

# Отсортированный список преобразуем в словарь
cafes = OrderedDict(ratings)

print(cafes)

#4.10 Создаём словарь и заполняем по принципу название сервера — ключ, 
# по которому хранится очередь задач для конкретного сервера. 
# Если поступает задача без высокого приоритета (последний элемент кортежа — False), 
# добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.
from collections import defaultdict, deque

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

def task_manager(tasks):
    server = defaultdict(deque)
    # Цикл по элементам списка
    for task in tasks:
        # Если последний элемент списка == True
        if task[-1]:
            # Добавляем в словарь номер задачи слева
            server[task[1]].appendleft(task[0])
        #Если последний элемент списка == False
        else:
            # Добавляем в словарь номер задачи справа
            server[task[1]].append(task[0])
            
    return server      

print(task_manager(tasks))

#Массивы
import numpy as np

arr = np.array([1,5,2,9,10], dtype=np.int8)
arr16 = np.array([1,5,2,9,10], dtype=np.int16)
arr32 = np.array([1,5,2,9,10], dtype=np.int32)
arr64 = np.array([1,5,2,9,10], dtype=np.int64)

nd_arr = np.array([
               [12, 45, 78],
               [34, 56, 13],
               [12, 98, 76]
               ], dtype=np.int16)

print(arr.itemsize)
print(arr16.itemsize)
print(arr32.itemsize)
print(arr64.itemsize)

zeros = np.zeros((5,4,3),dtype=np.float32)

n = np.arange(2.3, 32.6, 1.7)

print(n)

s = np.linspace(-6, 21, 60, endpoint=False, retstep=True)

print(s)