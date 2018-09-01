#!/usr/bin/python3
# pw.py - An Insecure password lockier program

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print(f'Usage: pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # The first command-line argument is the account

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard')
else:
    print(f'The account: {account} does not exist.')