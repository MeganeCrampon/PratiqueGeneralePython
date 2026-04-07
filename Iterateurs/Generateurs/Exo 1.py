class SacADos:
    def __init__(self, objet):
        self.objet = objet
    def __iter__(self):
        return self
    def __next__(self):
        if not self.objet:
            raise StopIteration
        return self.objet.pop(0)
    def __str__(self):
        if not self.objet:
            return "Mon sac est vide"
        contenu = ", ".join(self.objet)
        return f"Mon sac contient : {contenu}"
    def __repr__(self):
        return f"SacADos({self.objet})"
    
mon_sac = SacADos(["Carte", "Potion", "Epee"])

print(mon_sac)
print("Je sors un(e)", next(mon_sac))
print("Je sors un(e)", next(mon_sac))
print("Je sors un(e)", next(mon_sac))
print(mon_sac)

"""for objet in mon_sac:
    print(f"Il me reste : {objet}")"""