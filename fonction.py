import mysql.connector
def Affichmenu(dictionaire):

    print("###########################################################################################################")
    print("##########              MENU                                                                    ###########")
    for keys,values in dictionaire.items():
        print(keys,")",values)
    print("E)Afficher les requêtes déjà choisi pour les ré exécuter")
    print("R)Réafficher tout le menu (exécuter ou non")
    print("Q)Quitter")
    print("###########################################################################################################")
def executequery(r):
    connectpar={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"DB_LemGUI"
    }
    with mysql.connector.connect(**connectpar) as db:
            with db.cursor() as c:
                c.execute(r)
                n=c.fetchall()
                for k in n:
                    print(k)