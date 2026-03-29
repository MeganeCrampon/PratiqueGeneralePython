from datetime import datetime, timedelta

heure_entree_str = "2026-03-29T09:00:00"

def ticket_est_depasse(entree_str):
    # 1. Convertis entree_str en objet datetime
    # 2. Crée un timedelta de 2 heures et 30 minutes (indice : hours=..., minutes=...)
    # 3. Calcule l'heure de fin de validité
    # 4. Compare avec datetime.now() et retourne True si dépassé, sinon False
    pass