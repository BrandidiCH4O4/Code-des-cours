"""Exercice5-Équation du premier degré
Écrire un programme qui demande à l'utilisateur
de saisir 2 réels a,b puis qui affiche le résultat
de la résolution de l'équation ax+b= 0"""
a=int(input('Saisir le premier réel --> '))
if a==0:
    print('ERROR 404')
else:
    b=int(input('Saisir le deuxième réel --> '))
    x=(-b)//a
    print('x= ', x)
