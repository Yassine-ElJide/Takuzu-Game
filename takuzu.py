
from fltk import rectangle, cercle, attend_clic_gauche, cree_fenetre, ferme_fenetre, texte, efface, mise_a_jour, efface_tout
import time


def charger_grille(nb):
    """
    Chargement d'un fichier txt contenant la grille et transformer son
    contenu en liste de liste qu'on on peut manipuler modifier après
    :param int nb: type de grille choisie
    :return: list : listes de listes représentant les lignes

    >>> charger_grille(4)
    [[' ', 1, ' ', 0], [' ', ' ', 0, ' '], [' ', 0, ' ', ' '], [1, 1, ' ', 0]]

    >>> charger_grille(6)
    [[' ', 0, ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', 1, ' ', 1, ' ', ' '], [' ', 0, ' ', ' ', ' ', ' '], [' ', 0, ' ', ' ', ' ', ' '], [0, 1, ' ', 0, ' ', 1, ' ']]
    """
    with open(f'grille{nb}.txt', 'r') as f:
        fichier_grille = f.readlines()
        plateau = []
        for ligne in fichier_grille:
            ligne = list(ligne)
            ligne.pop()  # Enlève le '\n' à la fin de chaque liste
            plateau.append(ligne)
        # Transforme tous les zéros et les uns de str  en int
        for lst in plateau:
            for i in range(len(lst)):
                if lst[i] == "0":
                    lst[i] = 0
                elif lst[i] == "1":
                    lst[i] = 1
        return plateau


def creation_colonnes(lignes):
    """
    Crée une liste de colonne à  partir d'une liste de ligne.
    :param lignes: liste de liste contenant la grille
    :return list : liste de de listes contenant les colonnes

    >>> creation_colonnes(charger_grille(4))
    [[' ', ' ', ' ', 1], [1, ' ', 0, 1], [' ', 0, ' ', ' '], [0, ' ', ' ', 0]]

    >>> creation_colonnes(charger_grille(6))
    [[' ', ' ', ' ', ' ', ' ', 0], [0, ' ', 1, 0, 0, 1], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 1, ' ', ' ', 0], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 1]]
    """
    colonnes = []
    for i in range(len(lignes[0])):
        n = [lignes[0][i]]
        for j in range(1, len(lignes)):
            n.append(lignes[j][i])
        colonnes.append(n)
    return colonnes


