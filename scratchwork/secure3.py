def generateCipher():
    # generating private key (RsaKey object) of key length of 1024 bits
    pr = RSA.generate(1024)
    # generating the PUBLIC KEY (RsaKey object) from the private key
    pu = pr.publickey()
    # only use the PUBLIC KEY to prevent decryption
    cipher = PKCS1_OAEP.new(pu)
    return cipher

# map a byte array to a usable password and return the password (passwordify the arr)
def trans(a, u='abcdefghijklmnopqrstuvwxyz1234567890!?@&^*-_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'):
    # the default list is predetermined, but any encryptable file could be read in here
    o = ''.join(list(map(lambda e: u[e % len(u)], a[:512])))
    return o

# make a new pw from phrase a and cipher c
def np(a, c):
    # encrypting the message with the PKCS1_OAEP object
    ba = c.encrypt(a)
    # return the password
    return trans(list(ba))

if __name__ == '__main__':
    #Importing necessary modules
    import logging
    from argparse import ArgumentParser
    import glob
    from os import path
    from cryptography.fernet import Fernet
    
    # key = Fernet.generate_key()
    # f = Fernet(key)
    # token = f.encrypt(b"my deep dark secret")
    # # print(f.decrypt(token))

    parser = ArgumentParser()
    parser.add_argument("-m", help="message")
    parser.add_argument("-k", help="\"path/to/key/file\"")
    args = parser.parse_args()
    m = args.m.encode('utf-8')
    k = args.k
    if k is None:
        k = 'key.txt'
    if m == 'k':
        c = Fernet.generate_key()
        with open(k, 'w') as hh:
            hh.write(str(c))
        print('new key: {0}'.format(c))
    else:
        c = None
        if path.exists(k):
            # read key
            with open(k, 'r') as hh:
                c = hh.read()[2:-1]
        else:
            c = Fernet.generate_key()
            with open(k, 'w') as hh:
                hh.write(str(c))
        print(f'\n  key = {c}\n\n  password: {str(Fernet(c).encrypt(m))[2:-1]}\n')
