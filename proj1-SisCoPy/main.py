from prompts import promptForLogin, promptForCommand, promptForRequirementsAndWeights, promptForNamingScheme
from preferences import preferences

def main():
  try:
    print('SisCoPy - Sistema de Correção de projetos Python\n')

    promptForLogin()

    print('')
    
    if preferences['requirementsAndWeights'] == None:

      print('*--------------------------------------*')
      print('| Bem-vindo(a) ao seu primeiro acesso! |')
      print('*--------------------------------------*\n')

      promptForRequirementsAndWeights()
      promptForNamingScheme()
      
    else:

      print('*------------------------*')
      print('| Bem-vindo(a) de volta! |')
      print('*------------------------*\n')
    
    while True:
      promptForCommand()

  except KeyboardInterrupt:
    exit(0)

if __name__ == '__main__':
  main()