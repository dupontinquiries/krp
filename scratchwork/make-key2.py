import argparse
import secrets

def generateKey(u='abcdefghijklmnopqrstuvwxyz1234567890!?@&^*-_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'):
    return ''.join(u[secrets.randbelow(len(u))] for i in range(160))
    # encrypting the message with the PKCS1_OAEP object
    # ba = cipher.encrypt(a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-hh", help="path/to/file")
    args = parser.parse_args()
    with open(g.hh, 'w') as hh:
    	hh.write(generateKey())