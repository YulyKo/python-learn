# 1 Create a vehicle that encapsulates engine, wheels and gas-tank.
# All internal items should interact with each other.
# 2 Internal mechanism should be hidden from client.
# All he needs is accelerate(), brake(), turn() these method should be part of Driveable interface.
# 3 Create a Boat that extends Vehicle.
# 4 Create a Car that extends Vehicle.
# 5 Create a Solar Car that extends Car.
from multiprocessing import Process
from threading import Thread, Event
import time
from transmission.Transmission import Transmission

class SparkPlug:
  def __init__(self):
    pass
  def turnOn(self):
    stop_event = Event()
    # We create a Process
    action_process = Process(target=self.__do_actions(stop_event))
    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=1)
    pass
  def __do_actions(self, stop_event):
    while True:
      time.sleep(1)
    # Here we make the check if the other thread sent a signal to stop execution.
      if stop_event.is_set():
        break
    pass
  pass

class Valve:
  def __init__(self):
    self.isOpen = False
    pass
  def __close(self):
    self.isOpen = False
    pass
  def open(self, seconds):
    stop_event = Event()
    # We create a Process
    action_process = Process(target=self.__do_actions(stop_event, seconds))
    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=seconds)
    pass
  def __do_actions(self, stop_event, seconds):
    while True:
      time.sleep(seconds)
      # Here we make the check if the other thread sent a signal to stop execution.
      if stop_event.is_set():
        self.__close()
      break
    # pass
class ExhaustValve(Valve):
  pass

class FlueAndAirInakeValve(Valve):
  pass

class Piston:
  def __init__(self):
    self.Pressure = 0
    self.sparkPlug = SparkPlug()
    self.exhaustValve = ExhaustValve()
    self.flueAndAirInakeValve = FlueAndAirInakeValve()
    self.charionShaft = CharionShaft()
    pass
  def __setSecondsForOpenValve(self, value):
    self.secondsForOpenValve = value
    pass
  def __getSecondsForOpenValve(self):
    return self.secondsForOpenValve
  def __setPressure(self, value):
    # тиск у поршні
    self.pistonPressure = value
    pass
  def __getPressure(self):
    return self.pistonPressure
    
  def __firstTact(self):
    seconds = self.__getSecondsForOpenValve()
    self.flueAndAirInakeValve.open(seconds)
    pass
  def __secondTact(self):
    self.__setPressure(self.__getPressure + 3000)
    pass
  def __thirdTact(self):
    self.sparkPlug.turnOn()
    self.__setPressure(self.__getPressure + 12000)
    self.charionShaft.setPosition(self.charionShaft.getPosition + 90)
    pass
  def __fourthTact(self):
    self.exhaustValve.open(1)
    self.__setPressure(0)
    pass
  def start(self, seconds):
    self.__setSecondsForOpenValve(seconds)
    self.__firstTact()
    self.__secondTact()
    self.__thirdTact()
    self.__fourthTact()
    pass
  pass

class CharionShaft:
  def __init__(self):
    self.position = 0
    pass
  def setPosition(self, value):
    self.position = value
    pass
  def getPosition(self):
    return self.position
  pass

class Engine:
  # двигун
  def calckGettedVolume(self, seconds):
    # 1 sec == 10 ml volume
    return seconds * 10
  def getEnergy(self, volume):
    pass
  pass

class Disel(Engine):
  # 4х тактний двигун внутрішнього згорання
  def __init__(self):
      self.__initPiston()
      self.gasTank = GasTank()
      pass
  def __initPiston(self):
    # поршень
    self.firstPiston = Piston()
    self.secondPiston = Piston()
    self.thirdPiston = Piston()
    self.fourthPiston = Piston()
    pass
  def getEnergy(self, volume):
    if volume <= 1:
      print('Low gas level & car stopped')
      return 0
    else:
      defaultSeconds = 2
      self.firstPiston.start(defaultSeconds)
      self.thirdPiston.start(defaultSeconds)
      self.fourthPiston.start(defaultSeconds)
      self.secondPiston.start(defaultSeconds)
      return 4
  pass

from commonDetails.Pedal import Pedal
class Axelerator(Pedal):
  # газ
  pass

class Brake(Pedal):
  # гальмо
  pass

class Wheels:
  # колеса
  pass

class GasTank:
  # паливний бак
  def __init__(self):
    pass
  def setVolume(self, volume):
    self.volume = volume
    pass
  def useVolume(self, gettedVolume):
    self.volume -= gettedVolume
    pass
  def getVolume(self):
    return self.volume
  pass

from weelRotationMechanism.WeelRotationMechanism import WeelRotationMechanism
from transmission.Transmission import Transmission
class Vehicle(Engine, Transmission, GasTank):
  # транспортний засіб
  def __init__(self):
    self.trasmission = Transmission()
    self.weelRotationMechanism = WeelRotationMechanism()
    self.axeleratorPedal = Axelerator()
    self.brakePedal = Brake()
    pass

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
