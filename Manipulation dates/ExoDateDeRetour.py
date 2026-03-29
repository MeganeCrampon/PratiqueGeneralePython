from datetime import datetime, timedelta

emprunt = datetime.now()

def calculer_date_retour(date_emprunt):
    duree = timedelta(weeks = 3)
    date_retour = date_emprunt + duree
    return date_retour

date_de_retour = calculer_date_retour(emprunt)
print(f"La date de retour est le : {date_de_retour.date()}")