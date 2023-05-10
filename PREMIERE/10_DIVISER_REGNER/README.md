## Dossier pour la méthode de programmation diviser pour régner



## Pour aller plus loin - Créer un environnement de test pour nos fonctions

Vérifier à la main que nos fonctions sont correctes est impossible, il faudrait tester tous les cas possibles et cela serait bien trop long.

D'une manière générale, il n'est pas possinle de vérifier à l'aide de tests que nos fonctions sont correctes. Les tests nous permettent d'avoir un certain degré de confiance dans nos fonctions.

Dans cette partie, nous allons essayer d'augmenter le degré de confiance en nos fonctions.


### Cas de la recherche dichotomique


1. Ouvrez le fichier ```rech_tableau_trie.py```

2. Supprimer les fonction ```test_not_in_liste(f,L)``` et ```test_in_liste(f,L)```

3. Une première façon de tester notre fonction serait de faire la chose suivante :

```python
print(recherche_dicho([1,2,3],1))
print(recherche_dicho([1,2,3],2))
print(recherche_dicho([1,2,3],3))
print(recherche_dicho([1,2,3],0))
```

Ici, on voit bien que l'affichage attendu est

```python
True
True
True
False
```

4. Recopier les 4 lignes de tests sous votre fonction ```recherche_dicho(L, N)``` et vérifier que le résultat obtenu est le même que celui qui est attendu

5. Bien que cette méthode soit utile pour vérifier nos résultats, celle-ci n'est pas très efficace. En effet, imaginez que l'on fasse une centaine de tests comme ceci et que l'on doit vérifier que l'on ait le bon résultat en regardant l'affichage ligne par ligne. Il nous faut donc un moyen automatique permettant de nous informer quand le résultat **n'est pas celui attendu**. De cette manière, il sera bien plus simple d'identifier les cas posants des problèmes.

Pour ce faire, nous allons utiliser **une assertion**. Une assertion est une expression qui doit être évaluée comme vraie. Si cette évaluation échoue elle peut mettre fin à l'exécution du programme, ou bien lancer une exception.

En Python, une assertion se note de la manière suivante :

```python
"assert" expression1 ["," expression2]
```

Ce qu'il faut comprendre ici est que ```expression1``` correspond à la condition que nous testons, et l’optionnel ```expression2``` est un message d’erreur qui ne s’affichera que si l’assertion échoue.

Par exemple si l'on veut tester qu'une variable ```x``` est égale à 2 grâce à une assertion, on pourra écrire :

```python
assert x == 2, "La variable x n'est pas égale à 2"
```

6. Modifier le programme et remplacer les ```print()``` effectués à l'étape 4 par des assertions. Normalement, aucune ```AssertionError``` ne devrait être relevée lorsque vous lancez le code

7. Maintenant, nous allons provoquer une erreur. Recopier la ligne suivante :

```python
assert recherche_dicho([1,2,3],0) == True, "Erreur attendue"
```

Ici, nous provoquons une erreur intentionnelle car nous ne mettons pas le bon résultat. Lancer le code, vous devriez avoir une erreur comme ceci :

```python
Traceback (most recent call last):
  File "...", line ..., in <module>
    assert recherche_dicho([1,2,3],0) == True, "Erreur attendue"
AssertionError: Erreur attendue
```

Nous pouvons remarquer 2 choses. La première est que l'on nous indique que l'erreur relevée est une assertion (```AssertionError```), un de nos tests n'a donc pas produit le résultat attendu **et** nous savons lequel. La seconde chose est que le message que nous avons écrit est affiché après le type de l'erreur. Grâce à ce message, il est possible de donner des informations sur le résultat attendu ou bien sur la nature du test réalisé.

Vous pouvez maintenant enlevé la ligne posant problème.


##### Recherche dichotomique - TODO

1. Créer une fonction ```generation(n)``` qui prend en argument un nombre ```n``` et qui renvoie une liste triée par ordre croissant contenant *n* éléments **et** une liste non triée par ordre croissant contenant aussi *n* éléments. Afin de vous aider, vous pouvez utiliser la fonction ```shuffle()``` du module ```random```.

2. Créer une fonction ```test_recherche_dicho()``` qui ne prend par d'argument. Cette fonction devra :
    
    - faire une boucle allant de 10 en 10 de 10 à 101
    - dans la boucle, appeler la fonction ```generation(n)``` avec en argument la variable de la boucle (bien évidemment, il faudra récupérer les listes renvoyées par la fonction)
    - il faudra ensuite passer à la phase de tests en utilisant des assertions, pour ce faire il faudra réaliser les tests suivants :
        - 1 test où la valeur cherchée est la valeur du milieu
        - 1 test où la valeur cherchée est la première valeur
        - 1 test où la valeur cherchée est la dernière valeur
        - 3 tests où la valeur cherchée se trouve à des indices aléatoires (cf la fonction ```randint``` du module ```random```)
        - 3 tests où la valeur cherchée **n'est pas dans la liste** (à vous de trouver comment faire)

Bien sûr ces tests seront à faire sur chacune des listes générées.

Pour vous aider dans vos assertions, vous pourrez comparer les résultats de ```recherche_dicho(L,N)``` aux résultats de l'instruction ```N in L``` qui renvoie ```True``` lorsque ```N``` est dans ```L```, ```False``` sinon.

Votre but, en plus d'écrire les tests, faire en sorte qu'ils passent tous, il faudra peut-être modifier la fonction ```recherche_dicho(L,N)```.