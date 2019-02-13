#################################
#       MIDN Jacob A. Lindow    #
#          SY301 - HW05         #
#         CBC Decryption        #    
#################################
import os
import sys
from Crypto.Cipher import AES

#Get Key 
with open(sys.argv[1], 'rb') as keyFile: 
    key = keyFile.read()

#Get Cipher
with open(sys.argv[2], 'rb') as cipherFile:
    IV  = cipherFile.read(16) 
    c   = cipherFile.read()

#Decrypt Message
aes = AES.new(key, AES.MODE_CBC, IV) 
msg = aes.decrypt(c)

#Strip padding
padSize = msg[-1]
msg = msg[:-padSize]

with open(sys.argv[3], 'wb') as plainText:
    plainText.write(msg)

