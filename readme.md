# Projet jeu du pendu

#### Guillaume REB

## Principe
L'objectif de ce projet est d'implémenter le jeu du pendu. 
Un mot secret est choisi parmi une liste de mots existante, et un mot masqué est affiché, en masquant les lettres inconnues par le joueur. A chaque tour, le joueur doit proposer une lettre, si le mot secret contient cette lettre alors elle devient visible dans le mot masqué, sinon il perd un essai. Le joueur gagne s'il trouve l'ensemble des lettres du mot avant d'épuiser son nombre maximum de tentatives.

## Utilisation 
Le jeu est implémenté dans le fichier `projet_pendu.py`. 
Il se lance avec la commande
>python projet_pendu.py
Il utilise une liste de mots contenue dans le fichier `mots_pendu.txt`, qui doit se trouver dans le même dossier que le fichier python. Ces mots doivent être séparés par un saut de ligne (caractère "\n").
Le joueur a le droit a 6 erreurs lors de l'entrée des lettres. Ce nombre peut être modifié en changeant la valeur de la variable *nb_chances*. 
