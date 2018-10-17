# MIDN 3/C Jacob Lindow
# Dr. Allen Parrish
# SY201
#
# "Caesar Cipher Decryption"
#
# Python v3.0

################################################################################
def GetNextCipher(Cipherstring):
    EntireCipherString = cipherstring["file"]
    DecryptedChar = ""
    if cipherstring["head"] == len(EntireCipherString):
        return("")
    else:
        try:
            while EntireCipherString[cipherstring["head"]] != "%":
                DecryptedChar += EntireCipherString[cipherstring["head"]]
                cipherstring["head"] += 1
            cipherstring["head"] += 1
            return(DecryptedChar)
        except IndexError:
            return(" ")

################################################################################
def CipherToPlain(cipher, offset):
    try:
        c = int(cipher) #This will raise an error if cipher is a special char, so try will be used for numbers, and except will be used for characters
    except:
        if cipher == "":
            return("")
        if cipher == " ":
            return(" ")
        if cipher == "\n":
            return("\n")
        c = ord(cipher)
        if c == 46:
            return(".")
        if c == 32:
            return(" ")
    if c < 0:
        c = c - int(offset)
        return(chr(abs(c)+64)) #Uppercase Letters

    elif c <=64 and c >=58: #special chars are spaces
        return(32)

    elif cipher == "%": #ignore percent signs
        return("")

    else:
        c = c - int(offset)
        return(chr(c+96)) #Lowercase Leters

################################################################################
def PrintLine(Cipherstring, num):
    CharToDecrypt = ""
    DecryptedChar = ""
    string = ""
    for x in range(0,30):
        CharToDecrypt = GetNextCipher(cipherstring)
        DecryptedChar = CipherToPlain(CharToDecrypt, num)
        if DecryptedChar == 32:
            string += " "
        else:
            string += str(DecryptedChar)
    print(str(num) + ") " + str(string))
################################################################################
def StartFromBeginning(Cipherstring):
    Cipherstring["head"]= 0
################################################################################
def OpenFile(RW):
    valid = ""
    #Loop will continue to run until user inputs a valid file name
    while valid == "":
        try:
            if RW == "r":
                InOrOut = "input"
            else:
                InOrOut = "output"
            FiletoOpen = input("Enter an " + InOrOut + " file name: ")
            F = open(FiletoOpen, RW)
            return(F)
            valid = "quit loop"
        except:
            print("File not Found. Please enter a valid file name.")
################################################################################
def GetValidR():
    valid = ""
    while valid == "":
        try:
            R = input("Enter a rotational value R: ")
            while R.isdigit == False or int(R) < 1 or int(R) > 10:
                print("Invalid rotation factor. Must be an integer between 1 and 10.")
                R = input("Enter a rotational value R: ")
                if R.isdigit == True and int(R) > 1 and int(R) < 10:
                    return(R)
                    valid = "quit loop"
                    break
            return(R)
            valid = "quit loop"
        except:
            print("Invalid rotation factor. Must be an integer between 1 and 10.")
################################################################################
#MAIN PROGRAM
################################################################################

f1 = OpenFile("r")
f2 = OpenFile("w")
cipherstring = {"head": 0, "file": str(f1.read())}

try:
    #Print the 10 possiblities for R values 1-10.
    for num in range(1,11):
        StartFromBeginning(cipherstring)
        PrintLine(cipherstring, num)
        StartFromBeginning(cipherstring)

        #Ask the user which value is correct
    R = GetValidR()

        #Loop runs while "head" is not equal to the length of the input file.
    while cipherstring["head"] != len(cipherstring["file"]):

            #Get the character to decrypt, and then decrypt using the user chosen "R" value.
        char = GetNextCipher(cipherstring)
        DecryptChar = CipherToPlain(str(char), R)

            #If statement writes a space into the file, otherwise it simply writes the decrypted character into the file.
        if DecryptChar == 32:
            f2.write(chr(DecryptChar))
        else:
            f2.write(str(DecryptChar))

    print("Process Complete.")
    f1.close()
    f2.close()
    
except:
    print("Unidentified Error. Program terminating.")
