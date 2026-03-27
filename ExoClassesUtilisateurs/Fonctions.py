from Classe import Utilisateur

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
        nouvel_utilisateur = Utilisateur(nouveau_nom, nouveau_mdp)
        user_base.append(nouvel_utilisateur)
        print(f"Votre compte a bien été crée {nouveau_nom} !")

def verif_mdp():
    print(f"\nBonjour {Utilisateur.nom} !")
    essai = 0
    mdp_entre = input("Veuillez entrer votre mot de passe : ")
    while True :
        if mdp_entre != Utilisateur.mdp:
            essai += 1
            print(f"Accès refusé. Au bout de 3 essais le compte sera temporairement bloqué. Essai {essai}/3.")
            if essai == 3:
                print("\nTrop de tentatives. Votre compte est temporairement bloqué.")
                break
        else :
            print(f"Accès autorisé. Bienvenue {Utilisateur.nom}.")
            return

def auth():
    print("\n---CONNEXION---")
    nom_entre = input("Veuillez entrer votre nom d'utilisateur : ").strip().capitalize()
    utilisateur_trouve = next((u for u in user_base if u.nom == nom_entre), None)
    if utilisateur_trouve:
        verif_mdp(utilisateur_trouve)
    else :
        print("Nom d'utilisateur inconnu.")
        add_user()