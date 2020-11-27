from json import loads, dumps

filename = './preferences.json'

preferences = {
  'requirementsAndWeights': None,
  'namingScheme': None
}

f = open(filename, 'a+')
f.seek(0)
contents = f.read()

if len(contents) == 0:
  f.write(dumps(preferences))
else:
  preferences = loads(contents)

f.close() 

def updatePreferences(preferences):
  f = open(filename, 'w')
  f.write(dumps(preferences))
  f.close()
