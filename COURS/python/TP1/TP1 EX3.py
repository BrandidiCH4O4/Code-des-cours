"""Exercice3-IMC
Écrire un script qui demande à l'utilisateur
sa masse et sa taille puis calcule son IMC
(IMC= masse en kilos/(taille en mètre^2)) et
affiche le résultat selon l'interprétation
suivante: IMC Interprétation moins de 16,5
dénutrition ou famine 16,5 à 18,5 maigreur
18,5 à 25 corpulence normale 25 à 30 surpoids
plus de 30 obésité
Par exemple: votre poids en kg 55 votre taille en metres
1.70 votre imc est de 19.03 ce qui correspond
a la classification: corpulence normale"""

masse=float(input('Quelle est votre masse en Kg ? '))
taille=float(input('Quelle est votre taille en m ? '))
IMC=masse/(taille**2)
print('IMC = ',IMC)
if IMC<=16.5:
    print('Dénutrition ou famine.')
elif IMC<=18.5:
    print('Maigreure.')
elif IMC<=25:
    print('Corpulence normale.')
elif IMC<=30:
    print('Surpoids.')
elif IMC>=30:
    print('Obésité.')
