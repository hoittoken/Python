def exp_value(var,prob):
    result=0
    if type(var)!=int and type(var)!=float \
        or type(prob)!=int and type(prob)!=float:
        print('Check type of input!\nThey must be numbers!')
        return None
print(exp_value(6,1))