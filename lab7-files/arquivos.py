# -*- coding: utf-8 -*-

#####################################
####### ----  NÃO EDITAR  ---- ######
#####################################

import re
import os.path

## Testa se um arquivo existe
def existeArquivo(arquivo):
    if os.path.isfile(arquivo):
        return True
    else:
        return False

## Não alterar
## Remove múltiplos espaços de uma string.
## Ex.: removeMultiplosEspacos("a     bc de") -> "a bc de"
## Ex.: removeMultiplosEspacos("a     bc     de    ") -> "a bc de "
## Ex.: removeMultiplosEspacos(" a     bc     de    ") -> " a bc de "
def removeMultiplosEspacos(str):
    return re.sub(" +"," ",str)

# Recebe uma imagem pgm ou ppm em formato string,
# remove quebras de linha e espaços desnecessários
# e retorna uma lista com cada elemento do arquivo.
def limpaImagem(imagem):
    # Troca todas as quebras de linha por espacos
    imagem = imagem.replace("\n"," ")
    # Remove multiplos espacos
    imagem = re.sub(" +"," ",imagem)
    # Remove espacos do inicio e do fim da string
    imagem = imagem.strip()
    # Separa uma string por espacos e devolve uma lista
    imagem = imagem.split(" ")
    # Retorna a lista com cada valor em uma posicao da lista
    return imagem


################################################
####### ----  EDITAR A PARTIR DAQUI  ---- ######
################################################

## Função que verifica se em um código python,
## todo comando if e elif tem dois pontos.
def checkDoisPontos(arquivo):
    if not existeArquivo(arquivo): return False
    erros=0

    f = open(arquivo)
    lines = f.readlines()
    f.close()

    for lineNumber in range(len(lines)):
      fileContent = lines[lineNumber]

      print("Linha {}: {} ".format(lineNumber + 1, lines[lineNumber].replace("\n", "")), end="")

      match = re.search("^(if|elif).*:", lines[lineNumber])

      if not match:
        print("[ERRO]")
        erros += 1
      else:
        print("[OK]")

    return erros #Retorna o número de
                 #erros encontrados

## Função que recebe um arquivo texto e cria um
## novo arquivo com todo o conteúdo do arquivo
## original mas com todas as letras em maiúsculo.
def toMaiusculo(arquivo):
    if not existeArquivo(arquivo): return False
    cont=0
    
    f = open(arquivo)
    lines = f.readlines()
    newLines = []
    f.close()

    for lineNumber in range(len(lines)):
      content = list(lines[lineNumber])
      newLine = ''
      
      for i in range(len(content)):
        if content[i].isalpha():
          newLine += content[i].upper()
          cont += 1
        else:
          newLine += content[i]
      
      newLines.append(newLine)

    filename = arquivo.split('/')[-1].split('.')
    newF = open("{}M.{}".format("".join(filename[:-1]), filename[-1]), 'w')
    newF.writelines(newLines)
    newF.close()

    return cont # Retorna o número de caracteres
                # transformados para maiúsculo

# Função que gerencia o arquivo topscores.txt
# que mantém a lista das 10 maiores pontuações
def topScores(nome,score):
  ok = True
  filename = "topscores.txt"

  reader = open(filename, 'a+')
  reader.seek(0)
  lines = reader.readlines()
  reader.close()

  lines.sort(key=lambda line: int(line.split(',')[0]))

  if len(lines) < 10:
    lines.append("{},{}\n".format(score, nome))
  elif score > int(lines[0].split(',')[0]):
    lines[0] = "{},{}\n".format(score, nome)
  else:
    ok = False
  
  if ok:
    writer = open(filename, 'w')
    writer.writelines(lines)
    writer.close()

  return ok

# Função que recebe uma imagem PGM e cria
# uma versão espelhada da imagem.
def espelhaPGM(imagem,novaImagem):
  if not existeArquivo(imagem): return False
  
  reader = open(imagem)
  fileContent = limpaImagem(reader.read())

  imageType = fileContent.pop(0)
  ySize = int(fileContent.pop(0))
  xSize = int(fileContent.pop(0))
  maxBrightness = fileContent.pop(0)

  newFileLines = [
    imageType + '\n',
    "{} {}\n".format(ySize, xSize),
    maxBrightness + '\n'
  ]

  for _ in range(xSize):
    y = [ "{} ".format(y) for y in fileContent[:ySize]]
    line = "{}\n".format(''.join(reversed(y)))
    del fileContent[:ySize]

    newFileLines.append(line)

  writer = open(novaImagem, 'w')
  writer.writelines(newFileLines)
  writer.close()

  return True

# Função que recebe uma imagem PPM e cria
# uma versão rotacionada em 90 graus da imagem.
def rotaciona90PPM(imagem,novaImagem):
  if not existeArquivo(imagem): return False
  
  reader = open(imagem)
  fileContent = limpaImagem(reader.read())

  imageType = fileContent.pop(0)
  ySize = int(fileContent.pop(0))
  xSize = int(fileContent.pop(0))
  maxBrightness = fileContent.pop(0)

  lines = [
    imageType + '\n',
    "{} {}\n".format(xSize, ySize),
    maxBrightness + '\n'
  ]

  matrix = []

  # Agrupa os pixels nas linhas da matriz
  for _ in range(xSize):
    newMatrixLine = []
    temp = fileContent[:ySize * 3]
    del fileContent[:ySize * 3]
    for _ in range(len(temp) // 3):
      newMatrixLine.append(temp[:3])
      del temp[:3]
    matrix.append(newMatrixLine)

  # Pra rotacionar, faz a matriz transposta e inverte as linhas
  newMatrix = []
  for i in range(len(matrix[0])):
    line = []
    for j in range(len(matrix)):
      line.append(matrix[j][i])
    newMatrix.append(list(reversed(line)))

  for line in newMatrix:
    newLine = []
    for pixel in line:
      newLine.append("{} {} {} ".format(pixel[0], pixel[1], pixel[2]))
    lines.append("".join(newLine) + '\n')
  
  writer = open(novaImagem, 'w')
  writer.writelines(lines)
  writer.close()

  return True
