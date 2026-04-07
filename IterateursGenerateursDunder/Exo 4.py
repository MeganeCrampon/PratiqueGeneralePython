import random

class Etoile:
    __slots__ = ('x', 'y', 'nom')
    def __init__(self, x, y, nom):
        self.x = x
        self.y = y
        self.nom = nom
    def __str__(self):
        return f"Nom de l'étoile : {self.nom} | Position : x={self.x}, y={self.y}."
    def __repr__(self):
        return f"Etoile(x={self.x}, y={self.y}, nom='{self.nom}')"

liste_etoiles = []
for e in range(1,1001):
    nouvelle_etoile = Etoile(x=random.randint(0, 900), y=random.randint(0, 900), nom =f"Etoile_{e}")
    liste_etoiles.append(nouvelle_etoile)

etoile_cible = next((etoile for etoile in liste_etoiles if etoile.nom == "Etoile_528"), "Non trouvée")
print(etoile_cible)
print(repr(etoile_cible))