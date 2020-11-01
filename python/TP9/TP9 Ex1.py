"""Ex 1"""
#1:
y=1
print(y,":")
import random
def tous_zero(l):
    for i in l:
        if i!=0:
            return False
    return True
#print(tous_zero([0,0,0,0,0,0,0,0]))

#############################
#2:
y+=1
print("")
print(y,":")
def aumoins_zero(l):
    if  0 in l:
        return True
    else:
        return False
    return l
#print(aumoins_zero([1,1,1,0,1,1]))
###############################
#3:
y+=1
print("")
print(y,":")
def compte(x,l):
    cp=0
    for i in l:
        if i==x:
            cp+=1
        else:
            i+=1
    return cp
#print(compte(0,[0,1,3,3,1,1,3,0]))
#############################
#4:
y+=1
print("")
print(y,":")
def pairs(l):
    x=0
    x<=max(l)
    while x in l:
        l+=l[x]
        print(l)
    return l
#a refaire a la maison
#print(pairs([1,1,1,0,1,11,2,2,2,0,2,3,3]))
###################################
#5:
y+=1
print("")
print(y,":")
def positions_zero(l):
    x=("0.1","0.2","0.3","0.9")
    for i in l :
        if x in l:
            print(l[x])
    return l
#a refaire a la maison
#print(positions_zero([0.1,0.2,0.3,1,1,0,1,11,2,2,2,0,2,0.9,3,3]))
####################################
#6:
y+=1
print("")
print(y,":")
def supprime_double(l):
    l=list(set(l))
    return l
#print(supprime_double([0.9,10,3,7,5,11,4,5,0,1,7,1,6,3,3]))
##################################
#7.1:
y+=1
print("")
print(y,".1:")
ch1=["abricot","banane","orange","pèche","pomme","poire","prune"]
ch2=["abricot","banane","orange","pèche","poire","pommee","prune"]
def test(ch1,ch2):
    if ch1>ch2:
        return False
    return True
#print(test(ch1,ch2))
##############################
#7.2:
print("")
print(y,".2:")
l=ch1 and ch2
def testplus(ch1,ch2):
    for i in l:
        if ch1<ch2:
            return i
    return i
#print(testplus(ch1,ch2))
