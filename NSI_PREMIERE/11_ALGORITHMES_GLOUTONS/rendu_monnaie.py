def rendu_monnaie_glouton_v1(liste_pieces, montant):
    """
    Résoud le problème du rendu de monnaie avec une approche gloutone

    :param liste_pieces: liste des pièces disponibles, la liste doit être triée de manière décroissante
    :param montant: montant à rendre
    :return: liste des pièces à rendre
    """
    
    resultat = ............

    indice_piece = 0

    while montant > ............: #quand est-ce que l'algorithme s'arrête ?
    
        if montant < ............[............]:
        
            ............ = ............ + 1 #on passe à la pièce suivante
        else:
            #on ajoute la pièce à la solution
            
            .............append(............[............])
            
            #on retire la pièce prise du montant
            
            ............ = ............ - ............[............]
    
    #on retourne la solution trouvée
    
    return ............
