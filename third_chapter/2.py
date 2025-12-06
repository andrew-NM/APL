my_list = list(range(1,11))
result = list(map(lambda x: x*x, filter(lambda y: y % 2 != 0, my_list)))
print(result)
