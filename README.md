# mcrack

Madison College Crack

A functional password cracker that demonstrates a dictionary attack. Input is a GECOS line that contains a password hash.

sample usage: python mcrack-0.1.py \`grep USERNAME /etc/shadow\`

Two versions are available:

mcrack-pentest.py : The penetration tester's version. Light and portable with minimal I/O.

mcrack-mgmt.py : The manager's version. Output includes metrics related to LoE (Level of Effort) and more.

