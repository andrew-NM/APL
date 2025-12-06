my_list = [10,20,30]
print(id(my_list)) # 140537778526784
my_list.append(40)
print(id(my_list)) # 140537778526784

"""
Mutable object its identity never changes after editing the value or assigning a new value
"""