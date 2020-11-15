from graphics import *
from scenes import drawGameScene, drawYouLostScene, drawYouWonScene
from utils import waitForReturnKey, undrawAll, parseStringForRendering, getRandomWord
from stickman import makeStickman, showStickmanPart

# Inicializa a suposição de letras
def runGuess(window: GraphWin, word: str, stickman: list):
  lives = 5
  usedChars = []
  guessedWord = ''.join(['_' for char in word])

  textObject = Text(Point(window.getWidth() / 2, 30), parseStringForRendering(guessedWord))
  textObject.draw(window)
  usedCharsObject = Text(Point(window.getWidth() / 2, window.getHeight() - 15), '')
  usedCharsObject.draw(window)

  validKeys = [chr(code) for code in range(65, 91)]

  while lives > -1:
    if not ('_' in guessedWord):
      textObject.undraw()
      usedCharsObject.undraw()
      return True

    key = window.getKey().upper()

    if key in validKeys:
      if not (key in usedChars):
        usedChars.append(key)
        usedCharsObject.setText(''.join(usedChars))
        if not (key in word):
          showStickmanPart(window, stickman, lives)
          lives -= 1
        else:
          guessedWord = list(guessedWord)
          for i, char in enumerate(list(word)):
            print(char)
            if char == key:
              guessedWord[i] = char
          guessedWord = ''.join(guessedWord)
          textObject.setText(parseStringForRendering(guessedWord))

  time.sleep(.5)
  usedCharsObject.undraw()
  textObject.undraw()

  return False

# Loop principal do jogo
def loop(window: GraphWin):
  lives = 5
  word = getRandomWord()
  print(word)

  gameScene = drawGameScene(window)
  stickman = makeStickman(window, window.getWidth() / 2, (window.getHeight() / 2) - 70)
  won = runGuess(window, word, stickman)
  undrawAll(stickman)
  undrawAll(gameScene)

  endGameScene = None
  if won:
    endGameScene = drawYouWonScene(window, word)
  else:
    endGameScene = drawYouLostScene(window, word)
  
  waitForReturnKey(window)
  undrawAll(endGameScene)
