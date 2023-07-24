### Importation des modules :
from random import randint
from time import time

### liste de 100 éléments compris entre 0 et 99, sorted(...) sert à trier la liste
LISTE = sorted([randint(0,100) for k in range(100)])


### A vous de jouer :
#todo
def recherche_naive(L,N):
    """Recherche la présence de x dans la liste L en parcourant toute la liste de gauche à droite. 
    L : list ; x : int
    sortie : True si x dans L, False sinon"""
    return 1
    

#todo
def recherche_dicho(L,N):
    """Cette fonction fait la même chose que la précédente mais en employant la méthode diviser pour régner
    L : list ; x : int
    sortie : True ou False"""
    return 1
    


### Ne rien modifier ici :

def test_not_in_liste(f,L):
    """Teste si la fonction f donne le même résultat que la fonction in de Python sur les valeurs qui ne sont 
    pas sont dans la liste. 
    f : fonction à tester ; L : list
    sortie : True (si renvoie False, il y a un problème !)"""
    
    b = True
    for i in range(-10,110):
        if i not in L:
            b = b and f(L,i)
    return b

def test_in_liste(f,L):
    """Teste si la fonction f donne le même résultat que la fonction in de Python sur les valeurs qui ne sont 
    pas sont dans la liste. 
    f : fonction à tester ; L : list
    sortie : True (si renvoie False, il y a un problème !)"""
    
    b=True
    for n in L:
        
        b = b and f(L,n)
    return b
        

###Décommenter cette partie uniquement quand les fonctions recherche_dicho et recherche_naive sont finies et testées     

#   
# def eval_des_perf(N):
#     """Cette fonction permet des voir quelle fonction fait son travail le plus vite sur une liste de longueur
#     N"""
#     liste = sorted([randint(0,100) for k in range(N)])
#     
#     print('Test de la méthode naive :')
#     d = time()
#     for i in range(-50,150):
#         recherche_naive(liste,i)
#     a = time()
#     print(f"Les tests de la méthode naïve ont pris : {a-d} secondes")
#     
#     print("---------------------------")
#     
#     print('Test de la méthode diviser pour régner :')
#     d = time()
#     for i in range(-50,150):
#         recherche_dicho(liste,i)
#     a = time()
#     print(f"Les tests de la méthode diviser pour régner ont pris : {a-d} secondes")
#     
    
    
    
    
    
    
    
    
    
    
