from preferences import preferences
from correctionRequirements import availableRequirements

def correct(file):
  reader = open(file, 'r')
  lines = reader.readlines()
  reader.close()

  feedbackFilename = "{}.feedback".format(file)
  feedbackWriter = open(feedbackFilename, 'w')

  for i, correctionStep in enumerate(preferences['requirementsAndWeights']):
    # print('Rodando passo de correção: {}'.format(correctionStep['requirementId']))
    # print('peso: {}'.format(correctionStep['weight']))
    method = next(requirement['method'] for requirement in availableRequirements if correctionStep['requirementId'] == requirement['id'])
    method(lines)
    feedbackWriter.writelines(lines)
  
  feedbackWriter.close()
    
correct('./test/examples/1.py')
