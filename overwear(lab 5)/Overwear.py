# Створити клас Overcoat верхня одежа.
# Реалізувати перевантажені оператори:
  # Перевірка на рівність ==
  # Операція присвоєння одного об'єкта в інший
  # Порівняння по вартості двух костюмів одного типу " > "
  # Введення-виведення інформації про об'єкт ..

from enum import Enum

class Types(Enum):
  SUMMER = 1
  AUTEMN = 2
  WINTER = 3
  SPRING = 4

class Overcoat():
  def __init__(self):
    pass

  def getType(self):
    return self.type

  def setType(self, type):
    self.type = type
    pass

  def getSize(self):
    return self.size

  def setSize(self, size):
    self.size = size
    pass
  
  def getPrice(self):
    return self.price

  def setPrice(self, price):
    self.price = price
    pass

  def checkEqualsOvercoat(self, firstOverCoat, secondOvercoat):
    return firstOverCoat == secondOvercoat

  def repaceOvercoatBySecond(self, firstOverCoat, secondOvercoat):
    return firstOverCoat
  
  def comparisonPrices(self, priceOfFirst, priceOfSecond):
    return priceOfFirst > priceOfSecond

  def showOvercoatData(self, overcoat):
    print(self)
    pass

class Overwear(Overcoat):
  def __init__(self):
    pass
  # тут перевизнаться останні методи із виводом повідомлень і застосуванням enum
  def comparisonPrices(self, priceOfFirst, priceOfSecond):
    if priceOfFirst > priceOfSecond:
      print('price of first more')
      pass
    else:
      print('price of second more')
      pass
    pass
  def checkEqualsOvercoat(self, firstOvercoat, secondOvercoat):
    if firstOvercoat == secondOvercoat:
      print('equals overcoats')
      pass
    else:
      print('no equals overcoats')
      pass
    pass
  def repaceOvercoatBySecond(self, firstOverCoat, secondOverCoat):
    if firstOverCoat == secondOverCoat:
      return 'there overcoats are flat'
    else:
      firstOverCoat = secondOverCoat
      return 'the first overcoat is replaced by the second'
  def showOvercoatData(self, overwear):
    print("type : " + str(overwear.getType()) + " | price : " + str(overwear.getPrice()) + " | size : " + str(overwear.getSize()))
    pass

firstOvercoat = Overwear()
firstOvercoat.setType(Types.SUMMER.name)
firstOvercoat.setPrice(20)
firstOvercoat.setSize(120)
firstOvercoat.showOvercoatData(firstOvercoat)

secondOvercoat = Overwear()
secondOvercoat.setType(Types.WINTER.name)
secondOvercoat.setPrice(29)
secondOvercoat.setSize(120)
secondOvercoat.showOvercoatData(secondOvercoat)

firstOvercoat.checkEqualsOvercoat(firstOvercoat, secondOvercoat)
secondOvercoat.comparisonPrices(firstOvercoat.getPrice(), secondOvercoat.getPrice())

# class RackForClothes():
#   def __init__(self):
#     self.OuterwearsList []
#     pass
#   def setOuterwear(self, outerwear):
#     newOuterwear = {
#       "id": outerwear.id,
#       "type": outerwear.type,
#       "price": outerwear.price,
#       "size": outerwear.size
#     }
#     self.setOuterwear.append(outerwear)
#     pass
#   def getOuterwearsList(self):
#     return self.OuterwearsList

#   def showRick(self):
#     for product in self.OuterwearsList:
#       print("type : " + product.type + " | price : " + product.price + " | size : " product.size)
#       pass
#   pass
