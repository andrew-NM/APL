class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))
        else:
            return "Invalid opeartion!"
        
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector((self.x * other.x), (self.y * other.y))
        else:
            return "Invalid opeartion!"
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
first_vector = Vector(5,6)
second_vector = Vector(3,2)
mul_vector = first_vector * second_vector
sub_vector = first_vector - second_vector

print(f"First vector => {first_vector}")
print(f"Second vector => {second_vector}")
print(f"Multiplied vector => {mul_vector}")
print(f"Substracted vector => {sub_vector}")