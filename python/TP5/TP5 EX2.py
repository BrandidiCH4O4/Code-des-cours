"""Ex2"""
#1:
print('1:')
def masomme(n,p):
    res=0
    for i in range(0,n+1):
        res=res+(i**p)
    return(res)
print('Sn=',masomme(2,10))

########################################
#2:
print('')
print('2:')
def main():
    n=int(input('Entrer un entier: '))
    p=float(input('Entrer une puissance: '))
    return(masomme(n,p))
print('Sn=',main())
