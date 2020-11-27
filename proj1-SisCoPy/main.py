from cli import promptForLogin, promptForRequirementsAndWeights, promptForCommand
from preferences import preferences, updatePreferences

def main():
  try:
    print('SisCoPy - Sistema de Correção de projetos Python')
    print('')

    if preferences['requirementsAndWeights'] == None:
      print('Parece que é o seu primeiro acesso')
      preferences['requirementsAndWeights'] = promptForRequirementsAndWeights([])
      updatePreferences(preferences)
    
    # promptForLogin()
    while True:
      promptForCommand()

  except KeyboardInterrupt:
    exit(0)

if __name__ == '__main__':
  main()