#################################
#        MIDN Jacob A. Lindow   #
#        HW05                   #
#        SY301                  #
#        PART 3                 #
#################################

#Imports
import sys
import os 
from Crypto.Cipher import AES

with open(sys.argv[1], 'wb') as keyFile: 
        key = os.urandom(16)
        keyFile.write(key) 
