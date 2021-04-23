import re
import os
import num2words
import unicodedata

lang = ''

print('\nSUPPORTED LENGUAGES: English, Spanish, French, German, Italian, Japanese, Russian, Arabic')
lang_input = input('What lenguage is spoken in your audios?: ')

if lang_input.strip().lower() == 'english':
    lang = 'en'
elif lang_input.strip().lower() == 'spanish':
    lang = 'es'
elif lang_input.strip().lower() == 'french':
    lang = 'fr'
elif lang_input.strip().lower() == 'german':
    lang = 'de'
elif lang_input.strip().lower() == 'italian':
    lang = 'it'
elif lang_input.strip().lower() == 'japanese':
    lang = 'ja'
elif lang_input.strip().lower() == 'russian':
    lang = 'ru'
elif lang_input.strip().lower() == 'arabic':
    lang = 'ar'

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

file = open('list.txt')

lineslist = []

# create file object
file1 = open('list_corrected.txt', "w+")

# read all lines
lines = file.readlines()

# traverse through lines one by one
for line in lines:
    lineslist.append(line.strip())

# close file
file1.close()

with open('transcript.csv', 'w+', encoding='utf-8') as f:
    for line in lineslist:
        decmark_reg = re.compile('(?<=\d),(?=\d)')

        comma_repl = decmark_reg.sub('',line.strip())

        normalized_sentence = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0)), lang=lang), str(comma_repl))
        final_line = f"{line.split('|')[0].replace('wavs/', '').replace('.wav', '').strip()}|{line.split('|')[1]}|{normalized_sentence.split('|')[1]}\n"
        
        final_line = strip_accents(final_line)

        f.write(final_line)
