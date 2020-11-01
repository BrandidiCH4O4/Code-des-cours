"""Exercice4
Écrire un script qui demande un entier N
à l'utilisateur et affiche selon les cas:
-N est divisible par 3 et 5
-N est divisible par 3 mais pas par 5
-N est divisible par 5 mais pas par 3
-N n'est divisible ni par 3 ni par 5
Pour tester qu'un nombre n est divisible
par p,on utilisera le test n%p==0"""
n=int(input('Marquer un entier --> '))
if n%3==0 and n%5==0:
    print('-N est divisible par 3 et 5.')
elif n%3==0 and n%5!=0:
    print('-N est divisible par 3 mais pas par 5.')
elif n%3!=0 and n%5==0:
    print('-N est divisible par 5 mais pas par 3.')
elif n%3!=0 and n%5!=0:
    print("-N n'est divisible ni par 3 ni par 5.")
