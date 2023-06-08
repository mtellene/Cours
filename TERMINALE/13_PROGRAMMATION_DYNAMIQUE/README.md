## Dossier pour la programmation dynamique

## TP Programmation dynamique

### I - Organisation

### II - Suite de Fibonacci
#### 1. Algorithme récursif
#### 2. Programmation dynamique
#### 3. Comparaison des méthodes

### III - Rendu de monnaie
#### 1. Description du problème
#### 2. Algorithme glouton
#### 3. Programmation dynamique

### IV - Sac à dos
#### 1. Description du problème
#### 2. Algorithme glouton
#### 3. Programmation dynamique

----------------------------------


## TP Programmation dynamique


### I - Organisation

**Conseil d'organisation : il vous est conseillé pour ce TP de créer dans votre dossier personnel, un dossier "programmation dynamique". C'est ce dossier qui contiendra le travail demandé lors de ce TP.**


### II - Suite de Fibonacci

Créer un fichier **fibonacci.py**. C'est dans ce fichier que sera à faire le travail de cette partie.

#### 1. Algorithme récursif

🖥️ Écrire une fonction récursive ```fibo_rec(n)``` qui calcule le rang *n* de la suite de Fibonacci.

#### 2. Programmation dynamique

Bien que l'implémentation d'un algorithme récursif afin de calculer un certain rang de la suite de Fibonacci soit simple, celui-ci reste limité. En effet lorsque l'on lance l'appel suivant par exemple :

```python
fibo_rec(35)
```

Le programme commence à mettre longtemps à calculer la réponse. Cela peut très vite se comprendre lorsque l'on réalise l'arbre d'appels de notre fonction :

