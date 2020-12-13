from re import match

# Retorna um numero de acordo com as funções comentadas em uma lista de linhas
# e também adiciona o feedback às linhas do arquivo.
def requireCommentsBeforeEveryFunction(lines: list) -> int:
  score = 1
  feedback = []

  for i, line in enumerate(lines):
    result = match('^def.*(.*):.*$', line)
    if result is not None:
      if match('^#.*$', lines[i - 1]) is None:
        score = 0
        feedback.append(i)

  for idx in feedback:
    lines.insert(idx, '# FEEDBACK: Faltou um comentário aqui\n')

  return score

# Lista de requisitos disponíveis no sistema.
availableRequirements = [
  {
    'id': 'requireCommentsBeforeEveryFunction',
    'description': 'Toda função requer um comentário antes',
    'method': requireCommentsBeforeEveryFunction
  }
]
