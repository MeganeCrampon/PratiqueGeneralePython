import json

inventaire_json = '''
[
    {"nom": "Clavier", "prix": 45, "quantite": 2},
    {"nom": "Souris", "prix": 20, "quantite": 5},
    {"nom": "Ecran", "prix": 150, "quantite": 1}
]
'''

def calculer_total(json_str):
    try:
        data=json.loads(json_str)
        total_general = 0
        for produit in data :
            # total_general = sum(p.get('prix', 0) * p.get('quantite', 0) for p in data)
            prix = produit.get('prix', 0)
            quantite = produit.get('quantite', 0)
            total_general += prix * quantite

        return total_general
    except (json.JSONDecodeError, ValueError) as e :
        return f"Erreur {e}"

print(f"Le prix total est de {calculer_total(inventaire_json)}.")