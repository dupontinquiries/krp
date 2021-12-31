import secrets
def randomString(stringLength=10):
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890!@&_'
    """Generate a random string of fixed length """
    l = len(letters)
    return ''.join(letters[secrets.randbelow(l)] for i in range(stringLength))

import sys
a = ''
while True:
    a = randomString(14 if len(sys.argv) < 2 else int(sys.argv[1]))
    x = input(f'{a} [y/n]')
    if x.lower() == 'y':
        break

import pyperclip
pyperclip.copy(a)
