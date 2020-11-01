"Ex 3"
age=float(input('Quelle est votre âge ? '))
sexe=input('Quelle est votre sexe ? (h/f) ')
if (sexe=='h') and (age>=20):
    print("Vous payer l'impôt.")
elif (sexe=='f') and ((age>=18) and (age<=35)):
    print("Vous payer l'impôt.")
else:
    print("Vous payer pas l'impôt.")
