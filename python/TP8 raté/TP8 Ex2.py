"""Allumette"""
#1:
print("1:")
def affiche(n):
    print("* "*n)
    return n
#print(affiche(10))
#########################
#2:
print("")
print("2:")
def Min(a,b):
    if a>b:
        return b
    else:
        return a
#print(Min(100,20))
#########################
#3:
print("")
print("3:")
def saisie(a,b):
    print("Entrer un entier entre",a,"et",b,"compris :")
    nbsaisie=int(input())
    print("\n")
    if (nbsaisie>=b) and (saisie <=a):
        #print("Vous avez bon.")
        return a,b
    elif (nbsaisie<=b) and (saisie>=a):
        #print("Vous avez bon.")
        return a,b
    elif (nbsaisie!=a) and (saisie!=b):
      #  print("Vous ne comprenez pas. C'EST ECRIT ENTRE !!!")
        return a,b
#print(saisie(1,25))
#########################
#4:
print("")
print("4:")
def programmePrincip():
    affiche(21)
    print("Joueur 1 combien d'allumette")
    saisie(1,3)
    return 
print(programmePrincip())
