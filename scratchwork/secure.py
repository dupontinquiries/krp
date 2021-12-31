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

# make a new pw from phrase a and key object o
def npfk(a, o):
    cipher = PKCS1_OAEP.new(key=o)
    # encrypting the message with the PKCS1_OAEP object
    ba = cipher.encrypt(a)
    # return the password
    return trans(list(ba))

# make a new pw from phrase a and key o
def np(a, o):
    # first convert the string into an RSA key object
    o = RSA.import_key(f'-----BEGIN PUBLIC KEY-----\n{o}\n-----END PUBLIC KEY-----')
    cipher = PKCS1_OAEP.new(o)
    # encrypting the message with the PKCS1_OAEP object
    ba = cipher.encrypt(a)
    # return the password
    return trans(list(ba))

# save key a in a file at h using password o
def sk(a, h='public_pem.pem', o=None):
    if o is None:
        try:
            logging.debug(f'saving key {a[:5]}...')
            with open(h, 'w') as hh:
                hh.write(a)
                return True
        except Exception:
            return False
    elif len(o) > 3:
        try:
            logging.debug(f'saving key {a[:5]}... with pass {o}')
            n = hashlib.sha3_512(o.encode('utf-8')).hexdigest()[:128]
            with open (h, 'w') as hh:
                hh.write(a)
                return True
        except Exception:
            return False
    else:
        logging.debug('an error occured when trying to save a key')
        return False

# read a message from a file at h using password o
def rwa(h, o=None):
    if o is None:
        try:
            logging.debug(f'reading key at {h[:5]}...')
            with open(h, 'r') as hh:
                return hh.read().replace('\n', '').replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----', '')
        except Exception:
            return False
    elif len(o) > 3:
        try:
            logging.debug(f'reading key at {h[:5]}... with pass {o}')
            n = hashlib.sha3_512(o.encode('utf-8')).hexdigest()[:128]
            with open (h, 'r') as hh:
                return hh.read()
        except Exception:
            return False
    else:
        logging.debug('an error occured when trying to save a key')
        return False

if __name__ == '__main__':
    #Importing necessary modules
    import logging
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from binascii import hexlify
    from argparse import ArgumentParser
    import glob
    from os import path
    parser = ArgumentParser()
    parser.add_argument("-m", help="message")
    parser.add_argument("-k", help="\"path/to/key/file\"")
    args = parser.parse_args()
    m = args.m.encode('utf-8')
    k = args.k
    if k is None:
        k = 'key.txt'
    if m == 'k':
        c = generateKey()
        sk(c, k)
        print('new key: {0}'.format(c))
    else:
        c = None
        if path.exists(k):
            # read key
            c = rwa(k)
        else:
            c = generateKey()
            sk(f'-----BEGIN PUBLIC KEY-----\n{c}\n-----END PUBLIC KEY-----', k)
        print(f'\nkey = {c}\n')
        print('\npassword: {0}\n'.format(np(m, c)))