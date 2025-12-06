class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

def shape_factory(shape):
    if shape == "circle":
        return Circle()
    elif shape == "Square":
        return Square()

shape = shape_factory("circle")
shape.draw()