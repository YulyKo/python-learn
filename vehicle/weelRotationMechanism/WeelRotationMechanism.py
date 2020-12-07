from TarqueSensor import TarqueSensor
from Helm import Helm
from GearShaftGear import GearShaftGear
from ElectricMotor import ElectricMotor

class WeelRotationMechanism:
  def __init__(self):
    self.tarqueSensor = TarqueSensor()
    self.helm = Helm()
    self.gearShaftGear = GearShaftGear(10, 32)
    self.electricMotor = ElectricMotor()
    pass
  def scrolleHelm(self, angleOfRotation):
    self.helm.setAngleOfRotation(angleOfRotation)
    self.tarqueSensor.on(angleOfRotation)
    self.gearShaftGear.scroll(angleOfRotation)
    factor = self.getFactorOfStrengthenedTurn(angleOfRotation)
    self.electricMotor.scroll(factor)
    pass
  def getFactorOfStrengthenedTurn(self, angleOfRotation):
    return angleOfRotation * 2
  pass