def plateau_graphique(nb):
    """
    Création du plateau du jeu en fonction du nombre de case que possède la grille donnée par ligne(nb)
    :param int nb: nombres de case par lignes

    """
    for h in range(0, 600, 600 // nb):
        for l in range(0, 600, 600 // nb):
            rectangle(l, h, l + (600 / nb), h + (600 / nb))


def remplissage_plateau_graphique(nb, lignes, symbole):
    """
    place les chiffres que contient la grille dans le plateau
    graphique en fonction du nombre de case que possède la grille
    par ligne(nb) et le symbole choisi par l'utilisateur.
    :param nb: nombres de cases par ligne
    :param lignes: liste de liste contenant la grille représentant les lignes
    :param symbole: symbole choisi par l'utilisateur (x/o, 1/0, noir/blanc )

    """
    efface("chiffre")

    # Affiche les 0 et les 1.
    if symbole == 1:
        for y in range(len(lignes)):
            for x in range(len(lignes[y])):
                # les chiffres bloqués sont affichés en noir
                if lignes[y][x] == 0:
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                          (600 / nb), "0", ancrage="center", tag="chiffre")
                elif lignes[y][x] == 1:
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                          (600/nb), "1", ancrage="center", tag="chiffre")
                # les chiffres modifiables sont affichés en vert
                elif lignes[y][x] == "0":
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                          (600/nb), "0", ancrage="center", couleur="green", tag="chiffre")
                elif lignes[y][x] == "1":
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                          (600/nb), "1", ancrage="center", couleur="green", tag="chiffre")

    # Affiche les jetons noirs et blancs.
    elif symbole == 2:
        for y in range(len(lignes)):
            for x in range(len(lignes[y])):
                if lignes[y][x] == 0 or lignes[y][x] == "0":
                    cercle((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                           (600/nb), 600 // (4*nb), remplissage="white", tag="chiffre")
                elif lignes[y][x] == 1 or lignes[y][x] == "1":
                    cercle((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                           (600/nb), 600 // (4*nb), remplissage="black", tag="chiffre")

    # Affiche les X et les 0.
    elif symbole == 3:
        for y in range(len(lignes)):
            for x in range(len(lignes[y])):
                # les symboles bloqués sont affichés en noir
                if lignes[y][x] == 0:
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) +
                          y * (600/nb), "O", ancrage="center", tag="chiffre")
                elif lignes[y][x] == 1:
                    texte((600 / (2*nb)) + x * (600/nb), (600 / (2*nb)) + y *
                          (600/nb), "X", ancrage="center", tag="chiffre")
                # les symboles modifiables sont affichés en vert
                elif lignes[y][x] == "0":
                    texte((600 / (2*nb)) + x*(600/nb), (600/(2*nb)) + y*(600/nb),
                          "O", ancrage="center", couleur="green", tag="chiffre")
                elif lignes[y][x] == "1":
                    texte((600/(2*nb)) + x*(600/nb), (600 / (2*nb)) + y * (600/nb),
                          "X", ancrage="center", couleur="green", tag="chiffre")
    mise_a_jour()


def modifier_valeur_graphique(x, y, nb, lignes):
    """
    Permt à l'utilisateur de changer la valeur des cases ou il a cliqué
    en prenant les coordonnées où il a cliqué (x, y) comme paramètre
    :param x: les coordonnées du clic par rapport à l'axe des abscisses
    :param y: les coordonnées du clic par rapport à l'axe des ordonnées
    :param lignes: liste de liste contenant la grille représentant les lignes
    :param nb: nombres de case par lignes

    """
    ligne = y // (600 // nb)
    colonne = x // (600 // nb)

    # Change la case sur laquelle l'utilisateur à cliqué en fonction de la valeur
    if lignes[ligne][colonne] == " ":
        lignes[ligne][colonne] = "0"
    elif lignes[ligne][colonne] == "0":
        lignes[ligne][colonne] = "1"
    elif lignes[ligne][colonne] == "1":
        lignes[ligne][colonne] = " "


def conditions_graphique(lignes, colonnes):
    """

    Vérifie les Conditions du jeu en mode graphique
    :param lignes: liste de liste contenant la grille représentant les lignes
    :param colonnes: liste de de listes représentant les colonnes

    """

    # Vérifie qu'il y a autant de 1 et de 0 dans chaque ligne et chaque colonne et qu'il n'y a aucune case vide.
    for ligne in lignes:
        lst = []
        nb_1 = 0
        nb_0 = 0
        for colonne in ligne:
            if colonne == " ":  # vérifie si aucune case n'est vide
                return False
            lst.append(colonne)
            if str(colonne) == "1":
                nb_1 += 1
            if str(colonne) == "0":
                nb_0 += 1
        if nb_0 != nb_1:  # vérifie si le nombre des 1 et de 0 sont égaux
            return False

    # Vérifie qu'il n'y est pas trois zéros ou trois uns les uns à côté des autres dans une ligne.
    for i in range(len(lignes)):
        for j in range(len(lignes[i]) - 2):
            if lignes[i][j] == lignes[i][j+1] == lignes[i][j+2]:
                return False

    # Vérifie qu'il n'y est pas trois zéros ou trois uns les uns à côté des autres dans une colonne.
    for i in range(len(colonnes)):
        for j in range(len(colonnes[i]) - 2):
            if colonnes[i][j] == colonnes[i][j+1] == colonnes[i][j+2]:
                return False

    # Vérifie qu'aucune ligne n'est identique à une autre.
    for i in range(len(lignes) - 1):
        if lignes[i] == lignes[i+1]:
            return False

    # Vérifie qu'aucune colonne n'est identique à une autre.
    for i in range(len(colonnes) - 1):
        if colonnes[i] == colonnes[i+1]:
            return False
        return True


def plateau_terminal(nb):
    """
    Permet l'affichage du la grille en terminal à l'aide d'une liste de liste générée par la
    fonction charger_grille
    :param int nb: type de grille choisie
    :return str plateau : plateau du jeu en mode terminal

    >>> plateau_terminal(4)
    ['| |1| |0|', '| | |0| |', '| |0| | |', '|1|1| |0|']

    >>> plateau_terminal(6)
    ['| |0| | | | |', '| | | | | | |', '| |1| |1| | |', '| |0| | | | |', '| |0| | | | |', '|0|1| |0| |1|']
    """
    plateau = charger_grille(nb)
    if nb == 4:
        for i in range(nb):
            plateau[i] = f'|{plateau[i][0]}|{plateau[i][1]}|{plateau[i][2]}|{plateau[i][3]}|'
    elif nb == 6:
        for i in range(nb):
            plateau[i] = f'|{plateau[i][0]}|{plateau[i][1]}|{plateau[i][2]}|{plateau[i][3]}|{plateau[i][4]}|{plateau[i][5]}|'
    elif nb == 8:
        for i in range(nb):
            plateau[i] = f'|{plateau[i][0]}|{plateau[i][1]}|{plateau[i][2]}|{plateau[i][3]}|{plateau[i][4]}|{plateau[i][5]}|{plateau[i][6]}|{plateau[i][7]}|'
    elif nb == 10:
        for i in range(nb):
            plateau[i] = f'|{plateau[i][0]}|{plateau[i][1]}|{plateau[i][2]}|{plateau[i][3]}|{plateau[i][4]}|{plateau[i][5]}|{plateau[i][6]}|{plateau[i][7]}|{plateau[i][8]}|{plateau[i][9]}|'
    return plateau


def conditions_terminal(nb, lignes, colonnes):
    """
        Vérifie les Conditions du jeu en mode terminal
        :param nb: nombre de cases par lignes
        :param lignes: liste de liste contenant la grille représentant les lignes
        :param colonnes: liste de de listes représentant les colonnes

    """

    # Lignes
    # Vérifie qu'il y est autant de un que de zéro sur une même ligne.
    for i in range(nb):
        nb_0 = lignes[i].count("0")
        if nb_0 != nb / 2:
            return False
        nb_1 = lignes[i].count("1")
        if nb_1 != nb / 2:
            return False

    # Vérifie qu'il n'y est pas trois un ou trois zéro les un à côté des autres.
    for i in range(len(lignes)):
        for c in range(1, len(lignes[i])//2, 2):
            if lignes[i][c] == lignes[i][c+2] == lignes[i][c+4]:
                return False

    # Vérifie qu'aucune ligne n'est identique à  une autre.
    for i in range(len(lignes) - 1):
        occ = lignes.count(lignes[i])
        if occ != 1:
            return False

    # colonnes
    # Vérifie qu'il y est autant de un que de zéro sur une même colonne.
    for compt in range(1, nb, 2):
        occurence0 = colonnes[compt].count("0")
        # Vérifie le nombre des zero.
        if occurence0 != nb / 2:
            return False
        occurence1 = colonnes[compt].count("1")
        # Vérifie le nombre des un.
        if occurence1 != nb / 2:
            return False

    # Vérifie qu'il n'y est pas trois un ou trois zéro les un à côté des autres.
    for i in range(1, len(colonnes), 2):
        for c in range(0, len(colonnes[i])//2):
            if colonnes[i][c] == colonnes[i][c+1] == colonnes[i][c+2]:
                return False

    # Vérifie qu'aucune colonne n'est identique à  une autre.
    for i in range(len(colonnes) - 1):
        occ = colonnes.count(colonnes[c])
        if occ != 1:
            return False
        return True


def modifier_valeur_terminal(lin, col, nb, lignes):
    """
       Permet à l'utilisateur de changer les valeurs de la grille en termibal
       :param str lin: la ligne choisie par l'utilisateur
       :param str col: la colonne choisie par l'utilisateur
       :param int nb: type de grille choisie
       :param list lignes: liste de liste contenant la grille représentant les lignes
    """
    for i in range(len(lignes)):
        # on remet les lignes en type liste pour pouvoir modifier les valeurs
        lignes[i] = list(lignes[i])

    valeur = input("Entrez 0 ou 1: ")
    while valeur != "0" and valeur != "1":
        print("On ne peut mettre que des 0 ou des 1")
        valeur = input("Entrez 0 ou 1: ")

    # On ajoute la saisie dans la liste de liste.
    lignes[int(lin)][2 * int(col) + 1] = valeur
    # On remet la liste de liste en liste de chaine de caractére pour que les conditions puisse être vérifiées.
    for i in lignes:
        i = "".join(i)
        print(i)


###########################
### PROGRAMME PRINCIPAL ###
###########################

print("""--------------------
| Welcome To Takuzu |
--------------------""")
print('Voici les règles du Takuzu : ')
print('1 - Chaque ligne et colonnes doit contenir autant de 0 que de 1,')
print('2 - Les lignes ou colonnes identiques sont interdites,')
print("3 - Il ne doit pas y avoir plus de deux 0 ou 1 placés l'un à coté ou en dessous de l'autre.")
print('-----------------------------------------------------')
print('A vous de jouer !')
print('-----------------------------------------------------', end='\n\n')

# Demande à l'utilisateur le type de grille qui veut et le mode du jeu
nb = int(input("Entrez le type de grille que vous voulez (4/6/8/10): "))
while not(nb == 4 or nb == 6 or nb == 8 or nb == 10):
    nb = int(input("Veuillez Choisir un de ces types(4/6/8/10): "))
choix = input(
    "Vous souhaitez jouer au Takuzu en mode terminal (T) ou en mode graphique (G): ")
choix = choix.lower()
while not(choix == "g" or choix == "t"):
    choix = input(
        "Tapez T pour le mode terminal ou G pour le mode graphique: ")
    choix = choix.lower()

# Mode Graphique
if choix == "g":
    print("Voulez-vous résoudre le takuzu avec:")
    print("1:des 0 et des 1")
    print("2:des jetons noirs et blancs")
    print("3:des cercle et des croix")
    symbole = int(input("Entrez votre choix: "))
    while not(symbole == 1 or symbole == 2 or symbole == 3):
        symbole = int(input("Choisissez 1, 2 ou 3: "))
    cree_fenetre(600, 600)
    plateau_graphique(nb)  # création du plateau avec des cases
    lignes = charger_grille(nb)  # listes de listes représentant les lignes
    # listes de listes représentant les colonnes
    colonnes = creation_colonnes(lignes)
    remplissage_plateau_graphique(nb, lignes, symbole)
    while not(conditions_graphique(lignes, colonnes)):
        # assigner l'endroit où l'ultisateur a cliqué à deux var x, y
        (x, y) = attend_clic_gauche()
        # permettre le changement des valeurs non existantes
        modifier_valeur_graphique(x, y, nb, lignes)
        remplissage_plateau_graphique(nb, lignes, symbole)
        colonnes = creation_colonnes(lignes)
    efface_tout()
    time.sleep(1)
    # On sort de la boucle si les conditions sont vérifiées et on affiche un texte
    texte(300, 300, "Bravo!", ancrage="center", couleur='red', taille=60)
    attend_clic_gauche()
    ferme_fenetre()


# Mode terminal
elif choix == "t":

    lignes = plateau_terminal(nb)
    # affichage du plateau pour que l'utilisateur puisse visualiser la grille avant de changer de valeur
    for i in lignes:
        ligne = "".join(i)
        print(ligne)

    print("\tPuisqu'on est en informatique, pour indiquer une case il suffit de donner le chiffre de la ligne et de la colonne en commençant de 0!!")
    print("Par exemple, la case (0,2) correspond à la troisième case de la première ligne")

    # Boucle du jeu
    while True:
        # On demande l'indice de la ligne et de la colonne à l'utilisateur.
        l = input("Entrer la ligne que vous voulez (chiffre): ")
        c = input("Entrer la colonne que vous voulez (chiffre): ")

        # Vérifie les coordonnées pour empêcher les coups impossibles.
        if nb == 4:
            while ((l == "0" and c == "1") or (l == "0" and c == "3") or (l == "1" and c == "2") or
                    (l == "2" and c == "1") or (l == "3" and c == "0") or (l == "3" and c == "0") or
                    (l == "3" and c == "3") or (l == "" or c == "") or (l > "3" or c > "3") or (l == " " or c == " ")):
                print(
                    "Case inéxistante ou non modifiable")
                l = input("Entrer la ligne que vous voulez (chiffre): ")
                c = input(
                    "Entrer la colonne que vous voulez (chiffre): ")

        if nb == 6:
            while ((l == "0" and c == "1") or (l == "0" and c == "2") or (l == "0" and c == "3") or
                    (l == "0" and c == "5") or (l == "1" and c == "0") or (l == "1" and c == "4") or
                    (l == "2" and c == "0") or (l == "3" and c == "2") or (l == "3" and c == "4") or
                    (l == "4" and c == "0") or (l == "4" and c == "3") or (l == "4" and c == "5") or
                    (l == "5" and c == "2") or (l == "5" and c == "5") or (l == " " or c == " ") or (l == "" or c == "") or (l > "5" or c > "5")):
                print(
                    "Case inéxistante ou non modifiable")
                l = input("Entrer la ligne que vous voulez (chiffre): ")
                c = input(
                    "Entrer la colonne que vous voulez (chiffre): ")

        if nb == 8:
            while ((l == "0" and c == "1") or (l == "0" and c == "7") or (l == "1" and c == "6") or
                    (l == "2" and c == "1") or (l == "2" and c == "3") or (l == "2" and c == "6") or
                    (l == "3" and c == "1") or (l == "3" and c == "6") or (l == "4" and c == "1") or
                    (l == "4" and c == "7") or (l == "5" and c == "0") or (l == "5" and c == "2") or
                    (l == "5" and c == "3") or (l == "5" and c == "4") or (l == "5" and c == "5") or
                    (l == "5" and c == "6") or (l == "6" and c == "4") or (l == "7" and c == "4") or
                    (l == "7" and c == "6") or (l == "7" and c == "7") or (l == "" or c == "") or
                    (l == " " or c == " ") or (l > "7" or c > "7")):
                print(
                    "Case inéxistante ou non modifiable")
                l = input("Entrer la ligne que vous voulez (chiffre): ")
                c = input(
                    "Entrer la colonne que vous voulez (chiffre): ")

        if nb == 10:
            while ((l == "0" and c == "2") or (l == "0" and c == "7") or (l == "0" and c == "8") or (l == "1" and c == "0") or
                    (l == "1" and c == "2") or (l == "1" and c == "4") or (l == "1" and c == "6") or (l == "1" and c == "7") or
                    (l == "2" and c == "0") or (l == "2" and c == "8") or (l == "3" and c == "0") or (l == "3" and c == "3") or
                    (l == "3" and c == "5") or (l == "3" and c == "8") or (l == "4" and c == "3") or (l == "4" and c == "9") or
                    (l == "5" and c == "0") or (l == "5" and c == "1") or (l == "5" and c == "4") or (l == "6" and c == "2") or
                    (l == "6" and c == "4") or (l == "6" and c == "5") or (l == "6" and c == "7") or (l == "6" and c == "9") or
                    (l == "7" and c == "0") or (l == "7" and c == "7") or (l == "7" and c == "9") or (l == "9" and c == "0") or
                    (l == "9" and c == "1") or (l == "9" and c == "5") or (l == " " or c == " ") or (l == "" or c == "") or
                    (l > "9" or c > "9")):
                print(
                    "Case inéxistante ou non modifiable")
                l = input(
                    "Entrer la ligne dans laquelle se trouve la case souhaitez (chiffre): ")
                c = input(
                    "Entrer la colonne dans laquelle se trouve la case souhaitez (chiffre): ")

        print(f'Vous avez choisi la case {(l, c)}')
        colonnes = creation_colonnes(lignes)
        modifier_valeur_terminal(l, c, nb, lignes)
        verification = conditions_terminal(nb, lignes, colonnes)
        if verification == True:
            print("Bravo!!!")
            break  # on sort de la boucle si les conditions sont vérifiées
