from datetime import datetime, timedelta

abonnement = {
    "user": "Jean",
    "date_debut": "2024-01-01",
    "duree_mois": 6
}

def est_encore_valide(data_dict):
    debut = datetime.fromisoformat(data_dict['date_debut'])
    duree_total = timedelta(days=data_dict.get('duree_mois', 0) * 30)
    date_fin = debut + duree_total
    maintenant = datetime.now()

    if maintenant > date_fin:
        return "Abonnement invalide"
    else :
        return "Abonnmment valide"

valide_ou_non = est_encore_valide(abonnement)
print(f"L'abonnement de {abonnement['user']} est valide : {valide_ou_non}")