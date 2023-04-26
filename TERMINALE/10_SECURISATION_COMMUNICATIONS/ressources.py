def recherche_automatique(d):
    f = open("tous_les_mots.txt", "r")
    ligne = ....... #permet de récupérer une ligne du fichier texte
    while ligne != ......: #tant que le fichier n'est pas terminé
        for (k,v) in ........: #on parcourt le dictionnaire par les éléments
            if v == ligne.upper()[:-1]: print(k) #si on a trouvé un mot qui existe en français, on affiche la clé associée
        ligne = ........ #on passe à la ligne suivante
