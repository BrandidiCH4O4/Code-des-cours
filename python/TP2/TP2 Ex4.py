"Ex 4"
print('ax**2+bx+c=0')
a=float(input("Valeur de a --> "))
b=float(input("Valeur de b --> "))
c=float(input("Valeur de c --> "))
delta=b**2-4*a*c

print("delta=",delta)
if delta>0:
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a
    print("Il y a deux solution: x1=", x1, "et x2=",x2)
elif delta==0:
    x3=(-b)/2*a
    print("Il y a une solution: x=",x3)
elif delta<0:
    print("Il n'y a pas de solution")
