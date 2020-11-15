from graphics import *
from random import randint

# Espera a tecla enter ser pressionada
def waitForReturnKey(window: GraphWin):
  if window.getKey() != 'Return':
    waitForReturnKey(window)

# Desativa a renderização de uma lista de componentes recursivamente
def undrawAll(components: list):
  for component in components:
    if type(component) is list:
      undrawAll(component)
    else:
      component.undraw()

# Retorna uma palavra do arquivo words.txt randomicamente
def getRandomWord():
  path = './words.txt'
  reader = open(path, 'r')
  words = [ word.replace('\n', '') for word in reader.readlines()]
  reader.close()

  return words[randint(0, len(words) - 1)]

# Inicializa a tela do graphics.py
def initWindow():
  # 360p
  window = GraphWin("Forca", 360, 360)
  window.setBackground("white")

  rectP1 = Point(0, 0)
  rectP2 = Point(window.getWidth(), window.getHeight())
  rectangle = Rectangle(rectP1, rectP2)
  rectangle.setWidth(10)
  rectangle.draw(window)

  return window

# Trata uma string para ser renderizada como a palavra da forca
def parseStringForRendering(text: str):
  return ''.join([' ' + char for char in text]).strip()
