def generateKey():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the PUBLIC KEY (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the PUBLIC KEY to prevent decryption
    return pu.export_key().decode().replace('\n', '').replace('-----BEGIN PUBLIC KEY-----', '').replace('-----END PUBLIC KEY-----', '')

def generateRSA():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the PUBLIC KEY (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the PUBLIC KEY to prevent decryption
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
            with open(k, 'r') as hh:
                c = hh.read()
        else:
            c = generateKey()
            with open(k, 'w') as hh:
                hh.write(c)
        print(f'\nkey = {c}\n')
        print('\npassword: {0}\n'.format(np(m, c)))