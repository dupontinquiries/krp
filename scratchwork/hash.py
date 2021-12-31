import secrets

def randomString(stringLength=256):
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890!?@&_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'
    """Generate a random string of fixed length """
    l = len(letters)
    return ''.join(letters[secrets.randbelow(l)] for i in range(stringLength))

from sys import argv
# from Crypto.Hash import SHA3_512 #pip install pycryptodome

import hashlib

p = 'password'

# ho = SHA3_512.new(data=p)

# n = ho.hexdigest()

n = hashlib.sha3_512(p.encode('utf-8')).hexdigest()

print(f'Results:\nkey: SHA3_512\nlock: {p}\npassword: {n}')