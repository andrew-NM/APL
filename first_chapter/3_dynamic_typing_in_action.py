def my_func():
    pass
data = 4
print(type(data))
data = [1,2,3,4]
print(type(data))
data = my_func
print(type(data))

#output
# <class 'int'>
# <class 'list'>
# <class 'function'>

#Reflection: What does this reveal about Python?
# A variable does not have a fixed type.
# The type belongs to the value, not the variable name.
# The interpreter checks types at runtime, not at compile time.