"""Exercice2
Récupérer le fichier a_corriger.py.
Modifier ce programme jusqu'à ce qu'il n'y
ait plus d'erreurs (bien observer les messages d'erreurs)."""

# definitions de quelques constantes

e= 2.71
i= 1
pi=3.14159

# petit travail sur une chaine

ch= "Python "
ch1="est un"
d=  ch[5] + ch[4] + ch[3] + ch[2] + ch[1] + ch[0]
e= ch [2:] + ch [0:2]
f= ch[-1]
g=ch1[:6]
x=" informatique"
print (ch+ g +" langage"+x, "formidable")


#dialogue
n=input ("Quel est votre pseudo ?  ")
print ("Bonjour", n )
a= int(input (n+" quelle est votre annee de naissance ? "))
print ( "Ah vous avez", 2020 - a, "ans")
print("Au revoir")
