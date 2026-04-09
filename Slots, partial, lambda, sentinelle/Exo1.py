class Pokemon :
    __slots__ = ('nom', 'type')
    def __init__(self, nom, type):
        self.nom = nom
        self.type = type
    def __str__(self):
        return f"Pokémon : {self.nom} | Type : {self.type}"
    def __repr__(self):
        return f"<{self.nom}><{self.type}>"
    def __eq__(self, other):
        return self.nom == other.nom
    def __hash__(self):
        return hash(self.nom)

def demander_pkmn():
    print("Entrez le nom et le type d'un Pokémon (ou 'FIN' pour quitter):")
    while True :
        nom = input("Nom : ")
        if nom == "FIN":
            break
        type = input("Type : ")
        yield nom, type

pkmn_unique = {Pokemon(nom, type) for nom, type in demander_pkmn()}

print(f"\nNombre de Pokémon uniques : {len(pkmn_unique)}")
print(f"Liste : {pkmn_unique}")
print("Détail de la liste :")
for p in pkmn_unique:
    print(p)
