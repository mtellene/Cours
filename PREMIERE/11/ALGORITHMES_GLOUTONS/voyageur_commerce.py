def voyageur_commerce(villes, distances, indice_depart):
    """
      Renvoie le circuit trouvé par la methode gloutonne et le coût associé
      :param villes: liste de villes à visiter
      :param distances: matrice des distances entre les villes
      :param indice_depart: indice de la ville de départ
      :return circuit: liste contenant le circuit à effectuer
      :return distance_parcourue: coût total du circuit
    """
    n = len(villes)
    visitees = [False] * n
    circuit = []
    
    courante = ....................................
    
    circuit.append(....................................)
    
    distance_parcourue = ....................................
    
    for _ in range(n-1):
        
        visitees[courante] = ....................................
        
        suivante = ....................................
        
        distance_parcourue = ....................................
        
        courante = suivante
        
        circuit.append(....................................)
        
    distance_parcourue = ....................................
    
    circuit.append(....................................)
    
    return circuit, distance_parcourue
