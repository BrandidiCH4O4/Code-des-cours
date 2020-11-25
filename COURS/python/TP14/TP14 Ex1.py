"""Ex1"""
#1:
e1 ={'alg': 9.0, 'python':15, 'anglais':7, 'cNum':15}
e2 ={'alg': 8, 'python':12, 'anglais':12, 'cNum':14, 'proba':9, 'Archi':11, 'Com':12}

def meilleure(etud):
    res=[]
    note=-1
    for matiere in etud:
        val=etud[matiere]
        if val> note:
            res=[matiere]
            note=val
        elif val==note:
            res.append(matiere)
    return res
#ou
"""
def meilleure2(et):
    n=max(et.values())
    return [mat for mat in et if et[mat]==n]
"""

print("e1 = La meilleure note de l'élève est :",meilleure(e1))
print("e2 = La meilleure note de l'élève est :",meilleure(e2))

################################################################
#2.1:
#✞#
print('')
coeffs ={"alg":6, "python":6, "anglais":2, "cNum":4, "proba":6, "Archi":4, "Com":2}

def sommeCoeff(etud):
    s=0
    for matiere in etud:
        s+=coeffs[matiere]
    return s

print("e1 = La somme des coeffs est de :",sommeCoeff(e1))
print("e2 = La somme des coeffs est de :",sommeCoeff(e2))

################################################################
#2.2:
print('')
def moyenneCoeff(etud):
    s=0
    for matiere in etud:
        s+=etud[matiere]*coeffs[matiere]
    n=sommeCoeff(etud)
    return round(s/n,2)

print("e1 = La moyenne de l'élève est de :",moyenneCoeff(e1))
print("e2 = La moyenne de l'élève est de :",moyenneCoeff(e2))

################################################################
#2.3:
print('')
"""def recu(etud):
    if sommeCoeff(etud) == 30:
        if moyenneCoeff(etud) >= 10:
            l="Bravo tu est reçu."
        return l
    elif sommeCoeff(etud) != 30:
            p="Tu n'as pas asser de coeffs, donc tu n'ai pas reçu."
    return p
#ou
"""
def recu(etud):
    s=sommeCoeff(etud)
    note=moyenneCoeff(etud)
    if s==30 and note>=10:
        return True
    elif s< 30 :
       return "pas assez de coeff"
    else:
        return False

print("e1 = ",recu(e1))
print("e2 = ",recu(e2))

################################################################
#3.1:
print('')
liste=[{'alg':9.0, 'python':15, 'anglais':7, 'cNum':15}, {'alg':12, 'python':12, 'anglais':8, 'cNum':12, 'proba':9, 'Archi':18, 'Com':11},
       {'alg':4, 'python':6, 'anglais':12, 'cNum':10, 'proba':5, 'Archi':11, 'Com':7}, {'alg':3, 'python':17, 'anglais':14, 'cNum':14, 'proba':4, 'Archi':15},
       {'alg':10, 'python':12, 'anglais':8, 'cNum':12, 'proba':11, 'Archi':11, 'Com':18}, {'alg':8, 'python':10, 'anglais':8, 'cNum':12, 'proba':7, 'Archi':12, 'Com':11}]

def nbEtud(liste):
    n=0
    for etud in liste:
        if recu(etud)==True:
            n+=1
    return n

print(nbEtud(liste))

################################################################
#3.2:
print('')
def ModifierLesDicos(listeEtud,mat,k):
    for et in liste:
        if mat in et:
            et[mat]*=k
    return liste
print(ModifierLesDicos(liste,'alg',1.5))


