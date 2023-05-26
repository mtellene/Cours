# I - Le voyageur de commerce
# II - Le sac à dos

---

# I - Le voyageur de commerce 

Dans un premier TP, nous avons vu le principe des algorithmes gloutons. Nous avons appliqué ce principe pour résoudre le problème du rendu de monnaie. Il existe cependant d'autres problèmes qui peuvent être résolus en utilisant les algorithmes gloutons. Dans ce TP, nous nous intéresserons à la résolution du problème du voyageur de commerce.

## Rappel de la méthode gloutonne

Les algorithmes gloutons servent à résoudre des problèmes d'optimisations. Ces types de problèmes sont caractérisés par 3 points :

- ce sont des problèmes qui possèdent beaucoup de solutions
    
- on dispose d'une fonction mathématique permettant d'évaluer chaque solution
    
- on recherche une solution qui soit bonne, voire la meilleure


La résolution des problèmes d'optimisations avec des approches gloutonnes se fait de la manière suivante : à chaque étape de la résolution, on regarde la meilleure solution possible et on passe à l'étape suivante.


## Le problème du voyageur de commerce

Le problème du voyageur de commerce, ou problème du commis voyageur, est un problème d'optimisation qui consiste à déterminer, étant donné une liste de villes et les distances entre toutes les paires de villes, le circuit le plus court qui passe par chaque ville une et une seule fois.

Ce problème est un problème d'optimisation car :

- il existe beaucoup de solutions possibles : pour 4 villes, on aura $4! (4 \times 3 \times 2 \times 1$) chemins possibles
    
- on fait la somme des distances entre les villes du circuit pour connaître le coût total du circuit
    
- on recherche une solution qui soit bonne, voire la meilleure


## La méthode brute force

Dans un premier temps, nous allons résoudre le problème du voyageur de commerce en utilisant une méthode "brute force".


On considère le tableau des distances suivant :

| | Marseille | Strasbourg | Toulouse | Brest |
|:-:|:-:|:-:|:-:|:-:|
| Marseille | / | 500 | 275 | 650 |
| Strasbourg | 500 | / | 700 | 400 |
| Toulouse | 275 | 700 | / | 500 |
| Brest | 650 | 400 | 500 | / |


Le but est de relier toutes les villes entre elles afin de construire un circuit, une fois fait, il suffit de prendre le plus petit circuit en termes de distance. Pour se simplifier la tâche, nous allons nous fixer une ville de départ.

---

### Exercice :pencil:

Un circuit est donné, sur une feuille écrire tous les autres circuits possibles, avec le coût associé, ayant pour ville de départ Marseille :

- Marseille - Strasbourg - Toulouse - Brest - Marseille = 2350

Quel est le meilleur circuit ?

---


Comme pour le rendu de monnaie, cette méthode permettra à coup sûr de trouver la solution optimale du problème. **Mais** le nombre de possibilités est très important (essayez de trouver le circuit optimal avec un choix de 10 villes). Utiliser ce type d'algorithme est très coûteux à la fois en termes de temps de calcul et d'espace mémoire.

Il faut donc trouver un moyen plus efficace de raisonner.

Dans le cas du rendu de $9$ euros en monnaie, il est facile, pour un humain, de déterminer de tête cette façon optimale de faire, à savoir une pièce de $5$ euros et deux pièces de $2$ euros.

Mais comment programmer un algorithme pour qu'il y parvienne ?


## La méthode gloutonne

Une règle de choix permet d’obtenir une solution optimale d’une étape à la suivante. Ce choix est réalisé pour être le meilleur sur le moment, dans l'espoir que cela mène à une solution optimale pour le problème posé. En effet, un algorithme glouton ne revient jamais en arrière (il ne remet jamais en question les choix déjà effectués).

## Problème du voyageur de commerce


#### Énoncé du problème


Une agence de voyage proposant des tours entre différentes villes vous demande de créer un algorithme capable de calculer le circuit le plus court entre les villes. En effet, pour rester attractif, l'agence se doit de proposer les meilleurs prix possibles et donc elle doit économiser sur les prix de transport.

Pour cela, on considère le tableau des distances énoncé précédemment.

#### Règle de choix

1. on commence par se rendre à la ville la plus proche en termes de distance de la ville actuelle
    
2. on actualise la liste des villes visitées et le distance parcourue. Le nombre de villes à parcourir est plus petit qu'avant : le problème a été simplifié
    
3. on recommence le 1. jusqu'à avoir visité toutes les villes ; **attention, il ne faut pas repasser par une déjà visitée !**
    
4. une fois toutes les villes visitées, on revient à notre ville de départ
    
5. on renvoie la liste des villes visitées et la distance parcourue


#### Application à la main


On considère le tableau des distances précédent.

On utilise les notations suivantes :

```python 
a_visitee = ["Marseille", "Strasbourg", "Toulouse", "Brest"]

distances = [
    [float('inf'), 500, 275, 650],
    [500, float('inf'), 700, 400],
    [275, 700, float('inf'), 500],
    [650, 400, 500, float('inf')]
]

visitees = []
    
distance_totale = 0
    
ville_actuelle = ""
```

