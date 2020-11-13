from random import randint
from graphics import *

wordsPath = './words.txt'

def getRandomWord(wordsPath):
  reader = open(wordsPath, 'r')
  words = [ word.upper().replace('\n', '') for word in reader.readlines()]
  reader.close()

  return words[randint(0, len(words))]

def initWindow():
  # 360p
  return GraphWin("Forca", 640, 360)

def turn():
  window = initWindow()
  drawGallow(window)
  window.getMouse()
  window.close()

# def drawPerson(window):

def drawGallow(window):
  gallowTopXAnchor = 80
  l1 = Line(Point(gallowTopXAnchor, 0), Point(gallowTopXAnchor, 50))
  l1.setWidth(3)
  l1.draw(window)

  headRadius = 30
  headWidth = 3
  head = Circle(Point(gallowTopXAnchor, l1.getP2().getY()  + headRadius), headRadius)
  head.setWidth(headWidth)
  head.draw(window)

  leftEye = Circle(Point(head.getCenter().getX() - 13, head.getCenter().getY() - 10), 5)
  leftEye.setWidth(headWidth - 1)
  leftEye.draw(window)

  rightEye = leftEye.clone()
  rightEye.move(26, 0)
  rightEye.setWidth(headWidth - 1)
  rightEye.draw(window)

  mouthLeftP = Point(leftEye.getCenter().getX(), leftEye.getCenter().getY() + 24)
  mouthRightP = Point(rightEye.getCenter().getX(), rightEye.getCenter().getY() + 24)
  mouthMiddleX = (leftEye.getCenter().getX() + rightEye.getCenter().getX()) / 2
  mouthMiddleY = leftEye.getCenter().getY() + 15
  mouthMiddleP = Point(mouthMiddleX, mouthMiddleY)
  mouth = Polygon(mouthLeftP, mouthMiddleP, mouthRightP)
  mouth.setFill('black')
  mouth.draw(window)

  spineP1 = Point(gallowTopXAnchor, l1.getP2().getY() + (headRadius * 2))
  spineP2 = spineP1.clone()
  spineP2.move(0, 130)
  spine = Line(spineP1, spineP2)
  spine.setWidth(3)
  spine.draw(window)

  leftArmP2 = Point(gallowTopXAnchor - 55, spineP2.getY() + 80)
  leftArm = Line(spineP2, leftArmP2)
  leftArm.setWidth(3)
  leftArm.draw(window)

  rightLegP2 = leftArmP2.clone()
  rightLegP2.move(110, 0)
  rightLeg = Line(spineP2, rightLegP2)
  rightLeg.setWidth(3)
  rightLeg.draw(window)


turn()