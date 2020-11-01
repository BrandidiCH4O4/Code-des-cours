"""Ex1-Premieres boucles"""
##########################################################
#1:
for i in range(1, 11):
    print(i," -Bonjour.")
print("\n")

##########################################################
#2:
for n in range(1, 10001):
    calcul=1/n**2
print("-1/n**2=",calcul, "\n")

##########################################################
#3:
entier=int(input("Quel nombre entier voulez-vous ? "))
res=1
for n in range(1,entier+1):
    res*=n
print(entier,"!=", res, "\n")

##########################################################
#4:
i=int(input("Entier 1: "))
x=int(input("Entier 2: "))
resultat="La somme des cubes entre les deux entiers est: "
Somme=0
if i<x:
    for z in range(i, x+1):
        Somme=Somme+z**3
elif i>x:
    for z in range(x, i+1):
        Somme=Somme+z**3
print(resultat, Somme)
