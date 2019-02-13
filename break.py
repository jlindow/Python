# Break's a Caesar Shift Cipher
import sys 

ciphertext = sys.argv[1] 

for k in range(0, 26):
    plaintextlist = []
    for i in range(len(ciphertext)):
        char_num    = ord(ciphertext[i]) - 65  #map to 0 - 25
        shifted_num = (char_num - k) % 26
        plainletter = chr(shifted_num + 65) 
        plaintextlist.append(plainletter)
    
    plaintextstring = ''.join(plaintextlist)
    print("k = " + str(k) +  " :  " + plaintextstring) 




