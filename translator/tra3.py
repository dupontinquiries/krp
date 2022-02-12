import argparse
import sys
import hashlib

if __name__ == '__main__':
    ps = argparse.ArgumentParser()
    ps.add_argument('-hh', help='path/to/key-file')
    ps.add_argument('-p', help='phrase')
    ps.add_argument('-s', help='encryption key salt')
    g = ps.parse_args()
    
    p = g.p

    secret = ''

    if g.s is not None:
        secret += str(g.s)

    with open(str(g.hh), 'r') as hh:
        secret += hh.read()

    # create a sha3 hash object
    hash_sha3_512 = hashlib.new('sha3_512', p.encode('utf-8'))

    # use hex numbers to get indicies from secret
    # t = (''.join(list(map(lambda e: secret[int(e,16)], hash_sha3_512.hexdigest()))))

    # print(str(hash_sha3_512.hexdigest()))

    t = ''

    for i, c in enumerate(str(hash_sha3_512.hexdigest())):
        # print(f"{i}: {str(c)}")
        # 244031501853741146277593991413
        aa = 9023517408979729987201486445741636684893 % ( (2 ** i) + int(c,16) )
        aa = (2 ** i) + int(c,16)
        # aa = (31 ** i) + int(c,16)
        bb = aa
        # print( aa )
        t += secret[ aa % len(secret) ]
        # t += secret[ len(secret) % aa ]

    print(t[:64])

    # t = (''.join(list(map( lambda i, c: secret[ ( (31 ** i) * int(c,16) ) % len(secret) ], enumerate(str(hash_sha3_512.hexdigest())) )))

    # print(f'password: {t[:64]}')
