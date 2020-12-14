from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator
from re import match
from scan import availableNamingSchemes, scan
from settings import settings
from preferences import preferences, updatePreferences
from requirements import availableRequirements
from correction import correct, exportToCSV

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
def promptForRequirementsAndWeights()->list:
  print("Selecione os requisitos e seus respectivos pesos.\n")

  for i, requirement in enumerate(availableRequirements, start=1):
    print("{} - {}".format(i, requirement['description']))

  print("\nDigite o número do requisito seguido por uma vírgula e seu peso, terminando com ponto e vírgula.")
  print("Por exemplo: 1,1;3,5. O requisito 1 terá peso 1 e o requisito 3 terá peso 5.")

  userPromptResult = prompt("", validator=reqsAndWeightsValidator, validate_while_typing=True)
  userInput = [ selection.split(',') for selection in userPromptResult.split(';')]

  selected = []
  for selection in userInput:
    try:
      index = int(selection[0]) - 1
      weight = int(selection[1])

      requirement = availableRequirements[index]

      selected.append({
        'requirementId': requirement['id'],
        'weight': weight
      })
    except IndexError:
      print('Índice {} inválido, ignorando.'.format(index))

  preferences['requirementsAndWeights'] = selected
  updatePreferences(preferences)

  print("Preferências atualizadas com sucesso.")

# Valida a entrada utilizada na função promptForNamingScheme
namingSchemeValidator = Validator.from_callable(
  lambda input: match('^[1-3]$', input),
  error_message="Esquema inválido",
  move_cursor_to_end=True,
)

def promptForNamingScheme() -> dict:
  print("Selecione um entre os esquemas de nomes")

  for i, namingScheme in enumerate(availableNamingSchemes, start=1):
    print("{} - {}".format(i, namingScheme['description']))

  userInput = prompt("Opção: ", validator=namingSchemeValidator, validate_while_typing=True)

  selected = availableNamingSchemes[int(userInput) - 1]
  
  preferences['namingScheme'] = selected
  updatePreferences(preferences)

  print("Preferências atualizadas com sucesso.")

def promptForCommand():
  commands_completer = WordCompleter(dict.keys(commands))
  command = prompt("$ -> ", completer=commands_completer, history=FileHistory('./history'))
  if command not in commands:
    print('Comando inválido, utilize o comando \'ajuda\' para obter ajuda.')
  else:
    commands[command]['method']()

# Valida a entrada utilizada na função promptForRequirementsAndWeights
confirmationValidator = Validator.from_callable(
  lambda input: match('^[SN]{1}$', input),
  error_message="Escolha inválida",
  move_cursor_to_end=True,
)
def promptForConfirmation(message: str)->bool:
  choice = prompt("{} (S/N): ".format(message), validator=confirmationValidator, validate_while_typing=True)
  if choice == 'S': return True
  return False

def ajuda():
  for key in dict.keys(commands):
    print("{}: {}".format(key, commands[key]['helpText']))

def corrigir():
  files = scan('./projetos', preferences['namingScheme'])
  print("Corrigindo {} arquivo(s) válidos.".format(len(files)))
  export = promptForConfirmation('Deseja exportar a correção para CSV?')
  files = correct(files)
  if export: 
    exportToCSV(files)
  else:
    for file in files:
      print("{}: Nota {}".format(file['id'], file['score']))
  print("Correção efetuada com sucesso!")

commands = {
  'ajuda': {
    'helpText': 'Mostra os comandos do sistema',
    'method': ajuda
  },
  'pesos': {
    'helpText': 'Seleciona os requisitos e pesos para a correção',
    'method': promptForRequirementsAndWeights
  },
  'nomenclatura': {
    'helpText': 'Seleciona a nomenclatura dos arquivos utilizados para a correção',
    'method': promptForNamingScheme
  },
  'corrigir': {
    'helpText': 'Corrige os arquivos no diretório \'projetos\' de acordo com as suas preferências.',
    'method': corrigir
  },
}