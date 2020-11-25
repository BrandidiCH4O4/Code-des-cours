"""Ex2"""
#1:
from random import *
caracteresPermis="abcdefghijklmnopqrstuvwxyz'−_.,!?"
def creeCode(ch):
    lp=list(ch)
    n=len(lp)
    shuffle(lp)
    d={}
    for i in range(n):
        d[lp[i]]=i
    return d

print(creeCode(caracteresPermis))
######################################################
#2:
print('')
def Coder(message,dico):
    chaine = ""
    for x in message:
        chaine += str(dico[x]) + "/"
    return chaine

print(Coder())
######################################################
#3:
print('')
def Inverse(dico):
    randint(0,len(chainepermise)-1)
    shuffle(chainepermise)
    return chainepermise

print(creeCode(caracteresPermis))
######################################################
#4:
print('')
def Decoder(message, dico):
    randint(0,len(chainepermise)-1)
    shuffle(chainepermise)
    return chainepermise

print(creeCode(caracteresPermis))
"messageCode.split("/")"
