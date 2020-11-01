"""Ex1"""
#1:
resultat=0
for i in range(1,64):
    resultat=resultat+2**i
print(resultat)

#2:
t=(10**3, 10**10, 10**100)
Somme=0
for i in t:
    Somme=Somme+i
    print("La somme fait: ", Somme)
