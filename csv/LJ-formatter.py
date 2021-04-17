import re
import os
import num2words

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

with open('transcript.csv', "w", encoding="utf-8") as f:
    for line in lineslist:
        decmark_reg = re.compile('(?<=\d),(?=\d)')

        comma_repl = decmark_reg.sub('',line.strip())

        normalized_sentence = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), str(comma_repl))
        f.write(f"{line.split('|')[0].replace('wavs/', '').replace('.wav', '').strip()}|{line.split('|')[1]}|{normalized_sentence.split('|')[1]}\n")
