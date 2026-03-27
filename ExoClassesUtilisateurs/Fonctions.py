from Classe import Utilisateur

# BASE DE DONNEES
user_base = []

# LOGIQUE METIER
def add_user_mdp():
    nouveau_mdp = input(print("Veuillez maintenant entrer votre mot de passe : ")).strip()
    if nouveau_mdp(len) < 8:
        print("Mot de passe trop court.")
    else:
        nouveau_mdp_hash = hash(nouveau_mdp)
        Utilisateur.mdp.append(nouveau_mdp_hash)

def add_user():
    reponse = input(print("Vous ne possedez pas de compte. Voulez vous en créer un ? (Y/N): ")).strip().upper()
    if reponse == "Y":
        nouveau_nom = input(print("Veuillez entrer votre nouveau nom d'utilisateur : ")).strip().capitalize()
        Utilisateur.nom.append(nouveau_nom)
        add_user_mdp()
    elif reponse == "N":
        print("Au revoir.")
    else : 
        print("Désolé, saisie incorrecte.")

def verif_mdp():
    essai = 0
    mdp_entre = input(print("Veuillez maintenant entrer votre mot de passe : "))
    while True :
        if mdp_entre != Utilisateur.mdp:
            essai += 1
            print("Accès refusé. Au bout de 3 essais le compte sera temporairement bloqué.")
            if essai == 3:
                print("Trop de tentatives. Votre compte est temporairement bloqué.")
                break
        else :
            print(f"Accès autorisé. Bienvenue {Utilisateur.nom}.")

def auth():
    nom_entre = input(print("Veuillez entrer votre nom d'utilisateur : ")).strip().capitalize()
    if nom_entre != Utilisateur.nom:
        add_user()
    else :
        verif_mdp()