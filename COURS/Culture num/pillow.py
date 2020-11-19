#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

# ouvre une image
def ouvrir(nomimg):
    return Image.open(nomimg)

# affiche une image
def affiche(img):
    img.show()

# recupère un cannal d'une image multicannaux
def imc2img(imc, n):
    img = Image.new('F', imc.size)
    pixc = imc.load()
    pixg = img.load()
    (width, height) = imc.size
    for j in range(height):
        for i in range(width):
            pixg[i,j] = pixc[i,j][n]
    return img

# moyenne d'une image
def moyenne(ims):
    pixs = ims.load()
    imd = ims.copy()
    pixd = imd.load()
    (width, height) = ims.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            p  = pixs[i,j]
            p += pixs[i-1,j-1]
            p += pixs[i,j-1]
            p += pixs[i+1,j-1]
            p += pixs[i-1,j]
            p += pixs[i+1,j]
            p += pixs[i-1,j+1]
            p += pixs[i,j+1]
            p += pixs[i+1,j+1]
            pixd[i,j] = p // 9
    return imd

# moyenne itérative d'une image
def moyenneIterative(ims, n):
    imd = ims
    for i in range(n):
        imd = moyenne(imd)
    return imd



#Exercice 2 filtre médian
#2.1. médiane d'une liste
def mediane(liste):
    liste.sort()
    return liste[len(liste)//2]

#2.2. filtre médian
def MedianeImage(ims):
    imd0 = ims.copy()
    pixs = ims.load()
    pixd0 = imd0.load()
    (width, height) = ims.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            liste=[pixs[i+1,j],pixs[i-1,j],pixs[i,j],pixs[i,j-1],pixs[i,j+1]]
            med=mediane(liste)
            pixd0[i,j] = med
    return imd0

#2.2. filtre médian itératif
def MedianeIteratif(ims,n):
    imd0 = ims.copy()
    imd1 = ims.copy()
    pixs = ims.load()
    (width, height) = ims.size
    for n_i in range(n):
        pixd0 = imd0.load()
        pixd1 = imd1.load()
        for j in range(1,height-1):
            for i in range(1,width-1):
                liste=[pixs[i+1,j],pixs[i-1,j],pixs[i,j],pixs[i,j-1],pixs[i,j+1]]
                med=mediane(liste)
                pixd0[i,j] = med
        (imd0, imd1) = (imd1, imd0)
    return imd0


# dilatation d'une image
def dilatation(ims):
    pixs = ims.load()
    imd = ims.copy()
    pixd = imd.load()
    (width, height) = ims.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            p = pixs[i,j]
            p = max(p, pixs[i-1,j-1])
            p = max(p, pixs[i,j-1])
            p = max(p, pixs[i+1,j-1])
            p = max(p, pixs[i-1,j])
            p = max(p, pixs[i+1,j])
            p = max(p, pixs[i-1,j+1])
            p = max(p, pixs[i,j+1])
            p = max(p, pixs[i+1,j+1])
            pixd[i,j] = p
    return imd


# dilatation itérative d'une image
def dilatationIterative(ims, n):
    imd = ims
    for i in range(n):
        imd = dilatation(imd)
    return imd


# Erosion d'une image
def erosion(ims):
    pixs = ims.load()
    imd = ims.copy()
    pixd = imd.load()
    (width, height) = ims.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            p = pixs[i,j]
            p = min(p, pixs[i-1,j-1])
            p = min(p, pixs[i,j-1])
            p = min(p, pixs[i+1,j-1])
            p = min(p, pixs[i-1,j])
            p = min(p, pixs[i+1,j])
            p = min(p, pixs[i-1,j+1])
            p = min(p, pixs[i,j+1])
            p = min(p, pixs[i+1,j+1])
            pixd[i,j] = p
    return imd

# Erosion itérative d'une image
def erosionIterative(ims, n):
    imd = ims
    for i in range(n):
        imd = erosion(imd)
    return imd

# difference entre 2 images
def difference(ims0, ims1):
    pixs0 = ims0.load()
    pixs1 = ims1.load()
    imd = Image.new('F', ims0.size)
    pixd = imd.load()
    (width, height) = ims0.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            pixd[i,j] = pixs0[i,j] - pixs1[i,j]
    return imd

# somme de 2 images
def somme(ims0, ims1):
    pixs0 = ims0.load()
    pixs1 = ims1.load()
    imd = Image.new('F', ims0.size)
    pixd = imd.load()
    (width, height) = ims0.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            pixd[i,j] = pixs0[i,j] + pixs1[i,j]
    return imd

def binarization(ims, seuil):
    imd = ims.copy()
    pixs = ims.load()
    pixd = imd.load()
    (width, height) = ims.size
    for j in range(height):
        for i in range(width):
            pixd[i,j] = 255 if pixs[i,j] >= seuil else 0
    return imd

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

# 3-a)
imdil = dilatation(ims)

# 3-b)
imero = erosion(ims)

# 3-c)
def gradient(ims):
    imdil = dilatation(ims)
    imero = erosion(ims)
    imdiff = difference(imdil, imero)
    return imdiff

# 3-d)
imgrad = gradient(ims)
imbin = binarization(imgrad, 20)
affiche(imbin)
