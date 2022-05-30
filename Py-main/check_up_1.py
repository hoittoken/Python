#from temp import geometric_mean

def geometric_mean(*args):
    args_mult = 1
    n = 0
    for i in args:
        n += 1
        args_mult *= i
    return args_mult ** (1/n)

print(geometric_mean(1,2,3,4,5,6))