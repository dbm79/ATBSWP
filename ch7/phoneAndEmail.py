
# phoneAndEmail.py - Finds phone numbers and emails addresses on the clipboard

import pyperclip
import re

phoneRegEx = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code
    (\s|-|\.)?                      # Seperator
    (\d{3})                         # First three digits
    (\s|-|\.)                       # Seperator
    (\d{4})                         # Last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

emailRegEx = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # Username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # Domain name
    (\.[a-zA-Z{2,4}])               # dot something 
    )''', re.VERBOSE)

# TODO: Find Mataches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegEx.findall(text):
    
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    
    if groups[8] != '':
        phoneNum += f' x {groups[8]}'
    matches.append(phoneNum)
print(matches)
# TODO: Copy results to clipboard