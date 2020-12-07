class Pedal:
  MAX_POSITION = -30
  MIN_POSITION = 0
  def __init__(self):
    self.pedalPosition = 0
    pass
  def __setPedalPosition(self, value):
    self.pedalPosition = value
    pass
  def __getPedalPosition(self):
    return self.pedalPosition
  def pressPedal(self, value):
    self.__setPedalPosition(value)
    if self.__getPedalPosition() != self.MAX_POSITION:
      return self.__getPedalPosition * -0.5
    elif self.__getPedalPosition() == self.MAX_POSITION:
      return self.__getPedalPosition * -0.7
    pass
    pass
  pass