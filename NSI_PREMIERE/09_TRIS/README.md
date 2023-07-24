# TP - Algorithmes de tri

## I - Création de l'environnement de travail

## II - Création des fonctions de vérification

## III - Création des fonctions de vérification
### 1. Tri insertion
### 2. Pour tester vos fonctions
### 3. Tri sélection

## IV - Comparaison de performances

## V - Pour aller plus loin
### 1. Tri à bulles
#### i/ Principe
### 2. Tri rapide
#### i/ Principe




---

## I - Création de l'environnement de travail

Avant de commencer le TP, vous allez créer votre environnement de travail. Pour ce faire vous allez dans votre dossier personnel. Une fois arrivé, créer un dossier **TP_tris**. C'est dans ce dossier que vous sauvegarderez les exercices de ce TP.


## II - Création des fonctions de vérification

Vous allez commencer créer un fichier ```tris.py``` et écrire une fonction ```est_trie()```. Cette fonction prend en argument un tableau et renvoie ```True``` si le tableau est trié, ```False``` sinon.

Exemples :

```python
>>> est_trie([1,2,3])
True
>>> est_trie([3,2,1])
False
>>> est_trie([1,1,1])
True
>>> est_trie([1])
True
>>> est_trie([])
True
```

En plus de cette fonction ```est_trie()```, vous écrirez une fonction ```nb_occ()``` qui prend en argument un tableau et renvoie le dictionnaire des occurrences correspondant.


Exemples :

```python
>>> nb_occ([1,2,2])
{1 : 1, 2 : 2}
>>> nb_occ([1,1,1])
{1 : 3}
>>> nb_occ([1])
{1 : 1}
>>> nb_occ([])
{}
```

Ces deux fonctions **devront** être utilisées afin de tester vos algorithmes de tri.


## III - Programmation des méthodes

### 1. Tri insertion

Le tri par insertion considère chaque élément de la liste et l'insère à la bonne place parmi les éléments déjà triés. Ainsi, au moment où on considère un élément, les éléments qui le précèdent sont déjà triés, tandis que les éléments qui le suivent ne sont pas encore triés.

Pour trouver la place où insérer un élément parmi les précédents, il faut le comparer à ces derniers, et les décaler afin de libérer une place où effectuer l'insertion. Le décalage occupe la place laissée libre par l'élément considéré. En pratique, ces deux actions s'effectuent en une passe, qui consiste à faire  "remonter" l'élément au fur et à mesure jusqu'à rencontrer un élément plus petit.

Exemple du tri insertion :

