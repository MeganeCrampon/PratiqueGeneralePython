class Utilisateur:
    def __init__(self, nom, mdp):
        self.__nom = nom
        self.__mdp = mdp

    @property
    def nom(self):
        return self.__nom
    def verifier_mot_de_passe(self, mdp_test):
        return self.__mdp == mdp_test