---
### Exercice

Sur feuille, détailler les étapes de recherche (avec cette stratégie gloutonne) du circuit. L'initialisation et la première étape sont données.

#### Initialisation

| ```ville_actuelle``` | ```visitees``` | ```distance_totale``` |
|:-:|:-:|:-:|
| Marseille | ```[]``` | 0 |

    
#### Étape 1
    
La ville actuelle est : Marseille.

| ```ville_actuelle``` | ```ville_plus_proche``` | ```visitees``` | ```distance_totale``` | nouvelle ```ville_actuelle``` |
|:-:|:-:|:-:|:-:|:-:|
| Marseille | Toulouse | ```["Toulouse"]``` | 275 | Toulouse |
    

On regarde ensuite la ville la plus proche de Toulouse
    

#### Étape 2
    
La ville actuelle est : Toulouse.

| ```ville_actuelle``` | ```ville_plus_proche``` | ```visitees``` | ```distance_totale``` | nouvelle ```ville_actuelle``` |
|:-:|:-:|:-:|:-:|:-:|
|  |  |  |  |  |
    

Quelle est la ville la plus proche ?
    

#### Étape 3
    

Quelle est la ville actuelle ?

| ```ville_actuelle``` | ```ville_plus_proche``` | ```visitees``` | ```distance_totale``` | nouvelle ```ville_actuelle``` |
|:-:|:-:|:-:|:-:|:-:|
|  |  |  |  |  |
    
Quelle est la ville la plus proche ?
    

#### Étape 4
    

Nous avons parcouru toutes les villes, il faut donc retourner à notre ville de départ :

| ```ville_actuelle``` | ```depart``` | ```visitees``` | ```distance_totale``` |
|:-:|:-:|:-:|:-:|
|  |  |  |  |  |
    
    
Nous avons terminé le circuit, nous retournons le circuit établi et la distance parcourue
    
- Quel est le contenu de la liste ```visitees``` ?
        
- Quelle est la valeur de ```distance_totale``` ?

---

## Un algorithme optimal ?

Comme pour le rendu de monnaie, l'application de la méthode gloutonne pour résoudre le problème du voyageur de commerce **ne donne pas obligatoirement** la meilleure solution et dans certains cas peut se retrouver bloqué.


Dans l'exemple suivant, déroulez, sur feuille, les étapes de recherche (par algorithme glouton) du circuit.

Indiquez ensuite si cette décomposition est optimale ou s'il est possible d'avoir un meilleur circuit.

---
#### Exemple n°1 :

```python
a_visitee = ["Lyon", "Saint-Étienne", "Grenoble", "Valence"]
    
distances = [
    [float('inf'), 64, 107, 102],
    [64, float('inf'), 150, 70],
    [107, 150, float('inf'), 100],
    [102, 70, 100, float('inf')]
]
    
distance_totale = 0
    
depart = "Saint-Étienne"
```

Au départ, la liste des villes visitées contient la ville de départ : ```visitees = ["Saint-Étienne"]```


On met également ```depart``` dans ```ville_actuelle``` : ```ville_actuelle = "Saint-Étienne"```



Quelle est la ville la plus proche ?


On met à jour les différents éléments de notre recherche de circuit :

- Quel est le contenu de ```visitee``` ?
    
- Quelle est la ```ville_actuelle``` ?
    
- Quelle est la valeur ```distance_parcourue``` ?



Quelle est la ville la plus proche de la nouvelle ville actuelle ?

On met à jour les différents éléments de notre recherche de circuit :

- Quel est le contenu de ```visitee``` ?
    
- Quelle est la ```ville_actuelle``` ?
    
- Quelle est la valeur ```distance_parcourue``` ?



Quelle est la ville la plus proche de la nouvelle ville actuelle ?

On met à jour les différents éléments de notre recherche de circuit :

- Quel est le contenu de ```visitee``` ?
    
- Quelle est la ```ville_actuelle``` ?
    
- Quelle est la valeur ```distance_parcourue``` ?




On a parcouru toutes les villes, on ajoute donc la ville ```depart``` dans notre circuit et on ajoute la distance de ```ville_actuelle``` à ```depart```.

On met à jour les différents éléments de notre recherche de circuit :

- Quel est le contenu de ```visitee``` ?
    
- Quelle est la valeur ```distance_parcourue``` ?


Quel est le circuit obtenu ? Le circuit est-il optimal ?

**À noter :** s'il existe un circuit plus court ayant une ville de départ différente, alors la solution trouvée n'est pas optimale.


## Un peu de code

### Création de l'environnement de travail

Dans votre dossier personnel, créez dans le dossier **algorithmes_gloutons**. Dans ce dossier, créez un fichier ```voyageur_commerce.py```. C'est dans ce fichier que vous ferez le travail demandé.

Soit le code suivant :

