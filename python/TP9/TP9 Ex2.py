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
l=['ananas','banane','pomme','mangue','fraise']
def modifie_list(l):
    for i in l:
        if i=='a':
            i+=i.replace('a','@')
    return l
print(modifie_list(l))
