from time import time

#todo
def puissance_naive(a,n):
    """Calcule a^n en remultipliant par a successivement
    a et n : int
    sortie : int
    """
    resultat = 1
    
    #todo
    
    return resultat
    

#todo
def puissance_rapide(a,n):
    """Calcule a^n en utilisant le principe de l'exponentiation rapide
    a et n : int
    sortie : int
    """
    resultat = 1
    
    #todo
    
    return resultat
    
    
### Fonction de test 
def test(f):
    """ fonction de test
    f : fonction
    sortie : True si f renvoie la même chose que **, False sinon
    """
    b = True
    L = [1,2,4,8,16,32,64,128,256,512,1024]
    for i in range(10):
        b = b and f(2,i) == L[i]
    return b


### Décommenter et utiliser cette fonction quanvos fonctions de clcul de puissances sont prètes.

# def eval_des_perf(a,n):
#     """Cette fonction permet quelles fonction puissance calcule le plus vite"""
#     
#     
#     print('Test de la méthode naive :')
#     d = time()
#     puissance_naive(a,n)
#     a = time()
#     print(f"Les tests de la méthode naïve ont pris : {a-d} secondes")
#     
#     print("---------------------------")
#     
#     print('Test de la méthode rapide :')
#     d = time()
#     puissance_rapide(a,n)
#     a = time()
#     print(f"Les tests de la méthode rapide pour régner ont pris : {a-d} secondes")
