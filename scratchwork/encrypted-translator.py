
# map a byte array to a usable password and return the password (passwordify the arr)
def trans(a, u='abcdefghijklmnopqrstuvwxyz1234567890!?@&^*-_,.:;<>YFGCRLAOEUIDHTNSQJKXBMWVZ'):
    # the default list is predetermined, but any encryptable file could be read in here
    o = ''.join(list(map(lambda e: u[e % len(u)], a)))
    return o

p = 'password2258'

secret = ''
with open('key5.txt', 'r') as hh:
    secret = hh.read()

# make password 512 characters
# p = p + (512 - len(p)) * ' '


# get hex of password
import codecs
# h = list(map(lambda c: codecs.encode(c, 'hex'), p.encode('hex')))
h = p.encode('utf-8').hex()

# print(h)

print(''.join(list(map(lambda e: secret[int(e,16)], h))))



# translator = ''
# with open('trans.txt', 'r') as hh:
#     translator = hh.read()

# print(password, trans(secret.encode('utf-8'))[:25])
# print()
#print(password, trans(secret.encode('utf-8'))[:25])