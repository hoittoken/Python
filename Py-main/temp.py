def geometric_mean(*args):
    args_mult = 1
    n = 0
    for i in args:
        n += 1
        args_mult *= i
    return args_mult ** (1/n)

def arithmetic_mean(*args):
    args_sum = 0
    n = 0
    for i in args:
        n += 1
        args_sum += i
    return args_sum / n

arithmetic_mean_lambda = lambda *args: sum(args) / len(args)

print(geometric_mean(1,2,3,4,5,6))
print(arithmetic_mean(1,2,3,4,5,6))
print(arithmetic_mean_lambda(1,2,3,4,5,6))

"Изменение выполнено на рабочем компе" 
     