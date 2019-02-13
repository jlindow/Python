import sys
from Crypto.Cipher import AES

#Get key from key.txt
with open(sys.argv[1], 'rb') as keyFile: 
    key = keyFile.read()

#Get cipher text from cipher.bin
with open(sys.argv[2], 'rb') as cipherFile: 
    r   = cipherFile.read(16) 
    c = cipherFile.read(16)


#Get block by reproducing random number r
aes = AES.new(key, AES.MODE_ECB)
block = aes.encrypt(r)

#XOR "random" block with CIPHERTEXT to get MSG 
msg = bytearray(len(c))
for i in range(len(c)): 
    msg[i] = block[i]^c[i]

#write to msg.txt
with open(sys.argv[3], 'wb') as msgFile: 
    msgFile.write(msg)


