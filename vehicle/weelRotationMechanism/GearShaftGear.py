class GearShaftGear:
  def __init__(self, numberOfTeethOfRail, numberOfTeethOfGear):
    self.numberOfTeethOfRail = numberOfTeethOfRail
    self.numberOfTeethOfGear = numberOfTeethOfGear
    pass
  def scroll(self, coefficient):
    return coefficient * ( self.numberOfTeethOfGear / self.numberOfTeethOfRail )
  pass
