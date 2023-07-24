def lecture_colonne_v2(liste_colonnes):
    """
    ouvre le fichier, parcourt la liste en argument et retient les colonnes qui sont la liste, affiche enfin les colonnes demandées
    liste_colonnes : liste de noms de colonnes
    sortie : /
    """
    fichier = pandas.read_csv("highscore.csv")
    liste_colonnes_verifiees = []
    for col in ...:
        if ... in cols.columns:
            ....append(...)
    print(...[liste_colonnes_verifiees])


def lecture_n_premieres_lignes(n):
    """
    affiche les n+1 premières lignes du fichier
    n : nombre de lignes à lire
    sortie : /
    """
    fichier = pandas.read_csv("highscore.csv")
    fichier = fichier.loc[...]
    print(fichier)
