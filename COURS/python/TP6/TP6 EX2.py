"""Ex2"""
#1:
##a:
print("1:")
print("a:")
l1=("ananas", "pomme", "poire", "kiwi", "banane")
l2=("kiwi", "pomme", "poire", "fraise", "pizza")

def compare_nb(l1,l2):
    cp=0
    for mot in l1:
        if mot in l2:
            cp+=1
    return(cp)
print("I y a ", compare_nb(l1,l2), "mots identiques.")

##b:
print("")
print("b:")
def compare(l1,l2):
    t=()
    for mot in l1:
        if mot in l2:
            t+=(mot,)
    return(t)
print(compare(l1,l2), "sont les mots identiques.")

#########################################################
#2:
print("")
print("2:")
def fusion(l1,l2):
    t=(l1)
    for mot in l2:
        if mot not in l1:
            t+=(mot,)
        else:
            pass
    return(t)
print(fusion(l1,l2))

########################################################
#3:
print("")
print("3:")
def MotPlusLong(l1):
    motp=0
    for mot in l1:
        if str(len(mot))>=max(mot):
            motp+=1
            print(motp)
    return(mot)
print("le mot le plus long est:", MotPlusLong(l1))
