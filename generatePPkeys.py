from subprocess import Popen, PIPE, STDOUT
import subprocess
import sys

def subpsfunc(a, b, op):
    p = Popen(['bc'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    encode_a_b  = "{} {} {}\n".format(a,op,b).encode('utf-8')
    stdout_data = p.communicate(input=encode_a_b)[0]
    result = stdout_data.decode('utf-8')[:-1]
    return int(result)

def gcd(a,b):
    stringWithEquationGCD = 'echo gcd \('+str(a)+','+str(b)+'\) | bc gcd'
    bc_cmd_output = subprocess.check_output(
        [stringWithEquationGCD],  # the command we want to send to shell
        universal_newlines=True,  # this lets us not have to deal with b'BYTE CODE' ,
        shell=True) 
    return int(bc_cmd_output.strip())

def checkD(d,e,totient_n):
    stringWithEquationGCD = 'echo '+str(d)+'*'+str(e)+'%'+str(totient_n)+'| bc '
    bc_cmd_output = subprocess.check_output(
        [stringWithEquationGCD],  # the command we want to send to shell
        universal_newlines=True,  # this lets us not have to deal with b'BYTE CODE' ,
        shell=True) 
    return int(bc_cmd_output.strip())

def generatePublicKey(n, p, q):
    totient_n = subpsfunc(p-1, q-1, '*')
    e = 0
    for i in range(104, totient_n):
        if gcd(i, totient_n)==1:
            print("gcd with 1 with totient_n is ",i)
            e = i
            break
    return totient_n, e

def generatePrivateKey(totient_n,e):
    for d in range(1, totient_n):
        if(checkD(d,e,totient_n)==1):
            break
    return d


p = input("Enter first prime number")
q = input("Enter second prime number")
print("Creating keys...")
n = subpsfunc(p,q,"*")
publicKey = generatePublicKey(n,p,q)
totient_n = publicKey[0]
e = publicKey[1]
print("e = ", e)
print("This might take a while....")
d = generatePrivateKey(totient_n,e)
print("d = ",d)
print("n = ", n)
publicKeyOut = open("public-key.txt","w+")
publicKeyOut.write(str(e)+" "+str(n))
publicKeyOut.close()

privateKeyOut = open("private-key.txt","w+")
privateKeyOut.write(str(d)+" "+str(n))
privateKeyOut.close()
print("Keys are done.")
