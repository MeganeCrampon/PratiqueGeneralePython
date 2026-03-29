from datetime import datetime, timedelta

date_prevue = datetime.fromisoformat("2026-03-15")
date_reelle = datetime.fromisoformat("2026-03-29")

def jours_de_retard(prevue, reelle):
    ecart = reelle-prevue
    return ecart.days

retard = jours_de_retard(date_prevue, date_reelle)
print(f"Le retour a {retard} jours de retard.")