from functools import reduce
def my_reduce(function, iterator, initializer=0):
    result = iterator[0]
    for i in range(1, len(iterator)):
        result = function(result, iterator[i])
    return result + initializer
    
my_list = list(range(1,11))
result = my_reduce(lambda x, y: x + y, my_list, 10)
print(result)
