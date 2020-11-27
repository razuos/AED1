from cli import promptForLogin, promptForRequirementsAndWeights, promptForCommand, promptForNamingScheme
from correctionRequirements import availableRequirements
from preferences import preferences, updatePreferences
from scanner import availableNamingSchemes

def main():
  try:
    print('SisCoPy - Sistema de Correção de projetos Python\n')

    promptForLogin()
    
    if preferences['requirementsAndWeights'] == None:
      print('*--------------------------------------*')
      print('| Bem-vindo(a) ao seu primeiro acesso! |')
      print('*--------------------------------------*\n')
      preferences['requirementsAndWeights'] = promptForRequirementsAndWeights(availableRequirements)
      preferences['namingScheme'] = promptForNamingScheme(availableNamingSchemes)
      updatePreferences(preferences)
    
    while True:
      promptForCommand()

  except KeyboardInterrupt:
    exit(0)

if __name__ == '__main__':
  main()