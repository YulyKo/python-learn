# 1 Create a vehicle that encapsulates engine, wheels and gas-tank.
# All internal items should interact with each other.
# 2 Internal mechanism should be hidden from client.
# All he needs is accelerate(), brake(), turn() these method should be part of Driveable interface.
# 3 Create a Boat that extends Vehicle.
# 4 Create a Car that extends Vehicle.
# 5 Create a Solar Car that extends Car.

class Engine:
  pass

class Wheels:
  pass

class GasTank:
  pass

class Vehicle(Engine, Wheels, GasTank):
  def accelerate(self):
    pass
  def brake(self):
    pass
  def turn(self):
    pass
  pass

class Boat(Vehicle):
  pass

class Car(Vehicle):
  pass

class Solar(Vehicle):
  pass
