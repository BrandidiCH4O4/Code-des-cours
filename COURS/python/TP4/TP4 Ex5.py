"""Ex 5"""
#1:
print('1:')
import random
val=random.randint(1,6)
NbrLance=int(input('Combien de dés voulez-vous lancer: '))
resJoueur=0
resOrdi=0
tupleRes=()
plusProche=''
ScoreJoueur=0
ScoreOrdi=0
for tour in range(NbrLance):
    print('----------------- tour',tour+1,'------------')
    print('')
    resJoueur=resJoueur+random.randint(1,6)
    resOrdi=resOrdi+random.randint(1,6)
    if (resJoueur==21) or (resOrdi==21):
        print('Le joueur gagne 5 points.')
        ScoreJoueur=ScoreJoueur+5
        ScoreOrdi=ScoreOrdi+0
    elif (resJoueur==21) or (resOrdi==21):
        ScoreJoueur=ScoreJoueur+0
        ScoreOrdi=ScoreOrdi-+5
        print("L'ordi gagne 5 points.")
    elif (resJoueur<21) and (resOrdi<21):
        print("Les joueurs n'ont pas fait 21. Le plus proche des deux remporte 2 points")
        if max(resJoueur, resOrdi)==resJoueur:
            print('Le joueur gagne 2 points.')
            ScoreJoueur=ScoreJoueur+2
            ScoreOrdi=ScoreOrdi+0
        else:
            print("L'ordi gagne 2 points.")
            ScoreJoueur=ScoreJoueur+0
            ScoreOrdi=ScoreOrdi+2
    elif (resJoueur>=21) and (resOrdi>=21):
        print('la partie est nul. Les joueur ne gagne aucun points.')
        ScoreJoueur=ScoreJoueur+0
        ScoreOrdi=ScoreOrdi+0
    elif (resJoueur>21) or (resOrdi>21):
        ScoreJoueur=ScoreJoueur-2
        ScoreOrdi=ScoreOrdi-0
        print('Le joueur pert 2 points.')
    elif( resJoueur>21) or (resOrdi>21):
        ScoreJoueur=ScoreJoueur-0
        ScoreOrdi=ScoreOrdi-2
        print("L'ordi pert 2 points.")
    print('Le resultat du joueur: ',resJoueur, 'Le score du joueur est: ',ScoreJoueur)
    print("Le resultat de l'ordi: ",resOrdi, "Le score de l'ordi: ",ScoreOrdi)
    print('')
print("Le score totale du Joueur est de: ",ScoreJoueur)
print("Le score totale de l'Ordi est de: ",ScoreOrdi)
if ScoreJoueur>ScoreOrdi:
    print("Bravo, vous avez battu l'Ordi.")
elif ScoreJoueur==ScoreOrdi:
    print("Bravo vous avez fait match nul.")
elif ScoreJoueur<ScoreOrdi:
    print("Perdu, vous vous êtes fait battre par l'Ordi.")


###############################################################################################
#2:
print('')
print('2:')
import random
val=random.randint(1,6)
NbrLance=int(input('Combien de dés voulez-vous lancer: '))
resJoueur=0
resOrdi=0
tupleRes=()
plusProche=''
ScoreJoueur=0
ScoreOrdi=0
for tour in range(NbrLance):
    print('----------------- tour',tour+1,'------------')
    print('')
    Nbrde=int(input('Combien de dés voulez-vous? '))
    resJoueur=resJoueur+random.randint(1,(6*Nbrde))
    resOrdi=resOrdi+random.randint(1,(6*Nbrde))
    if (resJoueur==21) or (resOrdi==21):
        print('Le joueur gagne 5 points.')
        ScoreJoueur=ScoreJoueur+5
        ScoreOrdi=ScoreOrdi+0
    elif (resJoueur==21) or (resOrdi==21):
        ScoreJoueur=ScoreJoueur+0
        ScoreOrdi=ScoreOrdi-+5
        print("L'ordi gagne 5 points.")
    elif (resJoueur<21) and (resOrdi<21):
        print("Les joueurs n'ont pas fait 21. Le plus proche des deux remporte 2 points")
        if max(resJoueur, resOrdi)==resJoueur:
            print('Le joueur gagne 2 points.')
            ScoreJoueur=ScoreJoueur+2
            ScoreOrdi=ScoreOrdi+0
        else:
            print("L'ordi gagne 2 points.")
            ScoreJoueur=ScoreJoueur+0
            ScoreOrdi=ScoreOrdi+2
    elif (resJoueur>=21) and (resOrdi>=21):
        print('la partie est nul. Les joueur ne gagne aucun points.')
        ScoreJoueur=ScoreJoueur+0
        ScoreOrdi=ScoreOrdi+0
    elif (resJoueur>21) or (resOrdi>21):
        ScoreJoueur=ScoreJoueur-2
        ScoreOrdi=ScoreOrdi-0
        print('Le joueur pert 2 points.')
    elif( resJoueur>21) or (resOrdi>21):
        ScoreJoueur=ScoreJoueur-0
        ScoreOrdi=ScoreOrdi-2
        print("L'ordi pert 2 points.")
    print('Le resultat du joueur: ',resJoueur, 'Le score du joueur est: ',ScoreJoueur)
    print("Le resultat de l'ordi: ",resOrdi, "Le score de l'ordi: ",ScoreOrdi)
    print('')
print("Le score totale du Joueur est de: ",ScoreJoueur)
print("Le score totale de l'Ordi est de: ",ScoreOrdi)
if ScoreJoueur>ScoreOrdi:
    print("Bravo, vous avez battu l'Ordi.")
elif ScoreJoueur==ScoreOrdi:
    print("Bravo vous avez fait match nul.")
elif ScoreJoueur<ScoreOrdi:
    print("Perdu, vous vous êtes fait battre par l'Ordi.")
