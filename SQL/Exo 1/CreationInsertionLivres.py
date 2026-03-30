import sqlite3

# Connexion crée le fichier 'biblio.db'
conn = sqlite3.connect('biblio.db')
cur = conn.cursor()

# Création de la table
cur.execute('''
    CREATE TABLE IF NOT EXISTS Livres (
        id INTEGER PRIMARY KEY,
        titre TEXT,
        auteur TEXT
    )
''')

def ajouter_livre(titre, auteur):
    commande = "INSERT INTO Livres (titre, auteur) VALUES (?, ?)"
    cur.execute(commande, (titre, auteur))
    conn.commit()

def afficher_tous_les_livres():
    cur.execute("SELECT * FROM Livres")
    recup = cur.fetchall()
    for r in recup :
        print(r)

    conn.close()

# ajouter_livre("Le Petit Prince", "Saint-Exupéry")
afficher_tous_les_livres()