import sqlite3
import os

conn = sqlite3.connect("SQL/Exo 3/pokemon.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Pokemons (
    id INTEGER PRIMARY KEY,
    nom TEXT UNIQUE,
    type TEXT,
    niveau INTEGER
)           
''')

cur.execute("SELECT COUNT(*) FROM Pokemons")
nombre_pokemons = cur.fetchone()[0]
if nombre_pokemons == 0:
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Pikachu', 'Electrique', 15)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Caninos', 'Feu', 12)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Kaiminus', 'Eau', 16)")
    conn.commit()

def ajouter_pokemon(nom, type, niveau):
    commande = "INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES (?, ?, ?)"
    cur.execute(commande, (nom, type, niveau))
    conn.commit()

def trouver_type(type_choisi):
    cur.execute("SELECT * FROM Pokemons WHERE type = ?", (type_choisi,))
    return cur.fetchall()

def trouver_niveau(niveau_choisi):
    cur.execute("SELECT * FROM Pokemons WHERE niveau >= ?", (niveau_choisi,))
    return cur.fetchall()

def affichage_recherche(liste_pokemons):
    if not liste_pokemons:
        print("[!] Aucun Pokemon trouvé !")
        return
    print("\n" + "="*55)
    print(f"{'Nom' :<15} | {'Type' :<19} | {'Niveau'}")
    print("-"*55)
    for pokemon in liste_pokemons:
        print(f"{pokemon[1]:<15} | Type : {pokemon[2] :<12} | Niveau : {pokemon[3]}")      
    print("="*55)

print("--- POKEDEX ---")


# TEST
print(f"--- POKEMONS DE TYPE : ELECTRIQUE ---")
resultat_elec = trouver_type('Electrique')
affichage_recherche(resultat_elec)
print(f"\n--- POKEMONS DE NIVEAU 12+ ---")
resultat_lvl_12 = trouver_niveau(12)
affichage_recherche(resultat_lvl_12)
print(f"--- POKEMONS DE TYPE : POISON ---")
resultat_poison = trouver_type('Poison')
affichage_recherche(resultat_poison)
