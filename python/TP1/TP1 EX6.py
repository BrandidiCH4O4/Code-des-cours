"""Exercice6-Triangles
Écrire un script qui demande à l'utilisateur
3 entiers qui correspondent aux 3 angles
en degré d'un triangle et qui répond selon lescas:
- ce n'est pas un triangle (quand la somme des 3
nombres ne donne pas 180)
- c'est un triangle dégénéré (un des angles est nul)
- c'est un triangle quelconque
- c'est un triangle rectangle (un des angles est 90)
- c'est un triangle isocèle (deux angles égaux)
- c'est un triangle isocèle-rectangle (deux angles égaux et
un angle à 90 et pas d'angle nul)
- c'est un triangle équilatéral (3 angles égaux)
On fera attention à l'ordre des conditions pour mettre le moins
de tests possibles...."""
a=int(input('Entrer le premier entier --> '))
b=int(input('Entrer le deuxieme entier --> '))
c=int(input('Entrer le troisième enbtier --> '))
if a+b+c!=180:
    print("Ceci n'est pas un triangle.")
elif a==0 or b==0 or c==0:
    print('Ceci est un triangle dégénéré.')
elif a==b==c:
    print('Ceci est un triangle équilatéral.')
elif (a==90 and b==c) or (a==b and c==90) or (a==c and b==90):
    print('Ceci est un triangle isocèle-rectangle.')
elif a==90 or b==90 or c==90:
    print('Ceci est un triangle réctangle.')
elif a==b or a==c or b==c:
    print('Ceci est un triangle isocèle.')
elif a+b+c==180:
    print('Ceci est un triangle quelconque.')
