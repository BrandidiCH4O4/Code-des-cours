"""Ex 3"""
#1:
import random
randint=random.randint
print('1:')
def alea(n):
    return(randint(1,n))
print(alea(5))

#################################
#2:
print('2:')
def lancer(n):
    res=0
    for i in range(n):
        if alea(2)==2:
           # print('Pile.')
            res+=1
        else:
           pass# print('Face.')
    return(res)
print('Nombre de pile obtenus:',lancer(6))

#################################
#3:
print('')
print('3:')
def main():
    n=int(input('Combien de lancer voulez-vous: '))
    return(lancer(n))
print('Nombre de lancer pile pour ces essais: ',main())
