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

  def __setType(self, type):
    self.type = type
    pass

  def getSize(self):
    return self.size

  def __setSize(self, size):
    self.size = size
    pass
  
  def getPrice(self):
    return self.price

  def __setPrice(self, price):
    self.price = price
    pass

  def checkEqualsOvercoat(self, firstOverCoat, secondOvercoat):
    return firstOverCoat == secondOvercoat

  def repaceOvercoatByEnother(self, firstOverCoat, secondOvercoat):
    return firstOverCoat
  
  def comparisonPrices(self, priceOfFirst, priceOfSecond):
    return priceOfFirst > priceOfSecond

  def showOvercoatData(self):
    print(self)
    pass

class Overwear(Overcoat):
  # тут перевизначити останні методи із виводом повідомлень і застосуванням enum
  def FunctionName(self):
    print('I am a life')
    pass