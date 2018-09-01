#!bin/python3
# bulletPointAdd.py - this will copy contents of the clipboard and add MD bullet points to each line

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)