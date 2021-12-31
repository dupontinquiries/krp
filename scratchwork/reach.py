import secrets
from sys import argv
import hashlib

def randomString(stringLength=256):
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890!?@&_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'
    """Generate a random string of fixed length """
    l = len(letters)
    return ''.join(letters[secrets.randbelow(l)] for i in range(stringLength))


p = 'hold-insth-2905!a'

#make private and public key, encrypt message, and then (poc) decrypt message using private key
#can use public key across all devices??

print(f'Results:\nkey: SHA3_512\nlock: {p}\npassword: {n}')