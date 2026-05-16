#!/usr/bin/env python3

""" This program read account name that user types in the terminal
    and the password of that accound will be copied to the clipboard 
    automaticly
"""

import sys, pyperclip

passwords = {
    'email' : ';hag;h23445',
    'blog'  : 'ahagh514'

}


if len(sys.argv) < 2:
    print('Usage: python password_locker.py[account] - copy acount password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'there is no account named {account}')











