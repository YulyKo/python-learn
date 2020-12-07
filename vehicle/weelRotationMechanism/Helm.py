class Helm:
  # кермо
  MAX_ROTATION = 360
  def __init__(self):
    self.angleOfRotation
    pass
  def setAngleOfRotation(self, angleOfRotation):
    if angleOfRotation < self.MAX_ROTATION:
      self.angleOfRotation = angleOfRotation
      pass
    pass
  def getAngleOfRotation(self):
    return self.angleOfRotation
  pass