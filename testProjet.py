# coding: UTF-8 
""" 
Script: testProjet/testProjet
Création: admin, le 26/02/2021
"""


# Imports 
import sqlite3
import math
# Fonctions 
def insert(prenom, nom, calculDonne, calculPose, resultat):
#connection bdd
    conn = sqlite3.connect('testProjet.db')
    curs = conn.cursor()
# insertion
    #insert = "Insert into test (CalculPose, Resultat) Where id = 1 Values(?,?)"
# les donnees sont placées dans "un tableau"
    data = (calculPose, resultat)
# execution commande
    curs.execute("Insert into test (Prenom, Nom, CalculDonne, CalculPose, Resultat) Values(?,?,?,?,?)", (prenom, nom, calculDonne, calculPose, resultat))
    conn.commit()
    curs.close()
    conn.close()

#permet de sortir le contenu de la bdd sur un mec
def sortir(prenom, nom):
    conn = sqlite3.connect('testProjet.db')
    curs = conn.cursor()
    data = (prenom, nom)
    curs.executemany("Select * From test Where Prenom = ?", prenom)
    for x in curs.fetchall():
        printf(x)

# Programme principal 
def main():
    racine = "25"
    nom = "Court"
    prenom = ('Toby')
    id = "2"
    calculDonne = "5+5/2"
    calculPose = "5+5/math.sqrt(4)"
    resultat = eval(calculPose)
# permet d'ouvrir la bdd
    conn = sqlite3.connect('testProjet.db')
#crétaion du curseur pour bouger dans la bdd
    curs = conn.cursor()
#Select
    requete = 'Select * From test where Prenom='
    requete += '"Toby"'
    #curs.execute('Select * From test where Prenom=?', prenom)
    curs.execute(requete)
#affichage progressif dans le résultat
    for x in curs.fetchall():
        print(x)
#fermeture cursor
    curs.close()

    #insert(prenom, nom, calculPose, calculDonne, resultat)

    sortir(prenom, nom)

if __name__ == '__main__':
    main()
    # Fin
