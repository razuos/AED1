from preferences import preferences
from requirements import availableRequirements
from scan import scan
import csv

def correct(files):

  for file in files:
    # print(dict.keys(file))
    lines = file['lines']

    feedbackFilename = "./feedback/{}.py".format(file['id'])
    feedbackWriter = open(feedbackFilename, 'w')

    scores = []
    for i, correctionStep in enumerate(preferences['requirementsAndWeights']):
      # print('Rodando passo de correção: {}'.format(correctionStep['requirementId']))
      # print('peso: {}'.format(correctionStep['weight']))
      method = next(requirement['method'] for requirement in availableRequirements if correctionStep['requirementId'] == requirement['id'])
      score = method(lines)
      scores.append(score)
      feedbackWriter.writelines(lines)
  
    feedbackWriter.close()

    weights = [ d['weight'] for d in preferences['requirementsAndWeights']]
    totalWeight = sum(weights)
    totalScores = 0

    for i, score in enumerate(scores):
      totalScores += weights[i]*score
    
    file['score'] = (totalScores / totalWeight) * 10.0

  return files

def exportToCSV(files):
  with open('scores.csv', 'w') as csvFile:
    fieldnames = ['id', 'aluno', 'turma', 'atividade', 'nota']
    writer = csv.DictWriter(csvFile, dialect='excel', fieldnames = fieldnames)
    writer.writeheader()
    for file in files:
      writer.writerow({
        'id': file['id'],
        'aluno': file['student'],
        'turma': file['class'],
        'atividade': file['activity'],
        'nota': file['score'],
      })
