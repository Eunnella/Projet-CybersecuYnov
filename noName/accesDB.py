#!/usr/bin/python3

import sqlite3

try:
    
    connectionDB = sqlite3.connect('Database.db')
    data_inutile= [['Unedonnée', 'NonNécessaire'],['UneAutredonnée', 'tjrPasNécessaire'],['etNon', 'tjrPas']]
    indice= '''INSERT INTO DATA_TWO (LOGIN, PASSWORD) VALUES ('indice', 'LatablecommenceparG');'''
    data_inutile1= [[1, 'NonNécessaire', 'notHere', 'flagada'],[2, 'Nope', 'stillnotHere', 'flagadagada'],[3,'etNon', 'tjrPas', 'tuChauffes'], [4, 'ceciEst', 'LeFlag', 'JesuIstrRRReeesF4tig8']]
    
    #j'ai utilisé des listes au lieu des dictionnaires pour facilité l'attaque
    
    cursor = connectionDB.cursor()
    print("Succesful connection to DB! \n")
    for d in data_inutile:
        cursor.execute("insert into DATA_ONE (LOGIN, PASSWORD) values (?, ?)", d)
        cursor.execute("insert into DATA_TWO (LOGIN, PASSWORD) values (?, ?)", d)
        cursor.execute("insert into DATA_THREE (LOGIN, PASSWORD) values (?, ?)", d)
    
    cursor.execute(indice)
    
    for di in data_inutile1:
        cursor.execute("insert into GroupeCS (ID, NAME, LOGIN, PASSWORD) values (?, ?, ?, ?)", di)

    
    connectionDB.commit()
    print("Data entry : SUCCESS! \n")

    cursor.close()

except sqlite3.Error as error:
    print("Data entry : FAILURE! \n", error)

finally:
    if connectionDB:
        connectionDB.close()
        print("Connection to DB : closed \n")