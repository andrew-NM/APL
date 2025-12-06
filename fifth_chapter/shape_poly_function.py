from math import pi

class Shape:
    def print_shape_area(self):
         print("No shape specified")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def print_shape_area(self):
        print(f"Area = {pi * (self.radius ** 2) :.2f} unit")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_shape_area(self):
        print(f"Area = {self.height * self.width:.2f} unit")
    

list_of_instances = [Shape(), Circle(4), Rectangle(3,4)]
for instance in list_of_instances:
    print("-" * 50)
    print(f"{instance.__class__.__name__}:")
    instance.print_shape_area()
