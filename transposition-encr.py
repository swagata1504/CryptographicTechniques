from collections import OrderedDict
import sys
import re

def writeToFile(filename, cipher):
    cipherFile = open(filename,"w+")
    cipherFile.write(cipher)
    print("The encrypted text is in a file called "+filename)
    cipherFile.close()

def checkKey(inputKey):
    inputKey.lower()
    inputKey = "".join(OrderedDict.fromkeys(inputKey))
    if(len(inputKey)<10):
        print("Please enter a larger key. Possibly with fewer duplications.")
        exit()
    elif(inputKey.isalpha()!=True):
        print("Make sure to only use alphabets")
        exit()
    else:
        inputKey = inputKey[0:10]
    return inputKey

def readingKeys(filename):
    text = ""
    try:
        f = open(filename, "r")
        for x in f:
            text += x
    except IOError:
        print( "There is no file called "+ filename)
        exit()
        
    keys = text.split(" ")
    return keys

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

def createCipher(result):
    newTable = []
    for i in range(len(result)):
        newString = ''.join(result[i])
        newTable.append(newString)
    cipher = "" 
    orderedList = sorted(newTable)
    for i in range(len(orderedList)):
        for j in range(1,len(orderedList[0])):
            cipher+=orderedList[i][j]
    return cipher

def transposeList(table):
    result = [[0 for y in range(len(table))] for x in range(len(table[0]))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            result[j][i] = table[i][j]
    return result

def encryptTransposition(text, key):
    table = []
    count = 0
    text = text.replace(" ", "")
    text = re.sub('[^A-Za-z]', '', text)
    for i in range((len(text)//10)+1):
        new = []
        for j in range(0,10):
            if(count>(len(text)-1)):
                break
            new.append(text[count])
            count+=1
        if new:
            table.append(new)
        if len(new)<10:
            while len(new)!=10:
                new.append('x')
    table.insert(0,list(key))
    transposedTable = transposeList(table)
    return createCipher(transposedTable)


keys = readingKeys(sys.argv[2])
key1 = checkKey(keys[0])
key2 = checkKey(keys[1])
filename = sys.argv[1]
plaintext = readingFile(filename)
print("Encrypting...")
cipher = encryptTransposition(plaintext, key1)
cipher = encryptTransposition(cipher, key2)
writeToFile(filename[:-4]+".cipher", cipher)
print("Done")
