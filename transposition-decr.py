import sys
def getKeys(keys):
    text =readingFile(keys)
    keys = text.split()
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

def decipherText(table,key):
    rearraged = []
    for i in range(len(key)):
        for j in range(len(table)):
            if key[i] == table[j][0]:
                rearraged.append(table[j])
                break
    return rearraged
                
def writeToFile(filename, plaintext):
    plainFile = open(filename,"w+")
    plainFile.write(plaintext)
    print("The decrypted text is in a file called "+filename)
    plainFile.close()

def transposeList(table):
    result = [[0 for y in range(len(table))] for x in range(len(table[0]))]
    for i in range(len(table)):
        for j in range(len(table[0])):
            result[j][i] = table[i][j]
    return result

def decryptTransposition(text, key):
    result = []
    sortedKey = ''.join(sorted(key))
    count = 0
    for i in range(10):
        newTable = []
        newTable.append(sortedKey[i])
        for j in range(int(len(text)/10)):
            if(count<len(text)):
                newTable.append(text[count])
                count+=1
        result.append(newTable)
    result = decipherText(result, key)
    result = transposeList(result)
    plaintext = ""
    pop = 0
    for i in range(1, len(result)):
        for j in range(len(result[i])):
            plaintext+=result[i][j]
    return plaintext

print("Decryptin...")
keys = getKeys(sys.argv[2])
key1 = keys[0]
key2 = keys[1]
filename = sys.argv[1]
ciphertext = readingFile(filename)
plaintext = decryptTransposition(ciphertext,key2)
plaintext = decryptTransposition(plaintext,key1)     
writeToFile(filename[:-7]+"-decrypted.txt", plaintext.upper())
print("Done!")
