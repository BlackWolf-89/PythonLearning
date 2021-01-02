
# with open('new.txt', mode='a') as my_file:
#   my_file.write('This is new file \n')
#   my_file.write('This is second line \n')

# tex = 'nujmber|test|range|value'
# print(tex.split('|')[2])

from translate import Translator

with open('test.txt', mode='r') as inputFile:
  text1 = inputFile.read()
  translator = Translator(to_lang = "es")
  result = translator.translate(text1)
  print(result)

  with open('result.txt', mode='w') as outputFile:
    outputFile.write(result)