![arbre appels fibonacci](https://github.com/mtellene/NSI/blob/main/TERMINALE/13_PROGRAMMATION_DYNAMIQUE/asset/arbre_rec_fibo.png)

Sur le schéma, on peut voir que le calcul de ```fibo_rec(3)``` et ```fibo_rec(4)``` se font plusieurs fois. C'est pour cela qu'à partir de *n = 35* le temps d'exécution est important : des mêmes calculs sont effecutés plusieurs fois.

Une implémentation de Fibonacci suivant le principe de la programmation dynamique permet de réduire le temps d'exécution en se souvenant des calculs déjà effectués. Les calculs effectués seront mis dans un tableau. Ceci nous permettra de rendre plus rapide le calcul du résultat final. Ainsi, au lieu de faire des appels récursifs pour calculer ```fibo_rec(n-1) + fibo_rec(n-2)```, nous ferons simplement des appels à ```fibo_tab[n-1] + fibo_tab[n-2]```. Nous ferons donc chaque calcul une seule fois. De plus, l'accès à un tableau est **beaucoup plus rapide** qu'un appel récursif, ce qui améliorera le temps d'exécution de notre fonction.

🖥️ Écrire une fonction ```fibo_pg(n)``` qui calcule le rang *n* de la suite de Fibonacci. Cette fonction devra suivre le principe de la programmation dynamique.

Une fois la fonction finie, réaliser les appels suivants (il est à noter que les appels ci-dessous ne sont pas réalisables avec l'algorithme récursif) :

```python
fibo_pg(100)
fibo_pg(500)
fibo_pg(1000)
fibo_pg(10000)
fibo_pg(100000)
```

📝 Indiquer ce que produit le dernier appel. Que pouvez-vous en conclure ?


#### 3. Comparaison des méthodes

Nous allons comparer nos deux méthodes. Pour ce faire, nous allons faire une étude en temps. Copier le code suivant, coller le dans votre fichier Python et exécuter votre fichier.

```python
import matplotlib.pyplot as plt

def mesure_temps(n):
    print(f"n = {n}")

    debut = time()
    fibo_rec(n)
    temps_rec = time() - debut

    debut = time()
    fibo_pg(n)
    temps_pg = time() - debut

    return temps_rec, temps_pg


def test():
    duree_rec = []
    duree_pg = []
    for n in range(37):
        drec, dpg = mesure_temps(n)
        duree_rec.append(drec)
        duree_pg.append(dpg)
    return duree_rec, duree_pg


def line_plot(duree_rec, duree_pg):
    x = [i for i in range(37)]
    c1 = duree_rec
    c2 = duree_pg

    _, ax = plt.subplots()
    ax.plot(x, c1, label = "Récursive")
    ax.plot(x, c2, label = "Prog Dyna")

    plt.title("Récursivité vs Prog Dynamique (Fibonacci)")
    ax.legend()
    plt.show()

d1, d2 = test()
line_plot(d1, d2)
```

📝 Dessiner les courbes obtenues.
📝 Que pouvez-vous remarquer ? 


### III - Rendu de monnaie

Créer un fichier **rendu_monnaie.py**. C'est dans ce fichier que sera à faire le travail de cette partie.


#### 1. Description du problème

Le problème du rendu de monnaie est un problème d'algorithmique. Il s'énonce de la façon suivante : étant donné un système de monnaie (pièces et billets), comment rendre une somme donnée de façon optimale, c'est-à-dire avec le nombre minimal de pièces et billets ?

Par exemple, la meilleure façon de rendre 7 euros est de rendre un billet de cinq et une pièce de deux, même si d'autres façons existent (rendre 7 pièces de un euro, par exemple).

Ce problème est NP-complet dans le cas général, c'est-à-dire difficile à résoudre mais facile à vérifier. En effet détrminer la solution optimale n'est pas une tâche aisée mais vérifier qu'une solution est correcte est simple : il suffit de faire la somme des pièces rendues et de vérifier que cette dernière est bien égale au montant à rendre.

Une première idée serait de lister toutes les possibilités de rendre un certain montant avec les pièces à disposition et d'utilisation la possibilité utilisant le moins de pièces. Ceci est la démarche *force brute*. Cette idée est réalisable sur les petite instance du problème : pas beaucoup de pièces à disposition et un petit montant à rendre. Cependant sur les grandes instances du problème, cette démarche est totalement irréalisable.


#### 2. Algorithme glouton

🖥️ Écrire une fonction ```rendu_monnaie_ag(liste_pieces, montant)``` qui renvoie le nombre optimal de pièces à rendre, mais aussi le détail du rendu, pour le montant ```montant``` avec les pièces de ```liste_pieces```. Votre fonction devra suivre le principe glouton. Vous savez que sur certaines instances de ce problème, les algorithmes gloutons ne permettent pas de donner une solution (cf. ```liste_pieces = [4,3,2]``` et ```montant = 6```). Ainsi, pour déterminer si votre algorithme a trouvé une solution optimale, il faudra renvoyer (en plus du nombre de pièces et du détail), le montant à rendre restant. Si celui-ci est égal à *0*, alors votre algorithme aura trouvé une solution acceptable, sinon la solution ne sera pas acceptable.

Pour rappel, le principe de l'algorithme glouton sur le problème du rendu de monnaie est le suivant : on prend les pièces de la plus grande à la plus petite.

- si on peut prendre la pièce, on la prend (on fait ce qui en découle) et on recommence

- si on ne peut pas prendre la pièce, alors on passe à la pièce suivante

- on recommence tant qu'il reste des pièces et que le montant est non nul


📝 Refaire le tableau et le compléter en réalisant les appels approprié :

| ```liste_pieces``` | ```montant``` | ```resultat``` | Solution optimale ? |
|:-:|:-:|:-:|:-:|
| ```[4,3,1]``` | ```6``` | | |
| ```[3,2,1]``` | ```6``` | | |
| ```[5,3,2]``` | ```6``` | | |
| ```[50,20,10,5,2,1]``` | ```9``` | | |
| ```[50,20,10,5,2,1]``` | ```47``` | | |
| ```[18,7,1]``` | ```21``` | | |

#### 3. Programmation dynamique

**À noter :** certains systèmes de monnaie dits canoniques, l'algorithme glouton est optimal, c'est-à-dire qu'il suffit de rendre systématiquement la pièce ou le billet de valeur maximale — ce tant qu'il reste quelque chose à rendre. C'est la méthode employée en pratique, ce qui se justifie car la quasi-totalité des systèmes ayant cours dans le monde sont canoniques. Il n'existe pas, à ce jour, de caractérisation générale des systèmes canoniques, mais il existe une méthode efficace pour déterminer si un système donné est canonique.

Comme dit précédemment, on remarque que sur certaines instances, le rendu de monnaie version gloutonne ne donne pas la solution optimale et des fois, pas de solution du tout. Nous allons donc programmer un algorithme suivant le principe de la programmation dynamique pour parer à ces problèmes.

Pour rappel, la programmation dynamique consiste à se souvenir des calculs intermédiaires afin de calculer une solution finale.

🖥️ Écrire une fonction ```rendu_monnaie_pg(liste_pieces, montant)``` qui renvoie le nombre optimal de pièces à rendre, mais aussi le détail du rendu, pour le montant ```montant``` avec les pièces de ```liste_pieces```. Cette fonction devra suivre le principe de la programmation dynamique.

🖥️ Une fois fait, tester votre fonction sur les appels réalisés sur l'algorithme glouton. 


### IV - Sac à dos

Créer un fichier **sac_a_dos.py**. C'est dans ce fichier que sera à faire le travail de cette partie.


#### 1. Description du problème


Le problème du sac à dos, parfois noté (KP) (de l'anglais Knapsack Problem) est un problème d'optimisation combinatoire. Il consiste à trouver la combinaison d'éléments la plus précieuse à inclure dans un sac à dos, étant donné un ensemble d'éléments décrits par leurs poids et valeurs.

L'objectif du problème du sac à dos est de sélectionner des objets à mettre dans le sac à dos de façon à **maximiser la somme des valeurs des objets pris, sous la contrainte que le poids total des objets pris ne dépasse pas la capacité du sac à dos**. Ce problème est NP-complet. Ainsi, il est difficile à résoudre, en particulier pour les grands ensembles d'objets.

Une première approche serait, comme pour le rendu de monnaie, considérer toutes les possibilités respectant la contrainte de poids. Une fois fait, il suffirait de regarder quelle solution donne la meilleure somme.

📝 Expliquer pourquoi cette méthode est totalement irréalisable ?


#### 2. Algorithme glouton

🖥️ Écrire une fonction ```sad_ag(objets, capacite_max)``` qui renvoie la liste des objets pris, la valeur du sac et le poids du sac. Il est possible que pour la solution donnée, on a : ```poids(sac_a_dos) < capacite_max```. Avant de vous lancer dans la résolution, il faudra trier les objets selon l'un des critères suivants :

- par valeur (du plus cher au moins cher)
- par poids (du moins lourd au plus lourd)
- par rapport valeur/poids (:fire:), généralement, c'est méthode qui donne les meilleurs résultats

**Attention :** il est à noter que ```objets``` est un dictionnaire de dictionnaires. Cela implique que pour cette instance :

| **Objet** | **Poids** | **Valeur** |
|:-:|:-:|:-:|
| A | 3 | 2700 |
| B | 7 | 9100 |
| C | 1 | 200 |
| D | 4 | 4800 |
| E | 6 | 7200 |
| F | 2 | 2600 |


La variable ```objets``` sera :

```python
objets = {
    "A" : {"poids": 3, "valeur": 2700},
    "B" : {"poids": 7, "valeur": 9100},
    "C" : {"poids": 1, "valeur": 200},
    "D" : {"poids": 4, "valeur": 4800},
    "E" : {"poids": 6, "valeur": 7200},
    "F" : {"poids": 2, "valeur": 2600}
}
```

Pour rappel, le problème du sac à dos est résolu de manière gloutonne de la façon suivante : on considère les objets par ordre décroissant de valeur.

- si on peut prendre l'objet, on le prend (on fait ce qui en découle) et on continue

- si on ne peut pas prendre l'objet, alors on passe au suivant

- on fait ça tant qu'il reste des objets ou que poids du sac à dos est égal à la capacité maximale

Une fois l'algorithme écrit, testez le sur les instances suivantes, vous indiquerez si la solution renvoyée est optimale :

1.

```python
objets = {
    "A" : {"poids": 3, "valeur": 8},
    "B" : {"poids": 7, "valeur": 13},
    "C" : {"poids": 3, "valeur": 10},
    "D" : {"poids": 4, "valeur": 12}
}

capacite_max = 6
```

2.

```python
objets = {
    "A" : {"poids": 4, "valeur": 300},
    "B" : {"poids": 5, "valeur": 4000},
    "C" : {"poids": 8, "valeur": 4800},
    "C" : {"poids": 1, "valeur": 500}
}

capacite_max = 10
```


3.

```python
objets = {
    "A" : {"poids": 5, "valeur": 3500},
    "B" : {"poids": 1, "valeur": 500},
    "C" : {"poids": 6, "valeur": 4800},
    "C" : {"poids": 4, "valeur": 3000}
}

capacite_max = 10
```


#### 3. Programmation dynamique

Résolvons maintenant ce problème en utilisant la programmation dynamique.

🖥️ Écrire une fonction ```sad_pg(objets, capacite_max)``` qui renvoie la liste des objets pris, la valeur du sac et le poids du sac. Il est possible que pour la solution donnée, on a : ```poids(sac_a_dos) < capacite_max```. Cette fonction devra suivre le principe de la programmation dynamique.

Voici la démarche suivie par la programmation dynamique pour résoudre ce problème (cf. cela se passe à peu près de la même manière que pour le rendu de monnaie) :

1. on crée un tableau avec ```capacite + 1``` colonnes et ```nombre d'objets + 1``` lignes. La dernière ligne sert à mettre la somme obtenue

2. pour chaque ```sous_poids``` entre ```1``` et ```capacite_max + 1``` faire :

    1. fixer une variable ```opt``` qui va servir à se souvenir de la meilleure somme obtenue à chaque étape

    2. fixer une variable ```objet_pris``` qui va se souvenir du nom de l'objet pris

    3. pour chaque objet, regarder si on peut le prendre et si oui, s'il nous donne une meilleure somme

    4. une fois la somme optimale trouvée pour le ```sous_poids```, il faut mettre à jour le tablaau 

3. une fois que chaque solution optimale a été calculée pour chaque ```sous_poids```, mettre en place les différentes variables à renvoyer

Une fois fait, tester votre fonction sur les appels réalisés sur l'algorithme glouton et indiquer les différences notables.


