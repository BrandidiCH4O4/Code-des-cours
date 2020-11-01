"""Ex 1"""
#1:
print("1:")
def saisieON():
    rep=input("Entrer OUI ou NON ")
    while rep!="OUI" and rep!="NON":
        print(rep, "n'est pas une réponse acceptable.")
        print("")
        rep=input("Entrer OUI ou NON ")
    return rep

print("")
print(saisieON(), "est une réponse accépté.")

############################################################
#2:
print("")
print("2:")
reponse=("oui","ui","o","y","Oui","OUI","Ui","UI","O","Y","yes","Yes","YES","nan","non","no","n","Nan","Non","No","NAN","NON","NO","N","nn","Nn","NN")
def begin():
    for lettre in reponse:
        if (lettre is "n") or (lettre is "N"):
            return 0
        elif (lettre is "y") or (lettre is "Y") or (lettre is "u") or (lettre is "U") or (lettre is "o") or (lettre is "O"):
            return 1
    return lettre
print(begin)

def saisieON():
    rep=input("Entrer OUI ou NON ")
    while rep not in reponse:
        if rep!=begin():
            print(rep, "n'est pas une réponse acceptable.")
            print("")
            rep=input("Entrer OUI ou NON ")    
    return rep

print("")
print(saisieON(), "est une réponse accépté.")