![Exemple tri insertion](https://github.com/mtellene/NSI/blob/main/PREMIERE/09_TRIS/asset/ex_tri_insertion.png)


Pour vous aider, il vous est conseillé d'écrire une fonction ```permutation()``` qui prend en argument un tableau et deux indices (```x``` et ```y``` par exemple). La fonction renvoie le tableau où les éléments aux indices ```x``` et ```y``` ont été permutés.

```python
>>> L = [9, 7, 2, 5, 10, 1, 6, 4, 3, 8]
>>> permutation(L, 0, 5)
[1, 7, 2, 5, 10, 9, 6, 4, 3, 8]
```

Une fois fait, écrire une fonction ```insertion()``` qui prend en argument un tableau et un indice (```x``` par exemple). La fonction doit renvoyer le tableau où l'élément à l'indice ```x``` est insérer au bon endroit. Dans l'exemple ci-dessous, les étapes intermédiaires ont été affichées.

```python
>>> L = [9, 7, 2, 5, 10, 1, 6, 4, 3, 8]
>>> insertion(L, 5)
[9, 7, 2, 5, 1, 10, 6, 4, 3, 8]
[9, 7, 2, 1, 5, 10, 6, 4, 3, 8]
[9, 7, 1, 2, 5, 10, 6, 4, 3, 8]
[9, 1, 7, 2, 5, 10, 6, 4, 3, 8]
[1, 9, 7, 2, 5, 10, 6, 4, 3, 8]
[1, 9, 7, 2, 5, 10, 6, 4, 3, 8] #c'est le renvoi
```

Enfin, écrire une fonction ```tri_insertion()``` qui prend en argument un tableau. La fonction doit renvoyer le tableau trié en suivant la méthode du tri insertion.

```python
>>> L = [9, 7, 2, 5, 10, 1, 6, 4, 3, 8]
>>> tri_insertion(L)
# ici on affiche toutes les étapes du tri
[7, 9, 2, 5, 10, 1, 6, 4, 3, 8]
[2, 7, 9, 5, 10, 1, 6, 4, 3, 8]
[2, 5, 7, 9, 10, 1, 6, 4, 3, 8]
[2, 5, 7, 9, 10, 1, 6, 4, 3, 8]
[1, 2, 5, 7, 9, 10, 6, 4, 3, 8]
[1, 2, 5, 6, 7, 9, 10, 4, 3, 8]
[1, 2, 4, 5, 6, 7, 9, 10, 3, 8]
[1, 2, 3, 4, 5, 6, 7, 9, 10, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # ici c'est le renvoi
```


### 2. Pour tester vos fonctions

Vous trouvez un fichier ```generation_tableau.py```. Ce fichier contient une fonction ```generateur(n)``` qui génère 3 tableaux de *n* éléments : 

- un tableau trié par ordre croissant
- un tableau trié par ordre décroissant
- un tableau trié aléatoirement

### 3. Tri sélection

Sur une liste ```L``` de *n* éléments (numérotés de 0 à *n-1*), le principe du tri par sélection est le suivant :

- rechercher le plus petit élément parmi \texttt{L[0;n-1]}, et l'échanger avec l'élément \texttt{L[0]} ;
    
- rechercher le plus petit élément parmi \texttt{L[1;n-1]}, et l'échanger avec l'élément \texttt{L[1]} ;
    
- continuer de cette façon jusqu'à ce que la liste soit entièrement triée.

Exemple du tri sélection :

![Exemple tri sélection](https://github.com/mtellene/NSI/blob/main/PREMIERE/09_TRIS/asset/ex_tri_selection.png)


Pour vous aider, il vous est conseillé d'écrire une fonction ```minimum()``` qui prend en argument un tableau et un indice ```x```. La fonction renvoie l'indice de l'élément de valeur minimale du tableau à partir de l'indice ```x```.

```python
>>> L = [9, 7, 2, 5, 10, 1, 6, 4, 3, 8]
>>> minimum(L, 6)
8
```


En vous servant de ```minimum``` et possiblement de ```permutation```, écrire une fonction ```tri\_selection()``` qui prend en argument un tableau. La fonction doit renvoyer le tableau trié en suivant la méthode du tri sélection.

```python
>>> L = [9, 7, 2, 5, 10, 1, 6, 4, 3, 8]
>>> tri_selection(L)
# ici on affiche toutes les étapes du tri
[1, 7, 2, 5, 10, 9, 6, 4, 3, 8]
[1, 2, 7, 5, 10, 9, 6, 4, 3, 8]
[1, 2, 3, 5, 10, 9, 6, 4, 7, 8]
[1, 2, 3, 4, 10, 9, 6, 5, 7, 8]
[1, 2, 3, 4, 5, 9, 6, 10, 7, 8]
[1, 2, 3, 4, 5, 6, 9, 10, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # ici c'est le renvoi
```


## IV - Comparaison de performances

Le but de cette partie est de comparer les deux méthodes via un graphique. Ajouter le contenu du fichier ```performances.py```. Compléter les "..." afin de rendre le code fonctionnel. Le résultat devrait être (approximativement) le graphique ci-dessous.

![Rendu graphique](https://github.com/mtellene/NSI/blob/main/PREMIERE/09_TRIS/asset/performances.png)
    

Dans un second temps, nous allons afficher seulement les courbes des deux méthodes l'une après l'autre. Commencer par afficher les trois courbes du tri insertion, puis les trois courbes du tri sélection.

Enfin, nous allons comparer les méthodes en fonction du tableau donné. Afficher d'abord les courbes des tableaux croissants, puis décroissants et enfin aléatoires.

--------------------------------------------------------

## V - Pour aller plus loin


### 1. Tri à bulles

Le tri à bulles ou tri par propagation est un algorithme de tri. Il consiste à comparer répétitivement les éléments consécutifs d'un tableau, et à les permuter lorsqu'ils sont mal triés. Il doit son nom au fait qu'il déplace rapidement les plus grands éléments en fin de tableau, comme des bulles d'air qui remonteraient rapidement à la surface d'un liquide.

Le tri à bulles est souvent enseigné en tant qu'exemple algorithmique, car son principe est simple. Mais c'est le plus lent des algorithmes de tri communément enseignés, et il n'est donc guère utilisé en pratique.

#### i/ Principe

L'algorithme parcourt le tableau et compare les éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l'ordre, ils sont permutés.

Après un premier parcours complet du tableau, le plus grand élément est forcément en fin de tableau, à sa position définitive. En effet, aussitôt que le plus grand élément est rencontré durant le parcours, il est mal trié par rapport à tous les éléments suivants, donc permuté avec le suivant jusqu'à arriver à la fin du parcours.

Après le premier parcours, le plus grand élément étant à sa position définitive, il n'a plus à être traité. Le reste du tableau est en revanche encore en désordre. Il faut donc le parcourir à nouveau, en s'arrêtant à l'avant-dernier élément. Après ce deuxième parcours, les deux plus grands éléments sont à leur position définitive. Il faut donc répéter les parcours du tableau, jusqu'à ce que les deux plus petits éléments soient placés à leur position définitive.

Écrire une fonction ```tri_bulle()``` réalisant ce principe de tri


### 2. Tri rapide

En informatique, le tri rapide ou tri pivot (en anglais quicksort) est un algorithme de tri inventé par C.A.R. Hoare en 1961 et fondé sur la méthode de conception diviser pour régner. Il est généralement utilisé sur des tableaux, mais peut aussi être adapté aux listes. Dans le cas des tableaux, c'est un tri en place mais non stable.

La complexité moyenne du tri rapide pour *n* éléments est proportionnelle à *n log n*, ce qui est optimal pour un tri par comparaison, mais la complexité dans le pire des cas est quadratique. Malgré ce désavantage théorique, c'est en pratique un des tris les plus rapides, et donc un des plus utilisés. Le pire des cas est en effet peu probable lorsque l'algorithme est correctement mis en œuvre et il est possible de s'en prémunir définitivement avec la variante Introsort.

Le tri rapide ne peut cependant pas tirer avantage du fait que l'entrée est déjà presque triée. Dans ce cas particulier, il est plus avantageux d'utiliser le tri par insertion ou l'algorithme smoothsort.

#### i/ Principe

La méthode consiste à placer un élément du tableau (appelé pivot) à sa place définitive, en permutant tous les éléments de telle sorte que tous ceux qui sont inférieurs au pivot soient à sa gauche et que tous ceux qui sont supérieurs au pivot soient à sa droite.

Cette opération s'appelle le partitionnement. Pour chacun des sous-tableaux, on définit un nouveau pivot et on répète l'opération de partitionnement. Ce processus est répété récursivement, jusqu'à ce que l'ensemble des éléments soit trié.

Concrètement, pour partitionner un sous-tableau :

- le pivot est placé à la fin (arbitrairement), en l'échangeant avec le dernier élément du sous-tableau ;
- tous les éléments inférieurs au pivot sont placés en début du sous-tableau ;
- le pivot est déplacé à la fin des éléments déplacés.

Écrire une fonction ```tri_rapide()``` réalisant ce principe de tri

