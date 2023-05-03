# Fichier de test de la classe Graphe
# L & S Gonnord, 2016 - M Tellene, 2023
from LibGraphe import *

demo = False  # True pour tester la librairie


def main():
    g = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []
    }
    
    g2 = {
        "r3": ["r1", "r2"],
        "r2": ["r3", "r1", "c", "a"],
        "r1": ["r3", "r2", "c"],
        "c": ["r1", "r2", "b", "a", "d", "e"],
        "b": ["a", "c", "d", "e"],
        "e": ["b", "c", "d"],
        "a": ["b", "c", "d", "r2"],
        "d": ["a", "b", "c", "e"]
    }
    
    notagraph = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b"],
        "d": []  # problème ici
    }

    g3 = {
        "1": ["4", "3", "2"],
        "2": ["1", "7"],
        "3": ["1", "4", "5", "6"],
        "4": ["1", "3", "8"],
        "5": ["3", "6"],
        "6": ["3", "5", "7"],
        "7": ["2", "6"],
        "8": ["4"]
    }

    g4 = {
        "1": ["2", "7", "8"],
        "2": ["1", "3", "4"],
        "3": ["2", "8", "10"],
        "4": ["2", "8"],
        "5": ["6", "8", "9", "10", "11"],
        "6": ["5", "7", "8"],
        "7": ["1", "6", "9"],
        "8": ["1", "3", "4", "5", "6"],
        "9": ["5", "7", "11"],
        "10": ["3", "5"],
        "11": ["5", "9"]
    }

    g5 = {
        1: [2, 3],
        2: [1],
        3: [1],
        4: [5],
        5: [4, 6],
        6: [5],
        7: [8],
        8: [7]
    }  # l'affichage fonctionne aussi avec des sommets non str

    print("-------- Début des tests --------")
    print()

    if demo:  # demo des fonctions basiques de la lib
        print("### Création d'un graphe ###")
        graphe_error = Graphe(notagraph)
        print(f"Intégrité du graphe, devrait être False : {graphe_error.verification_integrite()}")

        print()
        
        print("### Création d'un graphe ###")
        graph = Graphe(g)
        print(f"Intégrité du graphe, devrait être True : {graph.verification_integrite()}")

        print(f"Sommet du graphe, devrait être ['a', 'b', 'c', 'd', 'e', 'f'] : {graph.liste_sommets()}")
        print(f"Arêtes du graphe, devrait être [{'d', 'a'}, {'a', 'z'}, {'b', 'c'}, {'d', 'c'}, {'c', 'e'}] : {graph.liste_aretes()}")

        print()
        
        print("Ajout du sommet z")
        graph.ajouter_sommet("z")
        print(f"Sommet du graphe, devrait être ['a', 'b', 'c', 'd', 'e', 'f', 'z'] : {graph.liste_sommets()}")

        print("Ajout de l'arête {'a', 'z'}")
        graph.ajouter_arete(("a", "z"))
        print("Ajout de l'arête {'a', 'a'}")
        graph.ajouter_arete(("a", "a"))
        print(f"Arêtes du graphe, devrait être [{'d', 'a'}, {'b', 'c'}, {'d', 'c'}, {'c', 'e'}] : {graph.liste_aretes()}")

        print()

        print("Ajout de l'arête {'x', 'y'}, avec de nouveaux sommets")
        graph.ajouter_arete({"x", "y"})
        print(f"Sommet du graphe, devrait être ['a', 'b', 'c', 'd', 'e', 'f', 'z'] : {graph.liste_sommets()}")
        print(f"Arêtes du graphe, devrait être [{'d', 'a'}, {'b', 'c'}, {'d', 'c'}, {'c', 'e'}] : {graph.liste_aretes()}")

        # Dessiner un graphe, si cela ne marche pas vous pouvez mettre l'instruction suivante en commentaire
        print("Génération du graphe au format PNG")
        graph.print_dot("graph")

    else:
        print("### Création d'un graphe ###")
        graph = Graphe(g)

        print("Ajout du sommet z")
        print("Ajout de l'arête {'a', 'z'}")
        graph.ajouter_sommet("z")
        graph.ajouter_arete(("a", "z"))

        print()

        print(f"Intégrité premier graphe ? {graph.verification_integrite()}")
        print("Génération du graphe au format PNG...")
        graph.print_dot("graph")
        print("Premier graphe, parcours en profondeur à partir de 'a'")
        print("Une réponse possible : ['a', 'z', 'd', 'c', 'e', 'b']")
        print(graph.parcours_profondeur_iteratif('a'))

        print()

        print("Premier graphe, parcours en profondeur à partir de d")
        print("Une réponse possible : ['d', 'c', 'e', 'b', 'a', 'z']")
        print(graph.parcours_profondeur_iteratif('d'))

        print()

        print("Premier graphe, chemin entre a et z")
        print("Une réponse possible : ['a', 'z']")
        print(graph.chemin("a", "z"))

        print("Premier graphe, chemin entre a et e")
        print("Une réponse possible : ['a', 'd', 'c', 'e']")
        print(graph.chemin("a", "e"))

        print("Premier graphe, chemin entre a et f")
        print("Une réponse possible : []")
        print(graph.chemin("a", "f"))

        print()

        print("Premier graphe, parcours en largeur à partir de d")
        print("Une réponse possible : ['d', 'a', 'c', 'z', 'b', 'e']")
        print(graph.parcours_largeur_iteratif('d'))

        print()

        print("Premier graphe, composants connexes")
        print("Devrait renvoyer : [['z', 'a', 'd', 'c', 'e', 'b'], ['f']]")
        print(graph.composant_connexe())

        print()
        print()

        print("### Création d'un graphe ###")
        graph2 = Graphe(g2)

        print()

        print("Génération du graphe au format PNG...")
        graph2.print_dot("graph2")

        print("Deuxième graphe, parcours en largeur à partir de r1")
        print("Une réponse possible : ['r1', 'r3', 'r2', 'c', 'a', 'b', 'd', 'e']")
        print(graph2.parcours_largeur_iteratif('r1'))

        print()
        print()

        print("### Création d'un graphe ###")
        graph3 = Graphe(g3)

        print()

        print("Génération du graphe au format PNG...")
        graph3.print_dot("graph3")


        print("Troisième graphe, parcours en profondeur à partir de 1")
        print("Une réponse possible : ['1', '2', '7', '6', '5', '3', '4', '8']")
        print(graph3.parcours_profondeur_iteratif("1"))

        print()

        print("Troisième graphe, parcours en largeur à partir de 1")
        print("Une réponse possible : ['1', '4', '3', '2', '8', '5', '6', '7']")
        print(graph3.parcours_largeur_iteratif('1'))

        print()
        print()

        print("### Création d'un graphe ###")
        graph4 = Graphe(g4)

        print()

        print("Génération du graphe au format PNG...")
        graph4.print_dot("graph4")

        print()
        
        print("Quatrième graphe, parcours en profondeur à partir de 1")
        print("Une réponse possible : ['1', '8', '6', '7', '9', '11', '5', '10', '3', '2', '4']")
        print(graph4.parcours_profondeur_iteratif("1"))


        print()

        print("Quatrième graphe, parcours en largeur à partir de 1")
        print("Une réponse possible : ['1', '2', '7', '8', '3', '4', '6', '9', '5', '10', '11']")
        print(graph4.parcours_largeur_iteratif("1"))


        print()

        print("Quatrième graphe, composants connexes")
        print("Devrait renvoyer : [['11', '9', '7', '6', '8', '5', '10', '3', '2', '4', '1']]")
        print(graph4.composant_connexe())


        print()
        print()

        print("### Création d'un graphe ###")
        graph5 = Graphe(g5)

        print()

        print("Génération du graphe au format PNG...")
        graph5.print_dot("graph5")

        print()
        
        print("Cinquième graphe, parcours en profondeur à partir de 4")
        print("Devrait renvoyer : [4, 5, 6]")
        print(graph5.parcours_profondeur_iteratif(4))


        print()

        print("Cinquième graphe, parcours en largeur à partir de 1")
        print("Une réponse possible : [1, 2, 3]")
        print(graph5.parcours_largeur_iteratif(1))

        print()

        print("Cinquième graphe, composants connexes")
        print("Devrait renvoyer : [[8, 7], [6, 5, 4], [3, 1, 2]]")
        print(graph5.composant_connexe())

    print("-------- Fin des tests --------")

        

if __name__ == '__main__':
    main()
