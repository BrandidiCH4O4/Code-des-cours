"""Ex1"""
#1:
print("1:")
def maximum(a,b):
   return max(a,b)
print("Le maximun entre 12 et 1 est: ", maximum(12,1))
#########################################################
#2:
print("")
print("2:")
def maximum4 (a,b,c,d):
    maximum1=maximum(a,b)
    maximum2=maximum(c,d)
    return maximum(maximum1,maximum2)
print("Le maximun entre 15, 3, 17 et 15 est: ", maximum4(15,3,17,15))
