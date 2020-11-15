from graphics import *
from utils import parseStringForRendering, undrawAll
from stickman import makeStickman, showStickmanPart
from animation import animateStickmanLostGame, animateStickmanWonGame

def drawGameScene(window: GraphWin):
  
  line1P1 = Point(0, 50)
  line1P2 = Point(window.getWidth(), 50)
  line1 = Line(line1P1, line1P2)
  line1.setWidth(5)
  line1.draw(window)

  line2P1 = Point(0, window.getHeight() - 30)
  line2P2 = Point(window.getWidth(), window.getHeight() - 30)
  line2 = Line(line2P1, line2P2)
  line2.setWidth(5)
  line2.draw(window)

  gallowBaseP1 = Point(25, window.getHeight() - 40)
  gallowBaseP2 = Point(105, window.getHeight() - 40)
  gallowBase = Line(gallowBaseP1, gallowBaseP2)
  gallowBase.setWidth(3)
  gallowBase.draw(window)

  gallowBaseX = (gallowBaseP2.getX() + gallowBaseP1.getX()) / 2
  gallowBase2P1 = Point(gallowBaseX, window.getHeight() - 40)
  gallowBase2P2 = Point(gallowBaseX, 70)
  gallowBase2 = Line(gallowBase2P1, gallowBase2P2)
  gallowBase2.setWidth(3)
  gallowBase2.draw(window)

  gallowArmP2 = Point(window.getWidth() / 2, 70)
  gallowArm = Line(gallowBase2P2, gallowArmP2)
  gallowArm.setWidth(3)
  gallowArm.draw(window)

  gallowRopeP2 = Point(window.getWidth() / 2, 85)
  gallowRope = Line(gallowArmP2, gallowRopeP2)
  gallowRope.setWidth(3)
  gallowRope.draw(window) 

  gallowRope2P1 = Point(gallowRopeP2.getX() - 25, gallowRopeP2.getY())
  gallowRope2P2 = Point(gallowRopeP2.getX() + 25, gallowRopeP2.getY())
  gallowRope2 = Line(gallowRope2P1, gallowRope2P2)
  gallowRope2.setWidth(3)
  gallowRope2.draw(window)

  return [line1, line2, gallowBase, gallowBase2, gallowArm, gallowRope, gallowRope2]

# Desenha a cena de boas vindas e retorna uma lista com seus componentes
def drawWelcomeScene(window: GraphWin):
  gameName = Text(Point(window.getWidth() / 2, 30), 'Jogo da Forca')
  gameName.draw(window)

  preRulesText = "Regras:"
  preRules = Text(Point(window.getWidth() / 2, window.getHeight() - 280), preRulesText)
  preRules.draw(window)

  rulesText = "Digite a letra que você acha que se encaixa na\n palavra mostrada, caso você erre, seu boneco\n fica mais próximo da morte. As letras que já\n foram utilizadas aparecerão na parte inferior\n da tela. Boa sorte!"
  rules = Text(Point(window.getWidth() / 2, window.getHeight() - 200), rulesText)
  rules.draw(window)

  pressEnterText = "Pressione enter para iniciar"
  pressEnter = Text(Point(window.getWidth() / 2, window.getHeight() - 80), pressEnterText)
  pressEnter.draw(window)

  jokeText = "Mas lembre-se, toda vez que você perde,\n uma familia de Zé Palito perde um pai."
  joke = Text(Point(window.getWidth() / 2, window.getHeight() - 25), jokeText)
  joke.draw(window)

  return [gameName, preRules, rules, pressEnter, joke]

def drawYouLostScene(window: GraphWin, word: str):
  halfWidth = window.getWidth() / 2
  youLostText = "Você perdeu!"
  youLost = Text(Point(halfWidth, 20), youLostText)
  youLost.draw(window)

  theWordWasText = "A palavra era:"
  theWordWas = Text(Point(halfWidth, 80), theWordWasText)
  theWordWas.draw(window)

  theWord = Text(Point(halfWidth, 130), parseStringForRendering(word))
  theWord.draw(window)

  stickman = makeStickman(window, (window.getWidth() / 2) + 30, window.getHeight() / 2)
  for i in range(6):
    showStickmanPart(window, stickman, i)
  animateStickmanLostGame(window, stickman)
  undrawAll(stickman)
  
  pressEnterText = "Pressione enter para reiniciar"
  pressEnter = Text(Point(window.getWidth() / 2, window.getHeight() - 80), pressEnterText)
  pressEnter.draw(window)

  return [youLost, theWordWas, theWord, pressEnter]

def drawYouWonScene(window: GraphWin, word: str):
  halfWidth = window.getWidth() / 2
  youLostText = "Você venceu!"
  youLost = Text(Point(halfWidth, 20), youLostText)
  youLost.draw(window)

  theWordWasText = "A palavra era:"
  theWordWas = Text(Point(halfWidth, 80), theWordWasText)
  theWordWas.draw(window)

  theWord = Text(Point(halfWidth, 130), parseStringForRendering(word))
  theWord.draw(window)

  stickman = makeStickman(window, 1, window.getHeight() / 2)
  for i in range(6):
    showStickmanPart(window, stickman, i)
  animateStickmanWonGame(window, stickman)
  undrawAll(stickman)
  
  pressEnterText = "Pressione enter para reiniciar"
  pressEnter = Text(Point(window.getWidth() / 2, window.getHeight() - 80), pressEnterText)
  pressEnter.draw(window)

  return [youLost, theWordWas, theWord, pressEnter]