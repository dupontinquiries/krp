#Importing necessary modules
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
from sys import argv

def generateKey():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the public key (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the public key to prevent decryption
    return pu.export_key().decode().replace('\n', '').replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----', '')

def generateRSA():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the public key (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the public key to prevent decryption
    return pu

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

# save key a in a file at h using password o
def sk(a, h='public_pem.pem', o=None):
    if o is None:
        try:
            print(f'saving key {a[:5]}...')
            with open(h, 'w') as hh:
                hh.write(a)
                return True
        except Exception:
            return False
    elif len(o) > 3:
        try:
            print(f'saving key {a[:5]}... with pass {o}')
            n = hashlib.sha3_512(o.encode('utf-8')).hexdigest()[:128]
            with open (h, 'w') as hh:
                hh.write(a)
                return True
        except Exception:
            return False
    else:
        print('an error occured when trying to save a key')
        return False

# read a message from a file at h using password o
def rwa(h, o=None):
    if o is None:
        try:
            print(f'reading key at {h[:5]}...')
            with open(h, 'r') as hh:
                return hh.read()[25:247]
        except Exception:
            return False
    elif len(o) > 3:
        try:
            print(f'reading key at {h[:5]}... with pass {o}')
            n = hashlib.sha3_512(o.encode('utf-8')).hexdigest()[:128]
            with open (h, 'r') as hh:
                return hh.read()
        except Exception:
            return False
    else:
        print('an error occured when trying to save a key')
        return False

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
    #print(sk(k.export_key().decode(), 'key.txt'))
    #print(rwa('key.txt'))
    # print(sk(generateKey().export_key().decode(), 'key.txt', 'file-password'))