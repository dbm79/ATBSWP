#! python3
# mcb.py Saves and loads pieces of text to the clipboard
# Usage:
# python mcb.py save <keyword> - Saves clipboard to keyword
# python mcb.py <keyword> - Loads keyword data to clipboard
# python mcb.py list - Lists all of the stored keywords

import shelve, sys, pyperclip

try:
    mcb_db = shelve.open('mcb.db')
except IOError as e:
    print(f'File cannot be accessed')

# TODO Save clipboard content
if len(sys.argv) <= 1:
    print('''Usage:
    python mcb.py save <keyword> - Saves clipboard to keyword
    python mcb.py <keyword> - Loads keyword data to clipboard
    python mcb.py list - Lists all of the stored keywords''')

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_db[sys.argv[2].lower()] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        for key in mcb_db.keys():
            print(f'- {key}')
    else:
        try:
            print( mcb_db[sys.argv[1].lower()] )
            pyperclip.copy( mcb_db[sys.argv[1].lower()] )
        except KeyError as e:
            print('Entry not found in database')

# TODO List Keywords and Load content

mcb_db.close()