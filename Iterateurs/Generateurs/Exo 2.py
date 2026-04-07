class Pokemon :
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau
    def __str__(self):
        return f"Le Pokémon {self.nom} est au niveau {self.niveau}."
    def __repr__(self):
        return f"Pokemon(nom='{self.nom}', niveau={self.niveau})"
    
p = Pokemon("Pichu", 5)

print(str(p))
print(repr(p))