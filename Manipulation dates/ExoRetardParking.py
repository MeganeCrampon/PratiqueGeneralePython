from datetime import datetime, timedelta

heure_entree_str = "2026-03-29T09:00:00"

def ticket_est_depasse(entree_str):
    arrivee = datetime.fromisoformat(entree_str)
    duree=timedelta(hours=2, minutes=30)
    fin = arrivee + duree
    if datetime.now() > fin:
        return "Invalide (Temps dépassé)"
    else : return "Valide" 

ticket_valide = ticket_est_depasse(heure_entree_str)
print(f"Votre ticket est : {ticket_valide}")