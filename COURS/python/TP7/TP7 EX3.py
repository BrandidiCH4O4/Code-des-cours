"""EX 3"""
#a:
print("a:")
def Supprime():
    print("Entrer quelque chose avec des espace au début:")
    ch=input()
    return ch.lstrip()
print(Supprime())

##############################################################
#b:
print("")
print("b:")
def Supprime():
    print("Entrer quelque chose avec des espace au à la fin:")
    ch=input()
    return ch.strip()
print(Supprime(), ".")
