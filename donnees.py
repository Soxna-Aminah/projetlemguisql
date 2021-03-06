dictionn={
"1":"Lister les tous les agences",
"2":"Lister tous les caissiers par ordre croissant de leur nom",
"3" :"Lister tous chef d’agence ainsi que le nom de l’agence",
"4" :"Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
"5" :"Lister la somme des montants déposés par un caissier dans un compte de transactionde l’agence dont le chef est moussa dop par ordre croissant du montant",
"6":"Lister les utilisateurs de l’agence Plateau",
"7" :"Lister le nombre de compte par agence",
"8":"Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
"9" :"Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
"10":"Lister le montant des transactions effectué par utilisateur et par date dans l’agencedont le numéro est 001",
"11":"Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
"12":"Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussadiop par ordre croissant du montant",
"13":"Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop .",
"14":"Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
"15":"Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
"16":"Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
"17" :"Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
"18":"Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
"19":"Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
"20":"Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
"21":"Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221",
"22":"Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
"23":"Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
"24":"Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
"25":"Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop"
}
requetes={
    "1":"SELECT * FROM AGENCE",
    "2":"SELECT nom_USER FROM USERS JOIN PROFIL ON (id_PROFIL_PROFIL=id_PROFIL) WHERE libelle_PROFIL = 'caissier' ORDER BY nom_USER ASC",
    "3":"SELECT nom_USER,adresse_AGENCE FROM AGENCE JOIN USERS ON (AGENCE.id_USER_USER = USERS.id_USER) WHERE id_PROFIL_PROFIL =1",
    "4":"SELECT numero,solde_COMPTE_TRANSACTION,adresse_AGENCE FROM COMPTE_TRANSACTION JOIN TRANSACTIONS ON (TRANSACTIONS.numero_COMPTE_TRANSACTION = COMPTE_TRANSACTION.numero) JOIN AGENCE ON (AGENCE.numero_AGENCE = TRANSACTIONS.numero_AGENCE_AGENCE) WHERE adresse_AGENCE = '467 Everett Lane' ORDER BY solde_COMPTE_TRANSACTION ASC",
    "5":"SELECT SUM(montant_TRANSACTION),nom_USER FROM AGENCE JOIN USERS ON (AGENCE.numero_AGENCE = numero_AGENCE_AGENCE) JOIN TRANSACTIONS ON (TRANSACTIONS.id_USER_USER = USERS.id_USER) WHERE numero_AGENCE = (SELECT numero_AGENCE_AGENCE FROM USERS WHERE nom_USER = 'Siehard') AND id_PROFIL_PROFIL = 3 GROUP BY nom_USER",
    "6":"SELECT nom_USER FROM USERS JOIN AGENCE ON (AGENCE.numero_AGENCE = USERS.numero_AGENCE_AGENCE) WHERE adresse_AGENCE = '21 Dunning Alley'",
    "7":"SELECT COUNT(DISTINCT(numero_COMPTE_TRANSACTION)),numero_AGENCE_AGENCE FROM TRANSACTIONS GROUP BY numero_AGENCE_AGENCE",
    "8":"SELECT numero_COMPTE_TRANSACTION FROM USERS JOIN ASSOCIER ON(ASSOCIER.id_USER_USER = USERS.id_USER) WHERE nom_USER = 'Desantis' AND date_debut >= '2021-05-01' AND date_fin <= '2021-05-31'",
    "9":"SELECT nom_USER,numero_COMPTE_TRANSACTION FROM ASSOCIER JOIN USERS ON (ASSOCIER.id_USER_USER = USERS.id_USER) WHERE numero_COMPTE_TRANSACTION = 1",
    "10":"SELECT SUM(montant_TRANSACTION),id_USER_USER,date_TRANSACTION FROM TRANSACTIONS GROUP BY date_TRANSACTION,id_USER_USER ORDER BY date_TRANSACTION",
    "11":"SELECT COUNT(numero_COMPTE_TRANSACTION),id_USER_USER FROM ASSOCIER WHERE date_debut >= '2021-01-01' and date_fin <= '2021-03-31' GROUP BY id_USER_USER",
    "12":"SELECT date_TRANSACTION,COUNT( montant_TRANSACTION) from TRANSACTIONS where numero_AGENCE_AGENCE = (SELECT numero_AGENCE_AGENCE FROM USERS WHERE nom_USER = 'Siehard') group by date_TRANSACTION ORDER BY date_TRANSACTION ",
    "13":"SELECT montant_TRANSACTION,frais_TRANSACTION,id_TYPE_TYPE,id_USER_USER from TRANSACTIONS WHERE numero_AGENCE_AGENCE = (SELECT numero_AGENCE_AGENCE FROM USERS WHERE nom_USER = 'Siehard') AND id_USER_USER=41",
    "14":"SELECT montant_TRANSACTION, frais_TRANSACTION*0.4 part_etat, frais_TRANSACTION*0.3 part_systeme, frais_TRANSACTION*0.2 part_agence_retait, frais_TRANSACTION*0.1 part_agence_depot FROM TRANSACTIONS"
}
nrequetes={
"1":"select *from AGENCE",
"2":"select  *from USERS as u,PROFIL as p where id_PROFIL=id_PROFIL_PROFIL and p. libelle_PROFIL='caissier' order by nom_USER",
"3":"select  *from USERS ,PROFIL ,AGENCE where id_PROFIL=id_PROFIL_PROFIL and libelle_PROFIL='chef agence' and id_USER=id_USER_USER",
"4":"select * from TRANSACTIONS, AGENCE,COMPTE_TRANSACTION where numero_AGENCE=numero_AGENCE_AGENCE and adresse_AGENCE='692 Golden Leaf Place' and numero=numero_COMPTE_TRANSACTION ORDER BY solde_COMPTE_TRANSACTION",
"5":"select  sum(montant_TRANSACTION) from USERS as u,PROFIL as p,TRANSACTIONS as t,AGENCE as a ,USERS as us,PROFIL as pr where p.id_PROFIL=u.id_PROFIL_PROFIL and p. libelle_PROFIL='caissier' and t.id_USER_USER=u.id_USER and a.numero_AGENCE=t.numero_AGENCE_AGENCE and a.id_USER_USER=us.id_USER and us.nom_USER='Madgett' and us.id_PROFIL_PROFIL=pr.id_PROFIL and pr.libelle_PROFIL='chef agence'",
"6":"select *from USERS,AGENCE WHERE id_USER_USER=id_USER AND adresse_AGENCE='692 Golden Leaf Place'",
"7":"SELECT count(DISTINCT id_USER),numero_AGENCE,adresse_AGENCE,etat_AGENCE from USERS,AGENCE WHERE numero_AGENCE=numero_AGENCE_AGENCE group by numero_AGENCE"
}