class Gear:
  # шестерня
  def __init__(self, numberOfTeethOfLargeGear, numberOfTeethOfSmallGear):
    # the number of teeth of the large gear
    self.numberOfTeethOfLargeGear = numberOfTeethOfLargeGear
    self.numberOfTeethOfSmallGear = numberOfTeethOfSmallGear
    self.rotationSpeed = 0
    pass
  def getNumberOfTeethOfLargeGear(self):
    return self.numberOfTeethOfLargeGear
  def getNumberOfTeethOfSmallGear(self):
    return self.numberOfTeethOfSmallGear
  def getRotationSpeed(self):
    return self.rotationSpeed
  def setRotationSpeed(self, rotationSpeed):
    self.rotationSpeed = rotationSpeed
    pass
  pass