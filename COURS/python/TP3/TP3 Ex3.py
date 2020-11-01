"""Ex3"""
x=int(input("Bonjour, combien de valeurs voulez-vous saisir ? "))
note=[]
mooy=0
moyc=0
Adire=''
for c in range(x):
    Adire='Note '+ str(c+1)+': '
    note.append(float(input(Adire)))
for c in range(len(note)):
    moyc+=note[c]
moy=moyc/len(note)
print(moy)
