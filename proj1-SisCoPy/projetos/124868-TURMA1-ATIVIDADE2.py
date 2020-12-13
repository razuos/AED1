import re

# comentario
def testMe():
  pass

def testMe2():
  pass

def invalid()

def invalid2

invalid3():

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')import re
