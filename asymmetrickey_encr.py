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
    e = int(keys[0])
    n = int(keys[1])
    
    return e,n

def writeToFile(filename, wrappedText):
    wrappedFile = open(filename,"w+")
    wrappedFile.write(wrappedText)
    print("The wrapped-key text is in a file called "+filename)
    wrappedFile.close()

def encryptChar(m,e,n):
    stringWithEquationGCD = 'echo '+str(m)+'^'+str(e)+'%'+str(n)+'| bc '
    bc_cmd_output = subprocess.check_output(
        [stringWithEquationGCD],  # the command we want to send to shell
        universal_newlines=True,  # this lets us not have to deal with b'BYTE CODE' ,
        shell=True) 
    return bc_cmd_output.strip()

def wrapKey(text,e ,n):
    wrappedText = ""
    for i in range(len(text)):
       wrappedText+= encryptChar(ord(text[i]),e,n)+" "
    return wrappedText


publicKey = getKey(sys.argv[1])
publicE = publicKey[0]
print("E = ", publicE)
publicN = publicKey[1]
print("N = ", publicN)
keysText = readingFile(sys.argv[2])
print("keys: "+ keysText)
wrappedKey = wrapKey(keysText,publicE,publicN)
writeToFile("wrapped-keys.cipher", wrappedKey)
