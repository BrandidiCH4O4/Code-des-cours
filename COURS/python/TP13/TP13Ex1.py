"""Ex1"""
#1:
dicoprix={"jambon":3, "sauce_tomate":1.5, 'poivrons':2, 'oignons':1, "champignons":2, "mozarella":1.5,
      "creme_fraiche":1.5, "chevre":2, "tomates":2, "lardons":2.5, 'saumon':4, 'merguez':3}
def combien(dicoprix):
    res=len(dicoprix)
    return res
print ("Le nombre d'ingrédient présent dans dico est de : ", combien(dicoprix))
###############################################
#2:
print('')
def prix_moyen (dicoprix):
    s=0
    for x in dicoprix:
        s+=dicoprix[x]
    return round(s/combien(dicoprix),2)
print("la moyenne du prix des ingrédients est de :",prix_moyen(dicoprix),"€")
###############################################
#3:
print('')
def moinscher(dico):
    mini=""
    val=10000000000000000
    for x in dico:
        if dico[x]<val:
            val=dico[x]
            mini=x
    return mini
"""ou
def moinscher(dic):
    res=min(dic.values())
    return[x for x in dic if dic[x]==res][0]
"""
print("Le moins cher des ingrédients est :", moinscher(dicoprix))
###############################################
#4:
print('')
#1€=>1.12$
def dollars(dic): 
    for x in dic:
        dic[x]=round(1.12*dic[x],2)
    return dic
"""répond pas aux attente, mais c'est la même
ou
def newdollars(dic): 
    d={}
    for x in dic:
        d[x]=round(1.12*dic[x],2)
    return d
ou
def newdollars(dic): 
    return {x:round(1.12*dic[x],2) for x in dic}
"""
print(dollars(dicoprix))
###############################################
#5:
print('')
l=["jambon","sauce_tomate","champignons","tomates","lardons"]
def prixpizza(listeing,dic):
    res=0
    for x in listeing:
        res+= dic[x]
    return res*1.5  # multiplication par 1.5 pour le reste
"""ou
def prixpizza2(listeing, dic):
    return sum([dic[x] for x in listeing])*1.5

ou

def prixpizza(l,dico):
    i=0
    for l in dico:
        i+=dico[l]
    return round((i*1.5),2)
"""
print("La pizza coute :",prixpizza(l,dicoprix),"€")
###############################################
#6:
print('')
dicoprix1={"jambon":3, "sauce_tomate":1.6, 'oignons':1, "champignons":2, "mozarella":1.5, "creme_fraiche":1.5, "chevre":2, "tomates":2, "lardons":2.5, 'saumon':4, 'merguez':3}
dicoprix2={"poivrons":2, "jambon":3.1, "sauce_tomate":1.5, 'poivrons':2, 'oignons':1, "roquefort":2, "mozarella":1.5, "chorizo":2.6, 'saumon_fume':3.5, 'merguez':3}
def gestion(d1,d2):
   d=d1.copy()
   for x in d2:
       if x in d1:
           d[x]=min(d1[x],d2[x])
       else:
            d[x]=d2[x]
   return d
print("Dicoprix =",gestion(dicoprix1,dicoprix2))
###############################################
#7:
print('')
monDicoPizzas={"reine":["jambon", "mozarella", "sauce_tomate", "champignons"], "vesuvio":['merguez', 'jambon', 'mozarella', 'poivrons', 'oignons'],
               "cabri":["chevre", "lardons", "creme_ fraiche", "mozarella"], "napoli":["jambon", "tomates", "mozarella", "sauce_tomate", "champignons", "poivrons", "oignons"],
               "neptune":['saumon', 'creme_ fraiche', 'champignons']}
def possible(dic, val, dicoprix):
    return[x for x in dic if prixpizza(dic[x], dicoprix)<=val]
print(possible(monDicoPizzas,12,dicoprix))
###############################################
#8:
def inter(l1,l2):
     for x in l1:
	if x in l2:
            return True
     return False
def sansallergie(ling, dicopizza):
     return [x for x in dicopizza if not(inter(ling, dicopizza[x]))]
print(inter(l1,l2))
###############################################
#9:
def fusion(dicoprix,dicopizzas):
    return True
"""print(fussion(dicoprix,dicopizzas))"""
