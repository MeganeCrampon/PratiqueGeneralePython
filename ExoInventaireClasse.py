class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

class Inventaire:
    def __init__(self):
        self.produits = []
    def ajouter_produit(self, produit):
        self.produits.append(produit)
    def calculter_valeur_totale(self):
        total = 0
        for p in self.produits:
            total += p.quantite * p.prix
        return total
    def lister_rupture(self):
        return [p.nom for p in self.produits if p.quantite == 0]
    
# UTILISATION
ma_boutique = Inventaire()
ma_boutique.ajouter_produit(Produit("Potion", 50, 10))
ma_boutique.ajouter_produit(Produit("Epee", 75, 8))
ma_boutique.ajouter_produit(Produit("Armure", 60, 0))

print(f"La valeur total du stock de la boutique est de {ma_boutique.calculter_valeur_totale()}€.")
print(f"Les articles en rupture de stock dans la boutique sont : {ma_boutique.lister_rupture()}.")