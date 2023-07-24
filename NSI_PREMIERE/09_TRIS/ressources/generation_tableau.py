from random import shuffle

def generateur(n):
    l_croissante = [k for k in range(n)]
    l_decroissante = [k for k in range(n-1,-1,-1)]
    l_non_triee = [k for k in range(n)]
    shuffle(l_non_triee)
    
    return l_croissante, l_decroissante, l_non_triee

