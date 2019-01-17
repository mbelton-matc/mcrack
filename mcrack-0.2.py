root@lab-matc-00:/home/no6/pass-crack-0.1/matc-crack/delivery# vi matc-crack-0.2.py
#!/usr/bin/python

# A functional password cracker to demonstrate a dictionary attack
# Processes a set of GECOS fields from /etc/shadow
#
# usage: python matc-crack.py `grep root /etc/shadow`

import sys
import os
import crypt
from sys import argv

dictionary = '/usr/share/john/password.lst'

myName = sys.argv[0]
shadowGecos = sys.argv[1]
shadowHash = shadowGecos.split(':')[1]
position = shadowHash.rfind('$')
shadowSalt = shadowHash[:position]

def main():
    print '\n[ Madison College Password Cracker Demo ]\n'
    crackHash()

def crackHash():
    print '[ TARGET HASH ]', shadowHash, '\n'
    if os.access(dictionary, os.F_OK):
        words = open(dictionary, 'r')
        passFound = False
        counter = 0
        for myGuess in words.readlines():
            myGuess = myGuess.rstrip('\n')
            challengeHash = crypt.crypt(myGuess, shadowSalt)
            if (challengeHash == shadowHash):
                passFound = True
                print '\n\n[ PASSWORD FOUND ] The password is:', myGuess
                print '[ PASSWORD FOUND ] I processed', counter, 'lines from', dictionary, '\n'
                sys.exit()
            if (passFound == False):
                sys.stdout.write('|')
                sys.stdout.flush()
                counter = counter + 1
    else:
        print 'Password dictionary not found', dictionary
        sys.exit()


if __name__ == '__main__':
    main()
