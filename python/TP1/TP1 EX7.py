"""Exercice 7 - petit dialogue et chaînes de caractères
Écrire un script qui demande à l'utilisateur son prénom,
l'année en cours, puis sa date de naissance sous la forme
'08/01/2012'.
Le programme testera si la date comporte bien 10 caractères
dont le 3ème et le 6 ème sont des '/', puis récupérera le mois
de naissance et achera un texte style vous êtes né en le 4 ème
mois de l'année et vous avez 21 ans."""

import datetime
now=datetime.datetime.now()
prenom=input('Bonjour quel est votre Prénom ? --> ')
annee=int(input("Bonjour "+ prenom +" en quel année somme nous ? --> "))
date=input("Quel est votre date de naissance ? --> ")
ch=date
jour=ch[0:2]
mois=ch[3:5]
année=ch[6:10]
date=(jour, mois, année)
age=int(annee)-int(année)
Ch=mois
if len(ch)==10 and ch[2]=='/' and ch[5]=='/':
    print("C'est le bon format.")
else:
    print("C'est le mauvais format.")
    exit()
if annee!=datetime:
    print("Ce n'est pas la bonne année.")
else:
if len(Ch)==2:
    print("Votre prénom est",prenom,"vous êtes née le ",mois,"ème mois de l'année et vous avez",age,"ans.")
