# 10.6 Шахматная доска
def get_chess(a):
    import numpy as np
    chess_arr = np.zeros((a, a), np.float16)
    chess_arr[1::2,::2] = 1
    chess_arr[::2,1::2] = 1
    print(chess_arr)

get_chess(1)

get_chess(4)

get_chess(8)

# 10.7 Shuffle плейлиста
def shuffle_seed(array):
    import numpy as np
    seed_num = np.random.randint(0, 4294967295, dtype=np.uint32)
    np.random.seed(seed_num)
    shuffled_playlist = np.random.permutation(array)
    print((shuffled_playlist, seed_num))

array = [1, 2, 3, 4, 5]

shuffle_seed(array)

shuffle_seed(array)

#10.8 Расстояния между векторов
from itertools import combinations
from secrets import choice
import numpy as np
def min_max_dist(*vectors):
    vectors_list = list()
    distance_list = list()
    vector_size = np.size(vectors[0])
    for vector in vectors:
        if (vector_size-np.size(vector)) != 0:
            raise ValueError('Vectors has different size!')
        vectors_list.append(vector)
    for vec in combinations(vectors_list, 2):
        distance_list.append(np.sqrt(np.sum((vec[0] - vec[1]) ** 2)))
    print((min(distance_list),max(distance_list)))
    
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

min_max_dist(vec1, vec2, vec3)

#10.9 Проверкана перпендикулярность векторов
from itertools import combinations
import numpy as np
def any_normal(*vectors):
    vectors_list = list()
    distance_list = list()
    vector_size = np.size(vectors[0])
    for vector in vectors:
        if (vector_size-np.size(vector)) != 0:
            raise ValueError('Vectors has different size!')
        vectors_list.append(vector)
    for vec in combinations(vectors_list, 2):
        if np.dot(vec[0],vec[1]) == 0:
            return True
        else: 
            return False
    

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))

#10.10 Генерация трехмерных массивов
def get_loto(num):
    import numpy as np
    arr = np.random.randint(1, 101, size=(num,5,5))
    print(arr)
get_loto(3)

#10.11 Генерация трехмерного массива без повторений
def get_unique_loto(num):
    arr = np.arange(1, 101)
    new_arr = np.random.choice(arr, size=(num,5,5), replace=False)
    print(new_arr)
get_unique_loto(3)  