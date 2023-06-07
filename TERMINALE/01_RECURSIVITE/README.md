# TP - Récursivité

---

### Exercice 1

La somme des *n* premiers nombres entiers peut être implémentée à l'aide d'une boucle ```for``` très facilement :

```python
def somme_n_premiers_nb(n):
  s = 0
  for i in range(n+1):
    s += i
  return s
```

Un version plus « concise » existe en utilisant la récursivité.

🖥️ Écrire une fonction récursive ```somme_n_premiers_nb(n)``` qui renvoie la somme des *n* premiers nombres entiers.


### Exercice 2

La factorielle d'un nombre *n* correspond à l'opération *1x2x...xn*, c'est-à-dire le produit de tous les nombres positifs non nuls, inférieurs ou égaux à *n*.

🖥️ Écrire une fonction récursive ```factorielle(n)``` permettant de calculer la factorielle de *n*. La fonction devra renvoyer le résultat du calcul.


### Exercice 3

La récursivité permet, en plus de résoudre des problèmes mathématiques, de faire des opérations sur des structures de données. Cet exercice va s'intéresser à la manipulation de listes grâce à des fonctions récursives.

1. 🖥️ Écrire une fonction récursive ```somme_liste(L)``` qui calcule et renvoie la somme des éléments de la liste passé en paramètre

2. 🖥️ Écrire une fonction récursive ```concatenation(L1, L2)``` qui renvoie la concaténation de deux listes passées en paramètre. On mettra dans un premier temps les éléments de *L1* avant ceux de *L2*. *Pour rappel la concaténation de deux listes se fait grâce à l'opérateur « + » et consiste à créer une liste à partir des deux.

3. 🖥️ Sur les bases de la fonction ```concatenation(L1, L2)```, créer une nouvelle fonction ```concat_avec_tri(L1, L2)``` qui concatène deux listes ensembles **MAIS** qui crée une liste triée. Le fonctionnement est donné par le schéma suivant :



# TODO

### Exercice 1

Pour convertir un nombre entier positif *n* de la base décimale à la base binaire, il est possible d'opérer avec des divisions successives de *n* par 2. Les restes de ces divisions constituent la représentation binaire.

🖥️ Écrire une fonction récursive ```binaire(n)``` permettant de calculer la représentation binaire d'un nombre *n*. La fonction devra renvoyer une liste où chaqué élément est un bit (```int```) de la représentation binaire.


### Exercice 2

La suite doit son nom à Leonardo Fibonacci qui, dans un problème récréatif posé dans l'ouvrage *Liber abaci* publié en 1202, décrit la croissance d'une population de lapins : « Quelqu’un a déposé un couple de lapins dans un certain lieu, clos de toutes parts, pour savoir combien de couples seraient issus de cette paire en une année, car il est dans leur nature de générer un autre couple en un seul mois, et qu’ils enfantent dans le second mois après leur naissance. »

Le problème de Fibonacci est à l'origine de la suite dont le *n-ième* terme correspond au nombre de paires de lapins au *n-ième* mois. Dans cette population idéale, on suppose que :

- au début du premier mois, il n'y a qu'une paire de lapereaux ;
- les lapins ne peuvent procréer qu'à partir de l'âge de deux mois ;
- chaque début de mois, toute paire susceptible de procréer engendre exactement une nouvelle paire de lapereaux ;
- les lapins ne meurent jamais (la suite de Fibonacci est donc croissante).

Ainsi la suite de Fibonacci se définit comme suit :

- si *n=0* alors *F(n) = 0*
- si *n=1* alors *F(n) = 1*
- sinon *F(n) = F(n-1) + F(n-2)*

🖥️ Écrire une fonction récursive ```fibo(n)``` permettant de calculer l'élément *n* de la suite de Fibonacci.

📝 Décrire l'arbre d'appels de la fonction ```fibo(n)```


### Exercice 3

Un nombre *n* est pair si *(n-1)* est impair, et un nombre *n* est impair si *(n-1)* est pair.

🖥️ Écrire une fonction **deux fonctions récursives mutuelles** ```pair(n)``` et ```impair(n)``` permettant de savoir si un nombre *n* est pair ou impair.

📝 Décrire les échanges entre les deux fonctions lors des appels suivants :

- *n=0*
- *n=1*
- *n=2*


### Exercice 4

Un nombre premier est un entier naturel qui admet **exactement deux diviseurs distincts entiers et positifs** : 1 et le nombre considéré.

🖥️ Écrire une fonction récursive ```est_premier(n,i)``` renvoyant ```True``` si *n* est premier, ```False``` sinon. Il est à noter que la variable *i* permet de tester la divisibilité de *n*.


### Exercice 5

Le PGCD de *a* et *b* est le plus grand nombre qui est diviseur à la fois de *a* et de *b*.

🖥️ Écrire une fonction récursive ```pgcd(a,b)``` renvoyant le PGCD de deux entiers *a* et *b*.
