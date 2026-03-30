import sqlite3

conn = sqlite3.connect('pharmacie.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Medicaments (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prix REAL,
    stock INTEGER
)
''')

cur.execute("INSERT INTO Medicaments (nom, prix, stock) VALUES ('Doliprane', 2.50, 50)")
cur.execute("INSERT INTO Medicaments (nom, prix, stock) VALUES ('Sirop', 8.90, 10)")
conn.commit()

def trouver_medicaments_chers(prix_min):
    cur.execute("SELECT * FROM Medicaments WHERE prix > ?", (prix_min,))
    return cur.fetchall()
    
def alerte_stock_bas(seuil):    
    cur.execute("SELECT * FROM Medicaments WHERE Stock < ?", (seuil,))
    return cur.fetchall()

print(f"Les medicaments à plus de 5€ sont : {trouver_medicaments_chers(5)}")
print(f"Les medicaments à plus de 8€ sont : {trouver_medicaments_chers(8)}")
print(f"ALERTE Stock bas (moins de 15) : {alerte_stock_bas(15)}")
