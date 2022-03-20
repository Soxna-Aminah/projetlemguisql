
def Requetechoisi(diction):
    for k in diction:
        print(k)
def Affichagemenu(dictionn):
    c=0
    while c not in ['Q','q']:
        print("""##############################################################################################################
                                                            MENU
    ##############################################################################################################
        """)
        for keys,values in dictionn.items():
                print(keys ,")",values)
        print("E)Afficher les requêtes déjà choisi pour les ré exécuter")
        print("R)Réafficher tout le menu (exécuter ou non")
        print("Q)Quitter")
        print("##############################################################################################################")
        c=input("Faites votre choix: ")
        if c in dictionn:
           nidict=foncdic(c,dictionn)
           ndict=nidict[0]
           rdict=nidict[1]
           Affichagemenu(ndict)
        elif c in ['E','e']:
            print("Afficher les requêtes déjà choisi pour les ré exécuter")
        elif c in ['R','r']:
            print("Réafficher tout le menu (exécuter ou non)")
        else: print("Choix")

def foncdic(c,dictionna):
    dict2={}
    for keys in dictionna:
        if c==keys:
            print(dictionna[keys])
            dict2[c]=dictionna[c]
                    
    del dictionna[c]
    return dictionna,dict2


     