inventaire = [
    {"nom": "Potion de soin", "prix": 50, "quantité": 10},
    {"nom": "Épée en fer", "prix": 150, "quantité": 0},
    {"nom": "Bouclier", "prix": 80, "quantité": 5},
    {"nom": "Antidote", "prix": 25, "quantité": 0}
]

def analyser_stock(item_list):
    valeur_totale = 0
    en_rupture = []

    for item in item_list:
        valeur_totale += item["prix"] * item["quantité"]

        if item["quantité"] == 0:
            en_rupture.append(item["nom"])
    
    return valeur_totale, en_rupture

total, rupture = analyser_stock(inventaire)

print(f"La valeur totale du stock est de {total}.")
print(f"Les articles en rupture de stock sont : {rupture}.")