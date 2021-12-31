import argparse
import sys
import hashlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-hh", help="path/to/key-file")
    parser.add_argument("-p", help="phrase")
    g = parser.parse_args()
    
    p = g.p

    secret = ''
    with open(g.hh, 'r') as hh:
        secret = hh.read()

    # create a sha3 hash object
    hash_sha3_512 = hashlib.new("sha3_512", p.encode('utf-8'))

    # use hex numbers to get indicies from secret
    t = (''.join(list(map(lambda e: secret[int(e,16)], hash_sha3_512.hexdigest()))))

    print(f'password: {t[:64]}')
