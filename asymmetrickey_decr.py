import sys
import subprocess

def readingFile(filename):
    text = ""
    try:
        f = open(filename, "r")
        for x in f:
            text += x
    except IOError:
        print( "Could not read file: "+ filename)
        exit()
    return text

def getKey(filename):
    text = readingFile(filename)
    keys = text.split()
    d = int(keys[0])
    n = int(keys[1])
    
    return d,n

def writeToFile(filename, wrappedText):
    wrappedFile = open(filename,"w+")
    wrappedFile.write(wrappedText)
    print("The keys are in a file called "+filename)
    wrappedFile.close()

def decryptChar(c,d,n):
    stringWithEquationGCD = 'echo '+str(c)+'^'+str(d)+'%'+str(n)+'| bc '
    bc_cmd_output = subprocess.check_output(
        [stringWithEquationGCD],  # the command we want to send to shell
        universal_newlines=True,  # this lets us not have to deal with b'BYTE CODE' ,
        shell=True) 
    return bc_cmd_output.strip()

def unwrapKey(text,d,n):
    plainKey = ""
    wrappedChars = text.split()
    for i in range(len(wrappedChars)):
       charASCII = decryptChar(int(wrappedChars[i]),d, n)
       if(i==0):
           print("It might take a while...")
       plainKey += (chr(int(charASCII)))
    return plainKey


privateKey = getKey(sys.argv[1])
privateD = privateKey[0]
privateN = privateKey[1]
print("Decrypting keys...")
filename = sys.argv[2]
wrappedKeysText = readingFile(filename)
wrappedKey = unwrapKey(wrappedKeysText,privateD,privateN)

writeToFile("unwrapped.txt", wrappedKey)
