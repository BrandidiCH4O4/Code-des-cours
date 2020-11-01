"""Ex 2-- Travail avec des chaînes"""
#######################################################################################
#1:
phrase=input("Entrer une phrase: ")
lettre1=input("Entrer une première lettre: ")
lettre2=input("Entrer une seconde lettre: ")
x=0
y=0
for ch in phrase:
    if ch==lettre1:
        x=x+1
    elif ch==lettre2:
        y=y+1
print("Il y a ",x, "lettres ", lettre1, "et ",y, "lettres", lettre2, "dans la phrase.")

#######################################################################################
#2:
ph=input("Entrer un phrase: ")
lettre=input("Entrer une première lettre: ")
lettre3=input("Entrer une seconde lettre: ")
ph2=''
for c in ph:
    if c==lettre:
        ph2=ph2+lettre3
    elif c==lettre3:
        ph2=ph2+lettre
    else:
        ph2=ph2+c
print(ph2)