```python

villes = ["Marseille", "Strasbourg", "Toulouse", "Brest"]

distances = [
    [float('inf'), 500, 275, 650],
    [500, float('inf'), 700, 400],
    [275, 700, float('inf'), 500],
    [650, 400, 500, float('inf')]
]

visitees = [True, False, False, False]
# ici, on a visité Marseille mais pas Strasbourg, ni Toulouse et ni Brest
```

---
#### Exercice
Écrire une fonction ```plus_proche``` qui prend en argument l'indice d'une ville (issu de la liste de villes à visiter), le tableau des distances et la liste des villes visitées et qui renvoie l'indice de la ville la plus proche dans ```villes```.

``` python
# en considérant le code précédant
>>> plus_proche(0, distances, visitees)
2
# la ville la plus proche (ET non visitée) de villes[0] est villes[2]
```
---

Recopier et compléter la fonction ```voyageur_commerce``` dans le fichier ```voyageur_commerce.py```


Une fois la fonction écrite, faire les différents appels pour répondre aux questions

1.
```python
villes = ["Marseille", "Strasbourg", "Toulouse", "Brest"]

distances = [
    [float('inf'), 500, 275, 650],
    [500, float('inf'), 700, 400],
    [275, 700, float('inf'), 500],
    [650, 400, 500, float('inf')]
]
```
- Quel est le circuit obtenu ?        
- Quel est le coût de ce circuit ?
- Le circuit est-il optimal ?
    

2.
```python
villes = ["Lyon", "Orléans", "Lilles"]
        
distances = [
    [float('inf'), 450, 680],
    [450, float('inf'), 350],
    [680, 350, float('inf')]
]
```
- Quel est le circuit obtenu ?
- Quel est le coût de ce circuit ?
- Le circuit est-il optimal ?


3.
```python
villes = ["Paris", "Berlin", "Lisbonne", "Madrid", "Rome", "Londres", "Athènes"]
        
distances = [
    [float('inf'), 1050, 1730, 1275, 1420, 470, 2880],
    [1050, float('inf'), 2780, 2320, 1500, 1100, 2330],
    [1730, 2780, float('inf'), 625, 2500, 2190, 3800],
    [1275, 2320, 625, float('inf'), 1960, 1730, 3250],
    [1420, 1500, 2500, 1960, float('inf'), 1860, 1270],
    [470, 1100, 2190, 1730, 1860, float('inf'), 1980],
    [2880, 2330, 3800, 3250, 1270, 1980, float('inf')]
]
```
- Quel est le circuit obtenu ?
- Quel est le coût de ce circuit ?
- Le circuit est-il optimal ?


4.
```python
villes = ["Paris", "New York", "Tokyo", "Johannesburg"]
        
distances = [
    [float('inf'), 5835, 14831, 12416],
    [5835, float('inf'), 10845, 12832],
    [14831, 10845, float('inf'), 13537],
    [12416, 12832, 13537, float('inf')]
]
```

- Quel est le circuit obtenu ?
- Quel est le coût de ce circuit ?
- Le circuit est-il optimal ?


### II - Sac à dos

Créer un fichier **sac_a_dos.py**. C'est dans ce fichier que sera à faire le travail de cette partie.


#### 1. Description du problème


Le problème du sac à dos, parfois noté (KP) (de l'anglais Knapsack Problem) est un problème d'optimisation combinatoire. Il consiste à trouver la combinaison d'éléments la plus précieuse à inclure dans un sac à dos, étant donné un ensemble d'éléments décrits par leurs poids et valeurs.

L'objectif du problème du sac à dos est de sélectionner des objets à mettre dans le sac à dos de façon à **maximiser la somme des valeurs des objets pris, sous la contrainte que le poids total des objets pris ne dépasse pas la capacité du sac à dos**. Ce problème est NP-complet. Ainsi, il est difficile à résoudre, en particulier pour les grands ensembles d'objets.

Une première approche serait, comme pour le rendu de monnaie, considérer toutes les possibilités respectant la contrainte de poids. Une fois fait, il suffirait de regarder quelle solution donne la meilleure somme.

Pourquoi cette méthode est totalement irréalisable ?

Si l'on considère *N* objets, il y a alors 2<sup>*N*</sup> combinaisons possibles.

Le soucis est que s'il y a 2<sup>*N*</sup> possibilités, cela augmente très vite.

- avec *N = 10*, on a *1 024* possibilités

- avec *N = 20*, on a *1 048 576* possibilités

- avec *N = 60*, on a *1 152 921 504 606 846 976* possibilités

- avec *N = 300*, il a plus de combinaisons possibles qu'il y a d'atomes dans l'univers visible !

#### 2. Algorithme glouton

Écrire une fonction ```sad_ag(objets, capacite_max)``` qui renvoie la liste des objets pris, la valeur du sac et le poids du sac. Il est possible que pour la solution donnée, on a : ```poids(sac_a_dos) < capacite_max```. Il faudra au préalable **trier les objets selon l'un des critères suivants** :

- par valeur (du plus cher au moins cher)
- par poids (du moins lourd au plus lourd)
- par rapport valeur/poids (:fire:)

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

- si on peut prendre l'objet, on le prend (et on fait ce qui en découle) et on continue

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
