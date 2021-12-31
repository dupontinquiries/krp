#Importing necessary modules
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
from sys import argv
import argparse

def generateKey():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the public key (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the public key to prevent decryption
    return pu.export_key().decode().replace('\n', '').replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----', '')

def generateRSAKey():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the public key (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the public key to prevent decryption
    return pu

def generateRSACypher(k):
    #Instantiating PKCS1_OAEP object with the public key for encryption
    c = PKCS1_OAEP.new(key=k)
    return c

# map a byte array to a usable password and return the password (passwordify the arr)
def trans(a, u='abcdefghijklmnopqrstuvwxyz1234567890!?@&^*-_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'):
    # the default list is predetermined, but any encryptable file could be read in here
    o = ''.join(list(map(lambda e: u[e % len(u)], a[:512])))
    return o

# make a new pw from phrase a and key o
def np(a, o):
    cipher = PKCS1_OAEP.new(key=o)
    # encrypting the message with the PKCS1_OAEP object
    ba = cipher.encrypt(a)
    # return the password
    return trans(list(ba))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="message")
    parser.add_argument("-k", help="path to key file")
    # parser.add_argument("-p", help='key file password')
    args = parser.parse_args()
    # the message to be encrypted
    message = 'TestPass123_!@'.encode('utf-8')
    # print(generateKey())
    k = generateKey()
    print(k)
    c = generateRSACypher(k)
    print(c)
    print(c.encrypt(message))
    #print(sk(k.export_key().decode(), 'key.txt'))
    #print(rwa('key.txt'))
    # print(sk(generateKey().export_key().decode(), 'key.txt', 'file-password'))