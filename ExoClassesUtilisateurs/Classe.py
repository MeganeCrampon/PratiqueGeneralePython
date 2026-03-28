import hashlib
import secrets

class Utilisateur:
    def __init__(self, nom, salt, mdp_cru):
        self.__nom = nom
        self.__salt = salt
        self.__mdp_hash = self.prep_hash(mdp_cru)

    @property
    def nom(self):
        return self.__nom
    def prep_hash(self, mdp):
        return hashlib.sha256((mdp+self.__salt).encode()).hexdigest()
    def verifier_mot_de_passe(self, mdp_test):
        return self.__mdp_hash == self.__prep_hash(mdp_test)