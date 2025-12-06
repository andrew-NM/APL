class Point:
    __slots__ = ('x','y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


first_point = Point(1,2) # run normally
second_point = Point(1,2,3) #Raise an error because slots restricts only specific attributes to be given 