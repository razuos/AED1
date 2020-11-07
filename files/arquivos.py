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
    if not existeArquivo(arquivo): return -1
    erros=0
    f = open(arquivo)
    lines = f.readlines()
    f.close()

    for lineNumber in range(len(lines)):
      content = lines[lineNumber]

      print("Linha {}: {} ".format(lineNumber, lines[lineNumber].replace("\n", "")), end="")

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
    if not existeArquivo(arquivo): return -1
    cont=0
    
    f = open(arquivo)
    lines = f.readlines()
    newLines = []
    f.close()

    for lineNumber in range(len(lines)):
      content = lines[lineNumber]
      
      for i in range(len(content)):
        if content[i].isalpha():
          content[i] = content[i].upper()

      print(content)

    

      

    return cont # Retorna o número de caracteres
                # transformados para maiúsculo

print(toMaiusculo('test.py.txt'))

# Função que gerencia o arquivo topscores.txt
# que mantém a lista das 10 maiores pontuações
def topScores(nome,score):
    ok=True
    # Escreva seu código aqui

    return ok

# Função que recebe uma imagem PGM e cria
# uma versão espelhada da imagem.
def espelhaPGM(imagem,novaImagem):
    ok=True
    ## Escreva seu código aqui.
    
    return ok

# Função que recebe uma imagem PPM e cria
# uma versão rotacionada em 90 graus da imagem.
def rotaciona90PPM(imagem,novaImagem):
    ok=True
    ## Escreva seu código aqui.
    
    return ok
