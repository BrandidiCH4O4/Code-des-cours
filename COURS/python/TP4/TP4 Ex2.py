"""Ex2"""
#1:
print('1:')
ch=("coucou")
print(ch)
res=''
for i in ch:
    res=res+i*2
print(res)

#2:
print('2:')
cha=("bonjour j'aime la vie")
print(cha)
r=('*')
res2=''
for i in range(len(cha)):
    if i%2!=0:
        res2=res2+r
    else:
        res2=res2+cha[i]
print(res2)

#3:
print('3:')
voyelle=0
espace=0
voyelles=('a', 'e', 'i', 'o', 'u', 'y')
phrase=("j'aime la vie achetter moi une corde!!!")
print(phrase)
for i in phrase:
    if i==" ":
        espace=espace+1
    elif i in voyelles:
        voyelle=voyelle+1
print('il y a', voyelle,'voyelles et', espace,'espaces dans la phrase')
