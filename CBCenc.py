#############################
#   MIDN Jacob A. Lindow    #
#   SY301 - HW05            #
#   CBC Encryption          #
#############################

import sys
import os
from Crypto.Cipher import AES

#Get Key 
k = open(sys.argv[1], 'rb').read()
key = bytearray(k) 

#Get Message
m = open(sys.argv[2], 'rb').read()
msg = bytearray(m) 

#Create IV 
IV = bytearray(os.urandom(16))

#Pad Message
padSize = (16 - len(msg)) % 16
for _ in range(padSize):
    msg.append(padSize)

#Encrypt Message
aes     = AES.new(key, AES.MODE_CBC, IV)
cipher  = aes.encrypt(msg) 

#Output Cipher Text
with open(sys.argv[3], 'wb') as cipherFile: 
        cipherFile.write(IV + cipher) 
