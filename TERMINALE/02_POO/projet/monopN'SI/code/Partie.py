from Plateau import Plateau
from Terrain import Terrain

class Partie:

    def __init__(self, liste_joueur):
        """
            Constructeur de Partie
        """


    def avoir_joueur_avec_nom(self, nom):
        """
            Renvoie le joueur ayant pour nom nom
        """


    def choix_action(self, joueur):
        """
            Différents choix que peut faire le joueur joueur lors de son tour
        """


    def deplacement(self, joueur):
        """
            Déplace le joueur sur le plateau et renvoie la case sur laquelle le joueur est arrivé
        """


    def traitement_post_deplacement(self, joueur, case):
        """
            Une fois que le joueur s'est déplacé, fait le traitement (cf. le sujet)
            
             Aide : isinstance(case, Terrain) -> True si case est de la classe Terrain, False sinon
        """


    def tour(self, joueur):
        """
            Tour du joueur
            La méthode est faite, pas besoin de la modifier
        """
        print(f"Tour de {joueur.nom}")
        print()
        
        self.choix_action(joueur)
        case_joueur = self.deplacement(joueur)
        self.traitement_post_deplacement(joueur, case_joueur)


    def joueur_faillite(self):
        """
            Renvoie True si un joueur a fait faillite
            
            Rappel : un joueur ayant 0 sur son compte n'est pas en faillite
        """


    def prochain_joueur(self, indice_joueur_actuel):
        """
            Renvoie l'indice du prochain joueur
            La méthode est faite, pas besoin de la modifier
        """
        if indice_joueur_actuel == len(self.liste_joueur)-1:
            return 0
        return indice_joueur_actuel + 1


    def definir_gagnant(self):
        """
            Renvoie le joueur gagnant, celui qui a le plus gros compte à la fin de la partie
        """

