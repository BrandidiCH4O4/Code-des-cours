"""EX 2"""
def moyenne():
    cp=0
    nbr=int(input("Première valeure a rentrer: "))
    somme=0
    while nbr!=-1:
        cp+=1
        somme+=nbr
        nbr=int(input("Première valeure a rentrer ou tapper -1 pour stopper: "))
    n=somme//cp
    return n
print("La moyenne des valeurs saises est de: ", moyenne())
