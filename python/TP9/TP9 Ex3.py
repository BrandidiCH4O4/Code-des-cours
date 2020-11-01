"""Ex3"""
#1:
print("Ex 3 :")
maliste=["-2","3","-3","5","78"]
def absolue(maliste):
    for i in maliste:
        if i=='-':
            i+=maliste.replace('-','')
    return maliste
print(absolue(maliste))
