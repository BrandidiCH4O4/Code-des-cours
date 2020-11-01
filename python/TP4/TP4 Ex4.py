"""Ex 4"""
#1:
print('1:')
n=int(input('Entrer un entier n: '))
p=int(input('Entrer un entier p: '))
res=0
for i in range(1, p+1):
    print(n,'*',i,'=',n*i)

#2:
print('')
print('2:')
Espace=''
n=int(input('Entrer un entier n: '))
p=int(input('Entrer un entier p: '))
res=0
for i in range(1, p+1):  
    print(Espace,n,'*',i,'=',n*i)
    Espace+=' '
#3:
print('')
print('3:')
Espace=''
n=int(input('Entrer un entier n: '))
p=int(input('Entrer un entier p: '))
res=0
for i in range(1, p+1):
    if i%2==0:
        print(Espace,n,'*',i,'=',n*i)
        Espace+=''
    else:
        print(n,'*',i,'=',n*i,Espace)

#4:
print('')
print('4:')
nombreEspace=0
Espace=' '
n=int(input('Entrer un entier n: '))
p=int(input('Entrer un entier p: '))
res=0
for i in range(1, p+1):
    if i<=p/2:
        print((nombreEspace*Espace),n,'*',i,'=',n*i)
        nombreEspace+=1
    else:
        print((nombreEspace*Espace),n,'*',i,'=',n*i)
        nombreEspace-=1
