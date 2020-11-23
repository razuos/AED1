from cli import promptForLogin, promptForRequirementsAndWeights

def main():
  try:
    print("SisCoPy - Sistema de Correção de projetos Python")

    promptForLogin()

    print(promptForRequirementsAndWeights(['teste1', 'teste2', 'teste3']))

  except KeyboardInterrupt:
    exit(0)

if __name__ == '__main__':
  main()