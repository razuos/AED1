from arquivos import checkDoisPontos, toMaiusculo, topScores, espelhaPGM, rotaciona90PPM
import os

print('checkDoisPontos')
print('--------------')
print(checkDoisPontos('./resources/code.txt'))
print(checkDoisPontos('./idontexist.txt'))
print('--------------')

print('toMaiusculo')
print('--------------')
print(toMaiusculo('./idontexist.txt'))
print(toMaiusculo('./resources/lorem.txt'))
print('--------------')

print('topScores')
print('--------------')
print(topScores('Rafael', 1))
print(topScores('Joao', 2))
print(topScores('Rafaela', 3))
print(topScores('Thiago', 4))
print(topScores('Matheus', 5))
print(topScores('Laura', 6))
print(topScores('Ana', 7))
print(topScores('Miguel', 8))
print(topScores('Moacir', 9))
print(topScores('Leticia', 10))
print(topScores('Pedro', 11))
print(topScores('Jose', 12))
print(topScores('Gustavo', 13))
print('--------------')

print('espelhaPGM')
print('--------------')
print(espelhaPGM('./idontexist.txt', './idontexist.txt'))
for file in os.listdir('./resources/pgm'):
  print(file)
  print(espelhaPGM("./resources/pgm/{}".format(file), "./output_{}".format(file)))
print('--------------')

print('rotaciona90PPM')
print('--------------')
print(rotaciona90PPM('./idontexist.txt', './idontexist.txt'))
for file in os.listdir('./resources/ppm'):
  print(file)
  print(rotaciona90PPM("./resources/ppm/{}".format(file), "./output_{}".format(file)))
print('--------------')