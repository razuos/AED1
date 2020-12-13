from os import listdir
from re import match

availableNamingSchemes = [
  {
    'id': 'student',
    'order': ['student'],
    'description': 'ESTUDANTE.py',
    'regex': '^\w+$'
  },
  {
    'id': 'student-class',
    'order': ['student', 'class'],
    'description': 'ESTUDANTE-TURMA.py',
    'regex': '^\w+-\w+$'
  },
  {
    'id': 'student-class-activity',
    'order': ['student', 'class', 'activity'],
    'description': 'ESTUDANTE-TURMA-ATIVIDADE.py',
    'regex': '^\w+-\w+-\w+$'
  }
]

# Retorna uma lista de dicionários com os arquivos selecionados para correção.
def scan(path: str, namingScheme: dict)->list:

  results = []

  for file in listdir(path):
    fullPath = "{}/{}".format(path, file)

    if file.split('/')[-1].split('.')[-1] == 'py':
      strippedFilename = file.split('/')[-1].split('.')[0]

      if match(namingScheme['regex'], strippedFilename) != None:
        r = open(fullPath, 'r')
        lines = r.readlines()
        r.close()

        newFile = {
          'id': strippedFilename,
          'path': fullPath,
          'lines': lines
        }

        if '-' not in strippedFilename:
          splitted = [strippedFilename]
        else:
          splitted = list(reversed(strippedFilename.split('-')))

        for metadata in ['student', 'class', 'activity']:
          try:
            newFile[metadata] = splitted.pop()
          except IndexError:
            newFile[metadata] = 'N/A'

        results.append(newFile)

  return results

# print(scan('./test/examples', availableNamingSchemes[1]))