# MIDN Jacob A. Lindow 
# SY308 - HW04

###############################################################################
#    - NOT CRYPTOGRAPHICALLY SECURE  *** DO NOT USE FOR SECURE ENCRYPTION -   #
###############################################################################
import sys
import os
from Crypto.Cipher import AES

#Get key from key.txt
key = open(sys.argv[1], 'rb').read()

#Get message from msg.txt
msg = open(sys.argv[2], 'rb').read() 

#Create block using cipher F(r), where r is random number, with key k
aes = AES.new(key, AES.MODE_ECB)
r = os.urandom(16)
block = aes.encrypt(r)

#XOR BLOCK with MSG
encMsg = [block[i]^msg[i] for i in range(len(msg))]

#write to cipher.bin
with open(sys.argv[3], 'wb') as cipherFile: 
    cipherFile.write(r + encMsg) 

