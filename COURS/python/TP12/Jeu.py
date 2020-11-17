"""Jeu de grille"""
#############################################
#1:
#print('1:')
def creegrille(n, x):
    res=[0]*n
    for i in range(n):
        res[i]= [x]*n
    return res
#############################################
#4:
#print('')
#print('2:')
def affiche (grille):
    for l in grille:
        for x in l:
            print(x,' ',end="")
        print()

##############################################
#3:
#print('')
#print('3:')
from random import *
"""
def aleagrille(n,t,f):
    f='0'
    t='1'
    (i,j)=random.randint(0,n-1), random.randint(0,n-1)
    m=creegrille(n,'_')
    if m[i][j]=='_':
       m[i][j]=1
    while t!=0:
        print(t)*t
    while f!=0:
        print(f)*f
"""
def aleagrille(n,t,f):  # avec n taille de la grille,  t trésors, f fantômes
    m=creegrille(n,'_')
    cp=0
    while cp<t:
        (i,j)=randint(0,n-1), randint(0,n-1)
        if m[i][j]=="_":
            m[i][j]=1
            cp+=1
         
    cp=0        
    while cp<f:
        (i,j)=randint(0,n-1), randint(0,n-1)
       
        if m[i][j]=="_":
            m[i][j]=0
            cp+=1
    return m
#print(affiche(aleagrille(8,4,6)))
##############################################
#4:
#print('')
#print('4:')
def deplacement0(m,d, i,j):# deplacement de d à partir de la position i j
    n=len(m)
    x,y=i,j
    if d=="H":
        x=i-1
    elif d=='B':
        x+=1
    elif d=='G':
        y-=1
    elif d=='D':
        y+=1
    else:
        return deplacement0
    if x in range(0,n) and y in range(0,n):
        m[i][j]='_'
        m[x][y]='*'
        return [x,y]
    else:
        print ("sortie !!!")
        return [i,j]

##############################################
#5:
#print('')
#print('5:')
def deplacement0(m,d, i,j):# deplacement de d à partir de la position i j
    n=len(m)
    x,y=i,j
    p=0
    cp=0
    if d=='H':
        x=i-1
    elif d=='B':
        x+=1
    elif d=='G':
        y-=1
    elif d=='D':
        y+=1
    else:
        return deplacement0
    if x in range(0,n) and y in range(0,n):
        m[i][j]='_'
        if m[x][y]==0:
            p=5
            print ("tresor !!! vous gagnez 5 points")
        elif m[x][y]==1:
            p=-10
            print ("fantome !!! vous perdez 10 points")
        m[x][y]='*'
        return [x,y,p]
    else:
        print ("sortie !!! vous perdez 2 points")
        return [i,j,-2]
#print(deplacement0(aleagrille(8,4,6),"D",0,0))
"""
    test=aleagrille(8,6,7)
    test[2][3]="*"
    affiche(test)
    deplacement0(test,2,3,"D")
    affiche(test)
"""
##############################################
#6:
#print('')
#print('6:')
def saisie_dep():
    rep=input ("votre deplacement ? entre B,D,G,H ")
    while rep not in ("B","D","G","H"):
        print("incorrect.")
        rep=input ("votre deplacement ? ")
    return rep
def jeu(n,t,f):
    m=aleagrille(n,t,f)
    print("fantomes=0", "tresor = 1\n")
    m[0][0]='*'
    m[n-1][n-1]="A"
    posi=0
    posj=0
    points=0
    affiche(m)
    fin=0
    while not fin:
       dep=saisie_dep()
       val=deplacement0(m,dep,posi,posj)
       points+=val[2]
       posi=val[0]
       posj=val[1]
       affiche(m)
       if posi==n-1 and posj==n-1:
           fin=1
    print ("vous etes sortis avec ", points, "points")
    if points>0:
        print ('bravo')
    else:
        print("dommage......")
#print(jeu(8,4,6))
##############################################
#7:
#print('')
#print('7:')
"""def saisie():
    rep=input ("votre deplacement ? entre B,D,G,H ")
    n=int(input('Veuillez choisir la taille de votre jeu ? '))
    t=int(input('Veuillez choisir le nombre de trésors ? '))
    f=int(input('Veuillez choisir le nombre de fantômmes ? '))
    while rep not in ("B","D","G","H"):
        print("incorrect.")
        rep=input ("votre deplacement ? ")
    while n != n*4:
        print("ceci n'est pas un carré.")
        n=int(input("votre taille ? "))
    while t>=n:
        print('il y a trop de trésors.')
        t=int(input('Quelque chose de plus petit ? '))
    while f>=n:
        print('il y a trop de fantômes.')
        f=int(input('Moins que ça ?'))
    return rep
def jeu():
    m=aleagrille(saisie_dep,saisie,saisie)
    print("fantomes=0", "tresor = 1\n")
    m[0][0]='*'
    m[n-1][n-1]="A"
    posi=0
    posj=0
    points=0
    affiche(m)
    fin=0
    while not fin:
       dep=saisie_dep()
       val=deplacement0(m,dep,posi,posj)
       points+=val[2]
       posi=val[0]
       posj=val[1]
       affiche(m)
       if posi==n-1 and posj==n-1:
           fin=1
    print ("vous etes sortis avec ", points, "points")
    if points>0:
        print ('bravo')
    elif tresors == 0:
        print('Bravo vous avez trouvez tous les trésors')
    else:
        print("dommage......")
print(jeu())"""
