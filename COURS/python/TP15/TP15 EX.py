"""Annuaire téléphonique"""
#1.a:
def recherche(n,p, bottin):
    port=open(bottin,"r")
    for l in port:
        x=l.split()
        #print(x)
        if x[0]==n and x[1]==p:
            port.close()
            return x[2:][0]
    port.close()
    return ""
#ou
"""
def recherche2(n,p, bottin):
    with open(bottin, 'r') as port:
        for l in port:
            x=l.split()
            if x[0]==n and x[1]==p:
                return x[2]
    return ""
"""

print(recherche("dupont","pierre","bottinNomPrenom.txt"))

#1.b:
print('')
def rechercheNom(nom,bottin):
    with open(bottin, 'r') as p:
        res=[]
        for l in p:
            x=l.split()
            if x[0]==nom :
                res.append(l[:-1])
    return res

print(rechercheNom("dupont","bottinNomPrenom.txt"))

#1.c:
print('')
def combien(pre,fichier):
    with open(fichier, 'r') as f:
        n=len(pre)
        res=0
        for l in f:
            x=l.split()
            if x[2][0:n]==pre:
                res+=1
    return res

print(combien("02","bottinNomPrenom.txt"))

#################################
#2.a:
print('')
def ressemble(num,ref):

    for i in range(10): # on teste des numeros de 10 chiffres imperativement (pas de test là-dessu
    
        if not(num[i]=="*" or num[i]==ref[i]):
            return False
    return True

print(ressemble("0231****12","0231465612"))

#2.b:
print('')
def compatible(num, bottin):  #affichage des numéros compatibles avec num
    with open(bottin, 'r') as p:     
        for l in p:
           x=l.split()
           if ressemble(num, x[2]):
               print (l[:-1])  # -1 pour éviter le saut de ligne
    return 'Y a plus personne de corespondant.'

print(compatible("********12","bottinNomPrenom.txt"))

#################################
#3:
print('')
def InterneFac(bottin):
    with open(bottin, 'r') as s:
        with open("Fac"+bottin, 'w') as n: 
            for l in s:
                x=l.split()
                if x[2][0:6]=="023156" :
                    n.write(x[0]+ " "+ x[1] + " "+ x[2][-4:]+"\n")
    return "J'ai fini."

print(InterneFac('bottinNomPrenom.txt'))

#################################
#4.a:
print('')
def ajoute0(nom,prenom,num,fichier):
    with open(fichier,"r") as fic:
        jioj
    return True

print()

#4.b:
print('')
def ajoute(nom,prenom,num,fichier):
    with open(fichier,'r') as fichi:
        ijioj
    return True

print()

#################################
#5:
print('')
def commun(bot1,bot2):
    with open(fichier,"r") as c:
        okioj
    return True

print()

#################################
#6.a:
print('')
def creationDico(fichier):
    with open("r") as fier:
        lkokjio
    return True

print()

#6.b:
print('')
def sauvegarde(dico,f):
    with open(fichier,"r") as fie:
        lkkoijio
    return True

print()
