from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
from sys import argv
import secrets

def generateKey(u='abcdefghijklmnopqrstuvwxyz1234567890!?@&^*-_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'):
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the public key (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the public key to prevent decryption
    o = pu.export_key().decode().replace('\n', '').replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----', '')
    cipher = PKCS1_OAEP.new(key=o)
    return cipher.encrypt( ''.join(secrets.choice(u) for i in range(50)) )
    # encrypting the message with the PKCS1_OAEP object
    # ba = cipher.encrypt(a)

with open('key5.txt', 'w') as hh:
	hh.write(generateKey())