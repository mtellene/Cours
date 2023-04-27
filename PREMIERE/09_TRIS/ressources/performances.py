from time import time
import matplotlib.pyplot as plt


def mesure_temps(n):
    print(f"début pour n={n}")

    l_croissante, l_decroissante, l_non_triee = generateur(n)
    l_croissante_c = l_croissante.copy()
    l_decroissante_c = l_decroissante.copy()
    l_non_triee_c = l_non_triee.copy()

    debut = time()
    ... # test de la fonction de la fonction tri_insertion sur un tableau croissant
    fin = time()
    d_inser_croissant = fin - debut

    debut = time()
    ... # test de la fonction de la fonction tri_insertion sur un tableau décroissant
    fin = time()
    d_inser_decroissante = ...

    debut = time()
    ... # test de la fonction de la fonction tri_insertion sur un tableau aléatoire
    fin = time()
    d_inser_non_trie = ...

    debut = time()
    ... # test de la fonction de la fonction tri_selection sur un tableau croissant
    fin = time()
    d_selec_croissant = ...

    debut = time()
    ... # test de la fonction de la fonction tri_selection sur un tableau décroissant
    fin = time()
    d_selec_decroissante = ...

    debut = time()
    ... # test de la fonction de la fonction tri_selection sur un tableau aléatoire
    fin = time()
    d_selec_non_trie = ...

    print(f"fin pour n={n}")
    return d_inser_croissant, d_inser_decroissante, d_inser_non_trie, d_selec_croissant, d_selec_decroissante, d_selec_non_trie


def test():
    L = [50, 100, 200, 500, 1000, 2000]
    durees_inser_cr = []
    durees_inser_dr = []
    durees_inser_nt = []
    durees_selec_cr = []
    durees_selec_dr = []
    durees_selec_nt = []
    for elt in L:
        d_inser_cr, d_inser_dr, d_inser_nt, d_selec_cr, d_selec_dr, d_selec_nt = .... # lancer mesure_temps avec elt éléments
        durees_inser_cr.append(d_inser_cr)
        durees_inser_dr.append(d_inser_dr)
        durees_inser_nt.append(d_inser_nt)
        durees_selec_cr.append(d_selec_cr)
        durees_selec_dr.append(d_selec_dr)
        durees_selec_nt.append(d_selec_nt)
    return durees_inser_cr, durees_inser_dr, durees_inser_nt, durees_selec_cr, durees_selec_dr, durees_selec_nt

def line_plot(durees_inser_cr, durees_inser_dr, durees_inser_nt, durees_selec_cr, durees_selec_dr, durees_selec_nt):
    x = [50, 100, 200, 500, 1000, 2000]
    courbe1 = durees_inser_cr
    courbe2 = durees_inser_dr
    courbe3 = durees_inser_nt

    courbe4 = durees_selec_cr
    courbe5 = durees_selec_dr
    courbe6 = durees_selec_nt

    _, ax = plt.subplots()
    ax.plot(x, courbe1, label ="Insertion croissant") # ici on ajoute les valeurs de courbe1 au graphique avec le nom "Insertion croissant"
    ax.plot(x, ..., label =...) # ajouter les valeurs de courbe2 avec le nom "Insertion décroissant"
    ax.plot(x, ..., label =...) # ajouter les valeurs de courbe3 avec le nom "Insertion non trié"
    ax.plot(x, ..., label =...) # ajouter les valeurs de courbe4 avec le nom "Sélection croissant"
    ax.plot(x, ..., label =...) # ajouter les valeurs de courbe5 avec le nom "Sélection décroissant"
    ax.plot(x, ..., label =...) # ajouter les valeurs de courbe6 avec le nom "Sélection non trié"
    plt.title("Tri insertion vs Tri sélection")
    ax.legend()

    plt.show()


... # lancement de test et récupération des résultats
... # création du graphique avec line_plot