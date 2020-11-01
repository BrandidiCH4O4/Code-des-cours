"""Ex3"""
#1:
print('1:')
fruits=('pomme', 'poire', 'annas', 'banane', 'citron', 'carambole', 'kiwi')
mot=0
for i in fruits:
    if len(i)>=7:
        mot=mot+1
print(mot)

#2:
print('2:')
extraire=0
Tuple=()
for i in range(len(fruits)):
    if 'c'==str(fruits[i][0]):
        Tuple+=fruits[i],

print(Tuple)

#3:
print('3:')
Erreur=0
for i in range(len(fruits)):
    print('Recopier ce mot: ', fruits[i])
    x=input()
    if fruits[i]==x:
        print('Bravo.')
    else:
        print("Tu ne c'est pas recoipier.")
        Erreur+=1
print("tu as fait ", Erreur, " erreur.")
if Erreur<=1:
    print('Bravo tu es un génie.')
else:
    print('Tu as fait des érreurs.')
