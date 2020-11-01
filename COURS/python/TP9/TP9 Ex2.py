"""Ex2"""
#a:
a="a"
print(a,":")
ch="ananas"
def modifie(ch):
    return ch.replace("ananas","@n@n@s")
print(modifie(ch))
######################
#b:
a="b"
print("")
print(a,":")
ch=['ananas','banane','pomme','mangue','fraise']
def modifie(ch):
    listeChara = list(ch)
    for lettre in range(len(ch)):
        if ch[lettre] == 'a':
            listeChara[lettre] = '@'
    return ''.join(listeChara)

def modifieListe(l):
    """
    #Version for "normale"
    
    newL = []
    for elem in l:
       newL.append(modifie(elem))
    return newL
    """
    return [modifie(elem) for elem in l]

print(modifieListe(ch))
