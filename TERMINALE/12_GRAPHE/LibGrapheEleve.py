""" Classe Python pour des graphes non orienté
LG nov 2016 and fev 2020 - mis à jour juillet 2020 - MT mai 2023
adapté de http://www.python-course.eu/graphs_python.php
"""

from copy import deepcopy
# pour le graphe au format png
from graphviz import Digraph


debug = False

class Error(Exception):
    """Classe de base pour les exceptions dans ce module"""
    pass

class GraphError(Error):
    """Exception levée pour les boucles"""

    def __init__(self, message):
        self.message = message


class Graphe:

    def __init__(self, graph_dict=None):
        """ 
            Initialise un objet de la classe Graphe
            Si pas de dictionnaire ou None donné,
            un dictionnaire vide sera utilisé.

            :param graph_dict: dictionnaire d'adjacence du graphe
        """
        pass
        # mise en place de l'attribut __graph_dict contenant le dictionnaire d'adjacence

    
    def verification_integrite(self):
        """
            Vérification de l'intégrité du graphe : si s1->s2 alors s1->e2
            :return: True si le graphe est intègre, False sinon
        """
        pass

    
    def liste_sommets(self):
        """
            Renvoie les sommets du graphe
            :return: liste des sommets du graphe
        """
        pass
    

    def liste_aretes(self):
        """
            Renvoie les arêtes du graphe
            Attention l'arête {s1, s2} est le même que l'arête {s2, s1}
            :return: liste des arête du graphe - de la forme {s1, s2}
        """
        pass


    def voisin(self, sommet):
        """ 
            Renvoie les voisins d'un sommet
            :param sommet: un sommet du graphe
            :return: liste des voisins de sommet
        """
        pass

    
    def ajouter_sommet(self, sommet):
        """
            Ajoute un sommet au graphe.
            Si le sommet "sommet" n'est pas dans le graphe, 
            une clé "sommet" avec une liste vide comme valeur
            est ajoutée au dictionnaire.
            Sinon, rien n'est fait.

            :param sommet: sommet à ajouter
        """
        pass

    
    def ajouter_arete(self, arete):
        """ 
            Ajoute une arêtes dans le graphe.
            Vous utiliserez une structure try ... except

            :param arete: arête à ajouter - de la forme (s1, s2)
            Attention : l'arête ne doit pas être (s1,s1)
        """
        pass

        #try:
            # recupérer les deux sommets de l'arête à ajouter
            # si les deux sommets sont les mêmes
                # raise une GraphError avec le message "pas de boucle"
            
            # si au moins un des deux sommet n'est pas dans le graphe
                # raise une GraphError avec le message "sommet non présent"
            
            # si s2 est dans les voisins de s1
                # raise une GraphError avec le message "arête déjà présent"
            # sinon on ajoute de l'arête
            
            # si s1 est dans les voisins de s2
                # raise une GraphError avec le message "arête déjà présent"
            # sinon on ajoute de l'arête

        # décommenter et laisser ces lignes
        #except GraphError as s:
        #    print(f"problème avec l'ajout de l'arête : {s.message}")
        #    pass

    
    def __str__(self):
        """"
            Méthode d'affichage
            Ne pas modifier
        """
        res = "Sommets: "
        for sommet in self.__graph_dict:
            res += str(sommet) + " "
        res += "\nArêtes: "
        for arete in self.liste_aretes():
            res += str(arete) + " "
        return res

    
    def suppression_sommet(self, sommet):
        """
            Supprime un sommet et toutes ses arêtes
            :param sommet: sommet à supprimer

            Attention : si on supprime s1->s2, il faut aussi modifier s2->s1
            Vous pourrez utiliser "del" pour supprimer le sommet
        """
        pass

    
    def suppression_arete(self, arete):
        """
            Supprime une arête dans le graphe
            :param arete: arête à supprimer
            
            Pour rappel, une arête est de la forme (s1, s2)
        """
        pass


    def parcours_profondeur_iteratif(self, depart):
        """
            Parcours en profondeur itératif avec une pile
            :param depart: sommet de départ du parcours en profondeur
            :return: liste des sommets parcourus par le parcours profondeur
        """
        pass
    

    def est_atteignable_de(self, s1, s2):
        """
            Indique si deux sommets sont atteignables
            :param s1: et :param s2: sommets à prendre en compte
            :return: True si s2 est atteignable à partir de s1, False sinon  
        """
        pass

    
    def chemin(self, s1, s2):
        """
            Renvoie le chemin entre s1 et s2
            :param s1: et :param s2: sommets entre lesquels il faut trouver un chemin
            :return: chemin entre s1 et s2 (si possible), si impossible on renverra une liste vide
        """
        pass
    

    def parcours_largeur_iteratif(self, depart):
        """
            Parcours en largeur itératif avec une file
            :param depart: sommet de départ du parcours en largeur
            :return: liste des sommets parcourus par le parcours largeur
        """
        pass


    def composant_connexe(self):
        """
            Recherche de composant connexe
            :return: une liste par composant connexe
        """
        pass

    
    def print_dot(self, name="toto", colors={}):
        """
            Utilise graphvitz pour créer une image (png) du graphe
            Attention, il faut la libraire graphviz
        """
        foo = ['red', 'blue', 'green', 'yellow'] + (['black'] * 10)
        dot = Digraph(comment=name, format='png')  # change into pdf if you want.
        for k in self.__graph_dict:
            if not (colors):
                dot.node(str(k), str(k), color="red")
            else:
                dot.node(str(k), str(k), color=foo[colors[k]])
        for edge in self.liste_aretes():
            (v1, v2) = list(edge)[0], list(edge)[1]
            dot.edge(str(v1), str(v2), dir="none")
        if debug:
            print(dot.source)
        dot.render(name, cleanup=True)

    
