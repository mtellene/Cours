import matplotlib.pyplot as plt
from time import time


def mesure_temps (n):
    m = "a" * (n//2)
    t = "b" * n

    debut = time()
    premiere_recherche(m, t)
    fin = time()
    duree_pr = ................

    debut = time()
    deuxieme_recherche(m, t)
    fin = time()
    duree_dr = ................
    return ................, ................


def test():
    L = [4000, 8000, 16000, 36000, 64000, 128000, 256000]
    duree_pr = []
    duree_dr = []
    for elt in L:
        x, y = mesure_temps(elt)

        # ajout des temps dans les tableaux associés, TODO

    return ................, ................

def line_plot(pr, dr):
    x = [4000, 8000, 16000, 36000, 64000, 128000, 256000]
    courbe1 = pr
    courbe2 = dr

    _, ax = plt.subplots()
    ax.plot(x, courbe1, label ="première recherche")
    ax.plot(x, courbe2, label ="deuxième recherche")
    plt.title("Première recherche vs Deuxième recherche")
    ax.legend()

    plt.show()