from HalfShafts import HalfShafts
from LockingRing import LockingRing
from commonDetails.Gear import Gear
from SynchronizationCone import SynchronizationCone
from Clutch import Clutch

class Transmission():
  # ходова / коробка передач
  def __init__(self):
    # напіввали
    self.halfShafts = HalfShafts()
    # блокувальне кільце
    self.lockingRing = LockingRing()
    # шестерня
    self.gear = Gear(120, 80)
    # конус синхронізації
    self.synchronizationCone = SynchronizationCone()
    # муфта
    self.clutch = Clutch()
    pass
  def __getFrictionForce(self):
    return self.frictionForce
  def __setFrictionForce(self, frictionForce):
    self.frictionForce = frictionForce
  
  def __shiftingToGear(self, side):
    self.lockingRing.setPosition(0)
    self.lockingRing.setSide(side)
    oldFrictionForce = self.__getFrictionForce()
    while oldFrictionForce >= 100:
      if self.gear.getRotationSpeed() == self.halfShafts.getRotationSpeed():
        self.clutch.moveToHalfShafts(side)
        pass
      self.__setFrictionForce(oldFrictionForce + 1)
      rotationSpeed = self.gear.getRotationSpeed()
      self.gear.setRotationSpeed(rotationSpeed - 1)
      pass
    pass
  def shifting(self, gear):
    if gear == 1: 
      self.__shiftingToGear('')

    elif gear == 2: self.__shiftingToGear('left')
    elif gear == 3: self.__shiftingToGear('rigth')
    elif gear == 4: self.__shiftingToGear('left')
    pass
  def moveLockedRingToSynchronizationCone(self):
    self.lockingRing.setPosition(10)
    pass
  def move(self, power):
    newPower = (self.gear.getNumberOfTeethOfLargeGear()/self.gear.getNumberOfTeethOfSmallGear) * self.halfShafts.getRotationSpeed()
    return newPower
  pass
