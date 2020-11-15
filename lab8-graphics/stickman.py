from graphics import *

# Constrói a cabeça e retorna uma lista com seus membros
def makeHead(window: GraphWin, lineWidth: int, x: int, y: int):
  radius = 25
  eyeRadius = 5
  eyeXOffsetFromHeadCenter = 13
  eyeYOffsetFromHeadCenter = 8
  mouthYOffsetFromEyeCenter = 20

  head = Circle(Point(x, y), radius)
  head.setWidth(lineWidth)
  # head.draw(window)

  leftEyePX = head.getCenter().getX() - eyeXOffsetFromHeadCenter
  leftEyePY = head.getCenter().getY() - eyeYOffsetFromHeadCenter
  leftEyeP = Point(leftEyePX, leftEyePY)
  leftEye = Circle(leftEyeP, eyeRadius)
  leftEye.setWidth(lineWidth - 1)
  # leftEye.draw(window)

  rightEye = leftEye.clone()
  rightEye.move(eyeXOffsetFromHeadCenter * 2, 0)
  # rightEye.draw(window)

  mouth = Line(leftEye.getCenter(), rightEye.getCenter())
  mouth.move(0, mouthYOffsetFromEyeCenter)
  mouth.setWidth(lineWidth)
  # mouth.draw(window)

  return [head, leftEye, rightEye, mouth]

# Constrói a coluna e a retorna uma lista com seus membros
def makeSpine(window: GraphWin, lineWidth: int, head: Circle):
  spineLength = 80

  spineP1X = head.getCenter().getX()
  spineP1Y = head.getCenter().getY() + head.getRadius()
  spineP1 = Point(spineP1X, spineP1Y)
  spineP2 = spineP1.clone()
  spineP2.move(0, spineLength)
  spine = Line(spineP1, spineP2)
  spine.setWidth(lineWidth)
  # spine.draw(window)

  return [spine]

# Constrói um braço e o retorna uma lista com seus membros
def makeArm(window: GraphWin, lineWidth: int, spine: Line, isLeftArm: bool):
  armXOffsetFromSpine = 30
  armYOffsetFromSpine = 50
 
  if isLeftArm:
    armXOffsetFromSpine *= -1

  armP2X = spine.getP1().getX() - armXOffsetFromSpine
  armP2Y = spine.getP1().getY() + armYOffsetFromSpine
  armP2 = Point(armP2X, armP2Y)
  arm = Line(spine.getP1(), armP2)
  arm.setWidth(3)
  # arm.draw(window)

  return [arm]

# Constrói uma perna e a retorna uma lista com seus membros
def makeLeg(window: GraphWin, lineWidth: int, spine: Line, isLeftLeg: bool):
  legXOffsetFromSpine = 30
  legYOffsetFromSpine = 80

  if isLeftLeg:
    legXOffsetFromSpine *= -1
  
  legP2X = spine.getP2().getX() - legXOffsetFromSpine
  legP2Y = spine.getP2().getY() + legYOffsetFromSpine
  legP2 = Point(legP2X, legP2Y)
  leg = Line(spine.getP2(), legP2)
  leg.setWidth(lineWidth)
  # leg.draw(window)

  return [leg]

# Constrói o jogador e retorna uma lista com seus membros
def makeStickman(window: GraphWin, xAnchor: int, yAnchor: int):
  commonWidth = 3
  headRadius = 30

  head = makeHead(window, commonWidth, xAnchor, yAnchor)
  spine = makeSpine(window, commonWidth, head[0])
  leftArm = makeArm(window, commonWidth, spine[0], True)
  rightArm = makeArm(window, commonWidth, spine[0], False)
  leftLeg = makeLeg(window, commonWidth, spine[0], True)
  rightLeg = makeLeg(window, commonWidth, spine[0], False)

  return [rightLeg, leftLeg, rightArm, leftArm, spine, head]

# Esconde uma parte do jogador
def showStickmanPart(window: GraphWin, Stickman: list, index: int):
  for part in Stickman[index]:
    if type(part) is list:
      for subpart in part:
        subpart.draw(window)
    else:
      part.draw(window)
