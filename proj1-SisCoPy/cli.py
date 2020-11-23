from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.validation import Validator
from re import match
from settings import settings

# Bloqueia até o usuário acertar as credenciais de acesso
def promptForLogin():
  user = prompt("usuário: ")
  password = prompt("senha: ", is_password=True)

  if (user != settings["username"]) or (password != settings["password"]):
    print("Nome de usuário ou senha incorretos")
    promptForLogin()

# Valida a entrada utilizada na função promptForRequirementsAndWeights
reqsAndWeightsValidator = Validator.from_callable(
  lambda input: match('^(\d+,\d+(;|))+$', input),
  error_message="Requisitos e pesos inválidos",
  move_cursor_to_end=True,
)

# Retorna uma lista com os requisitos e pesos selecionados
def promptForRequirementsAndWeights(requirements: list)->list:
  print("Selecione os requisitos e seus respectivos pesos.")

  for i, requirement in enumerate(requirements, start=1):
    print("{} - {}".format(i, requirement))

  print("Digite o número do requisito seguido por uma vírgula e seu peso, terminando com ponto e vírgula.")
  print("Por exemplo: 1,1;3,5. O requisito 1 terá peso 1 e o requisito 3 terá peso 5.")

  userPromptResult = prompt("", validator=reqsAndWeightsValidator, validate_while_typing=True)
  userInput = [ selection.split(',') for selection in userPromptResult.split(';')]

  selected = []
  for selection in userInput:
    try:
      index = int(selection[0]) - 1
      weight = int(selection[1])

      requirement = requirements[index]

      selected.append([requirement, weight])
    except IndexError:
      print('Índice {} inválido, ignorando.'.format())
  
  return selected

# def normalPrompt():
#   return prompt("$ -> ",
#     history=FileHistory("history"),
#     auto_suggest=AutoSuggestFromHistory())
