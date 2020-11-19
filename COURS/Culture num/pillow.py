#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import random as r
from math import *

#---------FONCTIONS DE BASE---------

def ouvrir(nomimage):
    #Creer l'objet image a partir du fichier image, exemple : nomimage='lena.jpg'
    img=Image.open(nomimage)
    #Renvoie l'objet image a partir du fichier image
    return img

def affiche(img):
    #Affiche l'image
    img.show()

def imc2img(imc,n):
    #Transforme une image couleur en une image de niveaux de gris
    img=Image.new("L",imc.size) # Cree une image de meme taille que imc
    pixc=imc.load() # Recupere le tableau des pixels de imc
    pixg=img.load() # Recupere le tableau des pixels de img
    width = imc.size[0] # Le nombre de colonnes de l'image
    height=imc.size[1] # Le nombre de lignes de l'image

#Parcours de l'image : lignes / colonnes
    for j in range(height):
        for i in range(width):
            pixg[i,j]=pixc[i,j][n]

    #pour sauvegarder
    #img.save("img.bmp")

    return img



 #différence entre 2 images

# afficher une image
ims = ouvrir('femme.png')
affiche(ims)

# 1-a) moyenne d'une image
imavg = moyenne(ims)
affiche(imavg)

# 1-b) moyenne itérative
imavg5 = moyenneIterative(ims, n=5)
affiche(imavg5)

# 1-c) mediane
immed = MedianeImage(ims)
affiche(immed)

# 2-a)
ims1 = moyenneIterative(ims, 5)

# 2-b)
ims2 = moyenneIterative(ims, 20)

# 2-c)
imdiff = difference(ims1, ims2)

# 2-d)
imbin = binarization(imdiff, 0)

# 2-e)
def polarity(ims):
   ims1 = moyenneIterative(ims, 5)
   ims2 = moyenneIterative(ims, 20)
   imdiff = difference(ims1, ims2)
   imbin = binarization(imdiff, 0)
   return imbin
