class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2


rectangle = Rectangle(5,4)
print(f"Area => {rectangle.area()} unit")
print(f"Area => {rectangle.perimeter()} unit")