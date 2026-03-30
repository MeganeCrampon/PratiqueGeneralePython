import sqlite3
 
conn = sqlite3.connect("pokemon.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Pokemons (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    type TEXT,
    niveau INTEGER
)           
''')

cur.execute("INSERT INTO Pokemons (nom, type, niveau) VALUES ('Pikachu', 'Electrique', 15)")
cur.execute("INSERT INTO Pokemons (nom, type, niveau) VALUES ('Caninos', 'Feu', 12)")
cur.execute("INSERT INTO Pokemons (nom, type, niveau) VALUES ('Kaiminus', 'Eau', 16)")
conn.commit()

def ajouter_pokemon(nom, type, niveau):
    commande = ("INSERT INTO Pokemons (nom, type, niveau) VALUES (?, ?, ?)")
    cur.execute(commande, (nom, type, niveau))
    conn.commit()

def trouver_type(type_choisi):
    cur.execute("SELECT * FROM Pokemons WHERE type = ?", (type_choisi,))
    return cur.fetchall()

def trouver_niveau(niveau_choisi):
    cur.execute("SELECT * FROM Pokemons WHERE niveau >= ?", (niveau_choisi,))
    return cur.fetchall()

# TEST
ajouter_pokemon('Abo', 'Poison', 8)
print(f"Les Pokemons de type Electrique sont : {trouver_type('Electrique')}")
print(f"Les Pokemons avec un niveau d'au moins 12 sont : {trouver_niveau(12)}")
