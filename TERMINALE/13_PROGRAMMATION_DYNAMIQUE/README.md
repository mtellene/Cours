## Dossier pour la programmation dynamique

## TP Programmation dynamique

### I - Organisation

### II - Suite de Fibonacci
#### 1. Algorithme récursif
#### 2. Programmation dynamique
#### 3. Comparaison des méthodes

### III - Rendu de monnaie
#### 1. Algorithme glouton
#### 2. Programmation dynamique
#### 3. Comparaison des méthodes

### IV - Sac à dos
#### 1. Algorithme glouton
#### 2. Programmation dynamique

----------------------------------

## TP Programmation dynamique

### I - Organisation

**Conseil d'organisation : il vous est conseillé pour ce TP de créer dans votre dossier personnel, un dossier "programmation dynamique". C'est ce dossier qui contiendra le travail demandé lors de ce TP.**

### II - Suite de Fibonacci

Créer un fichier **fibonacci.py**. C'est dans ce fichier que sera à faire le travail de cette partie.

#### 1. Algorithme récursif

Écrire une fonction récursive ```fibo_rec(n)``` qui calcule le rang *n* de la suite de Fibonacci.


#### 2. Programmation dynamique

Bien que l'implémentation d'un algorithme récursif afin de calculer un certain rang de la suite de Fibonacci soit simple, celui-ci reste limité. En effet lorsque l'on lance l'appel suivant par exemple :

```python
fibo_rec(35)
```

Le programme commence à mettre longtemps à calculer la réponse. Cela peut très vite se comprendre lorsque l'on réalise l'arbre d'appels de notre fonction :

![arbre appels fibonacci](https://github.com/mtellene/NSI/blob/main/TERMINALE/13_PROGRAMMATION_DYNAMIQUE/asset/arbre_rec_fibo.png)

Sur le schéma ci-contre, on peut voir que le calcul de ```fibo_rec(3)``` et ```fibo_rec(4)``` se font plusieurs fois. C'est pour cela qu'à partir de *n = 35* le temps d'exécution est important : des mêmes calculs sont effecutés plusieurs fois.

Une implémentation de Fibonacci suivant le principe de la programmation dynamique permet de réduire le temps d'exécution en se souvenant des calculs déjà effectués.

Pour ce faire, au lieu de faire des appels récursifs pour calculer ```fibo_rec(n-1) + fibo_rec(n-2)```, nous ferons simplement des appels à ```fibo_tab[n-1] + fibo_tab[n-2]```. L'accès à un tableau est **beaucoup plus rapide** qu'un appel récursif.

Écrire une fonction ```fibo_pg(n)``` qui calcule le rang *n* de la suite de Fibonacci. Cette fonction devra suivre le principe de la programmation dynamique.

Une fois la fonction finie, réaliser les appels suivants (il est à noter que les appels ci-dessous ne sont pas réalisables avec l'algorithme récursif) :

```python
fibo_pg(100)
fibo_pg(500)
fibo_pg(1000)
fibo_pg(10000)
fibo_pg(100000)
```

Indiquer ce que produit le dernier appel.

#### 3. Comparaison des méthodes

Nous allons comparer nos deux méthodes. Pour ce faire, nous allons faire une étude en temps. Copier le code suivant, coller le dans votre fichier Python et exécuter votre fichier.

```python
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

Que pouvez-vous remarquer ? 


### III - Rendu de monnaie

Créer un fichier **rendu_monnaie.py**. C'est dans ce fichier que sera à faire le travail de cette partie.

#### 1. Algorithme glouton

Écrire une fonction ```rendu_monnaie_ag(liste_pieces, montant)``` qui renvoie le nombre optimal de pièces à rendre, mais aussi le détail du rendu, pour le montant ```montant``` avec les pièces de ```liste_pieces```.

Tester votre fonction sur les appels suivants :

| ```liste_pieces``` | ```montant``` | ```resultat``` | Solution optimale ? |
|:-:|:-:|:-:|:-:|
| ```[4,3,1]``` | ```6``` | | |
| ```[3,2,1]``` | ```6``` | | |
| ```[5,3,2]``` | ```6``` | | |
| ```[50,20,10,5,2,1]``` | ```9``` | | |
| ```[50,20,10,5,2,1]``` | ```47``` | | |
| ```[18,7,1]``` | ```21``` | | |

#### 2. Programmation dynamique

On remarque que sur certaines instances, le rendu de monnaie version gloutonne ne donne pas la solution optimale et des fois, pas de solution du tout. Nous allons donc programmer un algorithme suivant le principe de la programmation dynamique.

Pour rappel, la programmation dynamique consiste à se souvenir des calculs intermédiaires afin de calculer une solution finale.

Écrire une fonction ```rendu_monnaie_pg(liste_pieces, montant)``` qui renvoie le nombre optimal de pièces à rendre, mais aussi le détail du rendu, pour le montant ```montant``` avec les pièces de ```liste_pieces```. Cette fonction devra suivre le principe de la programmation dynamique.

Une fois fait, tester votre fonction sur les appels réalisés sur l'algorithme glouton. 

### IV - Sac à dos

Créer un fichier **sac_a_dos.py**. C'est dans ce fichier que sera à faire le travail de cette partie.



#### 1. Algorithme glouton

#### 2. Programmation dynamique


