"""Simon"""
#1:
print("1: ")
def saut(n):
    n=""
    res=0
    for i in range(0,4):
        if n=="":
            print(n)
    return n
#print(saut(50))

#############################
#2:
import random
print("")
print("2:")
def alea():
    return random.randint(0,2)
#print(alea())
#############################
#3:
print("")
print("3:")
def affiche(ch):
    for i in ch:
        print(i,end=" ")
    return i
#print(affiche("10221000110222"))
############################
#4:
print("")
print("4:")
def SansEspaces(ch):
    ch=ch.replace(" un ex emple ici  ", "unexempleici")
    return ch
#print(SansEspaces(" un ex emple ici  "))
#############################
#5:
print("")
print("5:")
def Simon():
    ch=alea()
    cp=0
    print(ch)
    print("Vous avez mémoriser taper une touche tour continuer.")
    input()
    saut(3)
    print("Votre réponse:")
    chSaisie=int(input())
    #print("1")
    #SansEspaces(chSaisie)
    while chSaisie==ch:
        cp+=1
        #print("1")
        print("Bravo on continue")
        ch+=ch
        #affiche(ch)
    else:
        #print("1")
        print("Dommage.")
        print("Votre Score est de:")
    return cp
print(Simon())
