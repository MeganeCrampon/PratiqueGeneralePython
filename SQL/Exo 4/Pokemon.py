import sqlite3

conn = sqlite3.connect("SQL/Exo 4/dresseurs_et_pokemons.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Pokemons (
    id INTEGER PRIMARY KEY,
    nom TEXT UNIQUE,
    type TEXT,
    niveau INTEGER
)           
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Dresseurs (
    id INTEGER PRIMARY KEY,
    nom TEXT UNIQUE,
    pokemon_id INTEGER,
    FOREIGN KEY (pokemon_id) REFERENCES Pokemons(id)
)''')

cur.execute("SELECT COUNT(*) FROM Pokemons")
nombre_pokemons = cur.fetchone()[0]
if nombre_pokemons == 0:
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Pikachu', 'Electrique', 15)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Caninos', 'Feu', 12)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Kaiminus', 'Eau', 16)")
    cur.execute("INSERT OR REPLACE INTO Pokemons (nom, type, niveau) VALUES ('Articodin', 'Glace', 52)")
    conn.commit()

cur.execute("SELECT COUNT(*) FROM Dresseurs")
nombre_dresseurs = cur.fetchone()[0]
if nombre_dresseurs == 0:
    cur.execute("INSERT OR REPLACE INTO Dresseurs (nom, pokemon_id) VALUES ('Sacha', 1)")
    cur.execute("INSERT OR REPLACE INTO Dresseurs (nom, pokemon_id) VALUES ('Régis', 2)")
    cur.execute("INSERT OR REPLACE INTO Dresseurs (nom, pokemon_id) VALUES ('Pierre', 3)")
    cur.execute("INSERT OR REPLACE INTO Dresseurs (nom, pokemon_id) VALUES ('Cynthia', 4)")
    conn.commit()

def afficher_equipe():
    commande = '''
    SELECT Dresseurs.nom, Pokemons.nom 
    FROM Dresseurs 
    JOIN Pokemons ON Dresseurs.pokemon_id = Pokemons.id
    '''
    cur.execute(commande)
    resultat = cur.fetchall()
    
    for dresseur, pokemon in resultat:
        print(f"Le dresseur {dresseur} possède {pokemon} !")

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

def dresseur_puissant():
    commande = '''
    SELECT Dresseurs.nom, Pokemons.nom, Pokemons.niveau
    FROM Dresseurs
    JOIN Pokemons ON Dresseurs.pokemon_id = Pokemons.id 
    WHERE Pokemons.niveau >= 50
    '''
    cur.execute(commande)
    resultat = cur.fetchall()

    for dresseur, pokemon, pk_niveau in resultat:
        print(f"Le dresseur {dresseur} est puissant : il possède un {pokemon} de niveau {pk_niveau} !!")

print("------ POKEDEX ------")


# TEST
print(f"\n--- POKEMONS DE TYPE : ELECTRIQUE ---")
resultat_elec = trouver_type('Electrique')
affichage_recherche(resultat_elec)

print(f"\n--- POKEMONS DE NIVEAU 12+ ---")
resultat_lvl_12 = trouver_niveau(12)
affichage_recherche(resultat_lvl_12)

print(f"\n--- POKEMONS DE TYPE : POISON ---")
resultat_poison = trouver_type('Poison')
affichage_recherche(resultat_poison)

print("\n--- EQUIPES ---")
afficher_equipe()

print("\n--- DRESSEURS PUISSANTS ---")
dresseur_puissant()