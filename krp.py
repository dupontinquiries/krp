import random
def randomString(stringLength=10):
    string = 'abcdefghijklmnopqrstuvwxyz1234567890!@&_'
    """Generate a random string of fixed length """
    letters = string
    return ''.join(random.choice(letters) for i in range(stringLength))

a = ''
while True:
    a = randomString(14)
    x = input(f'{a} [y/n]')
    if x.lower() == 'y':
        break

import subprocess
subprocess.run("pbcopy", universal_newlines=True, input=a)
