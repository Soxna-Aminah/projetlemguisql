from tkinter import E
from donnees import *
from fonction import *
import copy
c=0
e={}
dicto=copy.deepcopy(dictionn)
while c not in ['Q','q']:
    Affichmenu(dictionn)
    c=input("Faites votre choix: ")
    if c in dictionn:
         executequery(requetes[c])
         e[c]=dictionn[c]
         del dictionn[c]
         Affichmenu(dictionn)
    elif c in ['E','e']:
        Affichmenu(e)
        nc=input("Faites votre choix: ")
        executequery(requetes[nc])
        Affichmenu(e)
    elif c in ['R','r']:
        Affichmenu(dicto)
    else:
        print("Choix indisponible")


