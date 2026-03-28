from Classe import Utilisateur
import secrets

# BASE DE DONNEES
user_base = []

# LOGIQUE METIER
def add_user():
    print("\n--- CRÉATION DE COMPTE ---")
    reponse = input("Vous ne possedez pas de compte. Voulez vous en créer un ? (Y/N): ").strip().upper()

    if reponse != "Y":
        print("Opération annulée.")
        exit()
    else :
        while True :
            nouveau_nom = input("Veuillez entrer un nom d'utilisateur : ").strip().capitalize()
            if not nouveau_nom:
                print("Le nom ne peut pas être vide.")
                continue
            if any (u.nom == nouveau_nom for u in user_base):
                print("Ce nom d'utilisateur existe déjà. Veuillez choisir un autre nom.")
                continue
            break
        while True :
            nouveau_mdp = input("Veuillez maintenant entrer votre mot de passe : ").strip()
            if len(nouveau_mdp) < 8:
                print("Mot de passe trop court.")
            else:
                break
        # CREATION OBJET et STOCKAGE en DB
        salt = secrets.token_hex(16)
        nouvel_utilisateur = Utilisateur(nouveau_nom, nouveau_mdp, salt)
        user_base.append(nouvel_utilisateur)
        print(f"Votre compte a bien été crée {nouveau_nom} !")

def verif_mdp(user_obj):
    print(f"\nBonjour {user_obj.nom} !")
    for essai in range(1,4):
        mdp_entre = input(f"Essai{essai}/3 - Veuillez entrer votre mot de passe : ")

        if user_obj.verifier_mdp(mdp_entre):
            print(f"Accès autorisé. Bienvenue {user_obj.nom}.")
            return
        else :
            print(f"Accès refusé, mot de passe incorrect.")

    print("Compte temporairement bloqué.")

def auth():
    print("\n---CONNEXION---")
    nom_entre = input("Nom d'utilisateur : ").strip().capitalize()
    utilisateur_trouve = next((u for u in user_base if u.nom == nom_entre), None)
    if utilisateur_trouve:
        verif_mdp(utilisateur_trouve)
    else :
        print("Utilisateur inconnu.")
        add_user()