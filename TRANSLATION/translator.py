# This exercise is to translate a file from ENG to JAP. Or your chosen preferred language.

# You need to install pip install translate, relating to what pip version you have installed on your machine.

# Import TRANSLATION module

# Code written by Nadeem Shah.

from translate import Translator

# Translate text to Japanese
translator = Translator(to_lang='ja')

# Use OPEN to read file content in Read Only Mode.

with open('translate.txt', mode='r') as my_file:

# Print translation with OPEN file in Read Only.

    print(translator.translate(open('translate.txt', mode='r').read()))

# Create a file and translate to Japanese

translator2 = Translator(to_lang='ja')

with open('translator2-ja.txt', mode='w') as my_file2:
    my_file2.write(translator2.translate('Nadeem Shah'))

