"EX1"
a=float(input('Quel valeur de AB voulez-vous ? '))
b=float(input('Quel valeur de AC voulez-vous ? '))
c=float(input('Quel valeur de BC voulez-vous ? '))

if a<b+c and b<a+c and c<a+b:
    print("Ceci est un triangle.")
else:
    print("Ceci n'est pas un triangle")
