def multiples_de_trois():
    x = 3
    while True:
        yield x
        x += 3

def afficher_multiples():
    generateur = multiples_de_trois()
    for i, multiple in enumerate(generateur, 1):
        print(f"Multiple n°{i} : {multiple}")
        if i == 5 :
            break

print("--- LES MULTIPLES DE 3 ---\n")
afficher_multiples()
