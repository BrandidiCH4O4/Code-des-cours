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
def difference(ims0, ims1):
    pixs0 = ims0.load()
    pixs1 = ims1.load()
    imd = Image.new('F', ims0.size)
    pixd = imd.load()
    (width, height) = ims0.size
    for j in range(1,height-1):
        for i in range(1,width-1):
            pixd[i,j] = " à compléter"
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
            pixd[i,j] = " à compléter"
    return imd

"""
imd = somme(im, im_moy5)
affiche(imd)
"""
def binarization(img,seuil):
    imgbin=Image.new("L",img.size)
    pixg=img.load()
    pixbin=imgbin.load()
    width=img.size[0]
    height=img.size[1]
    for j in range(height):
        for i in range(width):
            "à compléter"
    return imgbin










im = ouvrir('texte1.jpg')
affiche(im)
