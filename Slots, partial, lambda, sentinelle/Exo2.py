def distributeur(somme):
    while somme >=20:
        yield 20
        somme -= 20
    if somme > 0:
        yield somme 

for billet in distributeur(105):
    print(f"Le distributeur donne : {billet}")