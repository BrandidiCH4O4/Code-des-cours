"""Ex4"""
#1:
import random
randint=random.randint
print('1:')
def alea(n):
    return(randint(1,n))
print(alea(10))

#################################
#2:
print('')
print('2:')
def calcul(n):
    a=alea(n)
    b=alea(n)
    print('Quelle est le résultat',a,'+',b,'= ',end='')
    c=int(input())
    if c==a+b:
        print('Bravo !')
        return(1)
    else:
        print('La réponse était:',a+b)
        return(0)
    return(alea(n))
print(calcul(10))
###############################
#3:
print('')
print('3:')
def Serie_calcul(n,nb):
    Score=0
    res=0
    n=10
    nb=3
    print('Valeur maximum des nombres: ',n)
    print('Nombre de calcul: ',nb)
    for i in range(1,nb+1):
        res=calcul(n)
        if res==1:
            Score+=1
    return(Score)
print('Score total pour les calcul: ',Serie_calcul(10,3))
##############################
#4:
print('')
print('4:')
def main():
    n=int(input('Valeur maximum des nombres: '))
    nb=int(input('Nombre de calcul: '))
    Score=Serie_calcul(n,nb)
    return(Score)
print('Score total pour les calcul: ',main())
