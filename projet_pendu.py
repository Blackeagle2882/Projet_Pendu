import random

def choisir_mot(mots):
    return random.choice(mots)

with open("mots_pendu.txt","r") as f:
    mots = f.readlines()

# On utilise la fonction de choix de mots, et on retire le caractère de saut de ligne avec strip()
mot = choisir_mot(mots).strip()

# Nombre autorisé max d'échecs (rentrer une lettre non présente dans le mot)
nb_chances = 6

# Ici on stocke les lettres que l'utilisateur connait ('_' si la lettre n'est pas connue a une certaine position)
cache = ["_"] * len(mot)

# Fonction pour afficher facilement un mot 
def affiche(mot):
    for lettre in mot:
        print(lettre,end="")
    print()

while nb_chances > 0: # On s'arrête si il ne reste plus aucune chance
    print("Avancement: ")
    affiche(cache)
    print("Il vous reste",nb_chances,"chances")
    
    # On récupère la lettre choisie par l'utilisateur
    test = input("Veuillez entrer une lettre:")
    
    # Si l'entrée a plus de 1 caractere
    while len(test) > 1:
        test = input("Veuillez entrer une lettre à la fois")
        
    # Pour chaque lettre dans le mot secret
    for i in range( len(mot) ):
        # Si la lettre entrée est a cette position dans le mot secret, alors on la découvre dans la liste des lettres
        # que l'utilisateur connait
        if mot[i] == test:
            cache[i] = mot[i]
            
    # S'il n'y a plus aucune lettre inconnue, alors on a trouve le mot
    if "_" not in cache:
        print("Gagné!")
        print(mot)
        break 
    
    # Si la lettre entree n'est pas dans le mot, alors on perd une chance
    if test not in mot:
        nb_chances -= 1

# Si il y a encore une lettre inconnue, alors on a perdu
if "_" in cache:
    print("Perdu ! Le mot est",mot)
    