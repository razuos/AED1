from graphics import GraphicsError
from game import loop
from utils import initWindow, waitForReturnKey, undrawAll
from scenes import drawWelcomeScene

def main():
  window = initWindow()

  welcomeScene = drawWelcomeScene(window)
  waitForReturnKey(window)
  undrawAll(welcomeScene)

  while True:
    loop(window)

if __name__ == '__main__':
  main()