import math
import random

liste = []

def affichage(mot):
    for lettre in mot:
        if liste.__contains__(lettre):
            print(lettre, end="")
        else:
            print("_", end="")
    print()

def affichageVie(NombreDeVie):
    print(f"Il vous reste {NombreDeVie} vies")


def jouer():
    mot = input("Entrez votre mot : ").strip()
    print(mot)

    vie = 10
    listeTrouve=[]
    while vie > 0 :
        lettre =input("Entrez une lettre :")
        if mot.__contains__(lettre):
            print("trouvé")
            listeTrouve.append(lettre)
            # Cela ne marche que s'il n'y a pas de lettre en double dans le mot
            if len(listeTrouve) == len(mot):
                print("WIN")
                break

        else:
            print("FAUX")
            vie=vie-1

        liste.append(lettre)
        print(liste)
        affichage(mot)
        affichageVie(vie)

        if vie == 0:
            print("GAME OVER")




jouer()