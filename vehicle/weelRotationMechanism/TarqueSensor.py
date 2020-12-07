from GearShaftGear import GearShaftGear
from commonDetails.Gear import Gear

class TarqueSensor:
  # датчик моменту
  def __init__(self):
    self.gearShaftGear = GearShaftGear()
    self.gear = Gear(0, 10)
    pass
  def on(self, angleOfRotation):
    coefficient = angleOfRotation * ( self.gear.getgetNumberOfTeethOfSmallGear )
    self.gearShaftGear.scroll(coefficient)
    return coefficient
  pass