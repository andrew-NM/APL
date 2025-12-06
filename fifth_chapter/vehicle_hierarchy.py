class Vehicle:
    def move(sef):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(sef):
        print("Car is driving")

class Bike(Vehicle):
    def move(sef):
        print("Bike is driving")

vehicle_list = [Vehicle(), Car(), Bike()]
for instance in vehicle_list:
    instance.move()