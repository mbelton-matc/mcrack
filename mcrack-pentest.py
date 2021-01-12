#!/usr/bin/python

# A functional password cracker that demonstrates a dictionary attack
# usage: python mcrack-0.1.py `grep root /etc/shadow`

import sys
import crypt
from sys import argv

dictionary = '/PATH/TO/password.lst'

myName = sys.argv[0]
shadowGecos = sys.argv[1]
shadowHash = shadowGecos.split(':')[1]
position = shadowHash.rfind('$')
shadowSalt = shadowHash[:position]

def main():
        crackHash()

def crackHash():
    words = open(dictionary, 'r')
    for myGuess in words.readlines():
        myGuess = myGuess.rstrip('\n')
        challengeHash = crypt.crypt(myGuess, shadowSalt)
        if (challengeHash == shadowHash):
            print 'The password is:', myGuess
            sys.exit()

if __name__ == '__main__':
    main()
