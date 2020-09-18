# Composition is a "has-a" relationship.



class Car():
    def __init__(self, engine, frame, tires):
        self.engine = engine
        self.frame = frame
        self.tires = tires

class Engine():
    def __init__(self, cylenders, liters):
        self.cylenders = cylenders
        self.liters

class Frame():
    def __init__(self, material):
        self.material = material

class Tire():
    def __init__(self, radius):



tires = [Tire(16, Tire(16), Tire(16))]
frame = Frame("Plastics")
engine = Engine(8, 6.4)

car = Car(engine, frame, tires)
print(car.engine.cylenders)
print(car.tires[0].radius)