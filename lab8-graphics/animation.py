from graphics import *

# Move uma lista de componentes
def moveAll(components: list, dx: int, dy: int):
  for component in components:
    if type(component) is list:
      moveAll(component, dx, dy)
    else:
      component.move(dx, dy)

# Desenha a animação de perda do jogo
def animateStickmanLostGame(window: GraphWin, stickman: list):
  times = 6
  while times != 0:
    time.sleep(.5)
    if times % 2 != 0:
      moveAll(stickman, 60, 0)
    else:
      moveAll(stickman, -60, 0)
    times -= 1
  time.sleep(.5)
  moveAll(stickman, -30, 0)
  time.sleep(1)

# Desenha a animação de vencer o jogo
def animateStickmanWonGame(window: GraphWin, stickman: list):
  while stickman[5][0].getCenter().getX() < window.getWidth():
    update(2)
    moveAll(stickman, 50, 0)
    