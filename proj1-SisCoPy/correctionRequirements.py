from re import match

# Retorna uma float de acordo com a porcentagem de funções comentadas em uma lista de linhas
# e também adiciona o feedback às linhas do arquivo.
def requireCommentsBeforeEveryFunction(lines: list):
  totalDefs = 0
  commentsBeforeDefs = 0
  feedback = []

  for i, line in enumerate(lines):
    result = match('^def.*(.*):.*$', line)
    if result is not None:
      totalDefs += 1
      if match('^#.*$', lines[i - 1]) is not None:
        commentsBeforeDefs += 1
      else:
        feedback.append(i)

  # print(totalDefs)
  # print(commentsBeforeDefs)
  # print(feedback)

  for idx in feedback:
    lines.insert(idx, '# FEEDBACK: Faltou um comentário aqui\n')

  if totalDefs == 0: return 1.0
  if commentsBeforeDefs == 0: return 0.0
  return commentsBeforeDefs / totalDefs

# f = open('./test/examples/1.py', 'r')
# lines = f.readlines()
# f.close()

# requireCommentsBeforeEveryFunction(lines)

# fout = open('./out.py', 'w')
# fout.writelines(lines)
