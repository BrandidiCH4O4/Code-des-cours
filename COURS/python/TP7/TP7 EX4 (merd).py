""""EX 4"""
#1:
print("1:")
import random
def alea(n):
    return random.randint(1,n)
print(alea(100))

#####################################
#2:
print("")
print("2:")
def aumoins(n):
    pile=0
    face=0
    lancer=0
    cp=0
    t=()
    while face!=n and pile!=n:
        lancer=alea(2)
        if lancer==1:
            face+=1
        else:
            pile+=1
        cp+=1
    t=(face,pile)
    print(t)
    return cp
print(aumoins(10))

###################################
#3:
print("")
print("3:")
def main():
    n=int(input("Nombre voulu: "))
    aumoins(n)
    return aumoins(n)
print("Nombre de lancer",main())
