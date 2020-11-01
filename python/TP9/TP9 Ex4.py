"""Ex4"""
#1:
y=1
print(y,":")
l=["0","1","10","5","2","4","6.1","6.2","8"]
def pairs(l):
    for i in l:
        if i%2:
            l+=[i,]
    return l
print(pairs(l))
