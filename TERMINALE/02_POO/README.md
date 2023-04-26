## Dossier pour la programmation orientée objet

## Explications sur la Programmation Orientée Objet (POO)

L'exemple décrit dans la suite donne des explications sur la POO

## Vocabulaire

- **Classe** : plan pour créer des objets. Une classe définit les données (**attributs**) et les fonctionnalités (**méthodes**) des objets. On peut accèder aux attributs et méthodes d'un objet avec un point (```.```).

Exemple :
```python
class Chien:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
    
    # une méthode
    def aboyer(self):
        print("Waf") 
```

- **Objet** : élément issu d'une classe possédant les fonctionnalités définit dans la classe auquel il appartient. Un objet correspond souvent à un quelque chose de réel (une voiture, un chien,...).

- **Instanciation** : processus de création d'un objet d'une classe. Cette création d'objet se fait grâce à la méthode ```__init__``` de la classe

Exemple :
```python
# création d'un objet de la classe Chien
medor = Chien("Médor")

# accès à un attribut
print(medor.nom)
>>> "Médor"

# accès à une méthode
medor.aboyer()
>>> "Waf"
```

- Méthode : un sous-ensemble des fonctionnalités globales d'un objet. Une méthode est définit de la même manière qu'une fonction (mot-clé ```def```) dans la définition de la classe.

- Self : Le premier argument lorsque l'on définit n'importe quelle méthode est **toujours** l'argument ```self```. Cet argument spécifie l'instance sur laquelle on applique une méthode. ```self``` donne à l'interpréteur Python les informations sur l'instance à utiliser. Pour *définir* une méthode il faut utiliser ```self``` pour modifier les attributs de l'instance. Mais lors de *l'appel* d'une méthode, on ne doit pas écrire ```self```.

## Un exemple de création et d'utilisation de classe

Dans cette partie, nous allons créer et utiliser une classe ```Zoo```.

Tout d'abord, définissons notre zoo. Nous allons le définir comme suit : un zoo possède un nom, un nombre d'enclos et des animaux (on simplifie). Ainsi lors de la définition de notre classe ```Zoo``` nous allons devoir spécifier ces 3 éléments (**attributs**).

```python
class Zoo:

    # constructeur
    def __init__(self, nom, nb_enclos, liste_animaux):
        self.nom = nom
        self.nb_enclos = nb_enclos
        self.liste_animaux = liste_animaux
```

Il est possible d'améliorer notre constructeur. En effet, nous pouvons indiquer que lorsqu'un zoo se crée, il ne possède pas d'enclos et pas d'animaux. Ainsi nous pouvons modifier notre constructeur de cette manière.

```python
class Zoo:

    # constructeur
    def __init__(self, nom, nb_enclos, compte_animaux):
        self.nom = nom
        self.nb_enclos = 0
        self.liste_animaux = []
```

Suite à ce changement, nous pouvons remarquer que 2 arguments de ```__init__()``` ne sont plus utilisés : ```nb_enclos``` et ```liste_animaux```. Afin de simplifier la création d'objet de la classe ```Zoo``` et pour optimiser le code, nous allons encore modifier le constructeur de notre classe.

```python
class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.liste_animaux = []
```

Et voilà, notre constructeur et achevé (pour l'instant), nous pouvons créer des objets de la classe ```Zoo```.

Pour créer un objet issu d'une classe, il faut procéder comme suit :

```python
objet = Nom_de_la_classe(elements_pour_créer_l_objet)
```

Dans notre cas, le nom de la classe est ```Zoo``` et pouvoir être créer, un zoo a besoin d'un nom. Pour le savoir, il suffit de regarder les arguments (sans prendre en compte le ```self```) de la méthode ```__init__()``` de la classe. Ainsi pour créer un zoo, il faut écrire :

```python
mon_zoo = Zoo("ZPoo")
```

Nous avons créé un objet de la classe ```Zoo```, nous pouvons donc accèder à ses attributs afin de vérifier que l'objet a été créé tel que nous le voulions.

```python
print(mon_zoo.nom)
>>> "ZPoo"

print(mon_zoo.nb_enclos)
>>> 0

print(mon_zoo.compte_animaux)
>>> {}
```

Notre zoo a bien été créé. Mais bien qu'il est été créé, un zoo sans animaux ne sert pas à grand chose... Rajoutons donc des animaux.

Avant de les rajouter, il faut qu'ils puissent être mis quelque part, autrement dit, il faut qu'il y est des enclos. Nous allons donc créer une méthode qui va ajouter un enclos dans un zoo. Pour ce faire nous devons simplement augmenter la valeur de l'attribut ```nb_enclos```.

Pour cette "version" de la méthode, nous allons augmenter de *1* le nombre d'enclos.

```python
class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.compte_animaux = {}

    # méthode ajouter_enclos
    def ajouter_enclos(self):
        self.nb_enclos = self.nb_enclos + 1
```

Il est à noter que la méthode n'a pas besoin de renvoyer l'attribut ```nb_enclos``` pour que le changement soit fait, c'est l'avantage de la programmation orientée objet. Il suffit simplement d'appliquer la méthode ```ajouter_enclos()``` à un objet de la classe ```Zoo``` pour que l'attribut ```nb_enclos``` de l'objet soit augmenter. Ainsi pour ajouter un enclos, nous ferons :

```python
mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
```

Pour vérifier que l'ajout a été fait, nous pouvons mettre à la suite l'instruction ```print(mon_zoo.nb_enclos)``` et voir que le nombre d'enclos a été augmenté de 1.

Maintenant que nous avons un enclos, nous pouvons ajouter un animal. Pour commencer, nous allons ajouter 3 lions. Ainsi nous allons créer une méthode ```ajouter_animaux()``` qui prendra en argument un nom d'animal et combien d'animaux nous voulons ajouter.

```python
class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.liste_animaux = []

    # méthode ajouter_enclos
    def ajouter_enclos(self):
        self.nb_enclos = self.nb_enclos + 1

    # méthode ajouter_animaux
    def ajouter_animaux(self, nom_animal, nombre_animal):
        if self.nb_enclos > 0:
            self.liste_animaux.append((nom_animal, nombre_animal))
```

Ensuite, pour ajouter nos 3 lions, il suffira de faire :

```python
mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
mon_zoo.ajouter_animaux("lion", 3)
```

Afin de vérifier l'ajout, nous pouvons ajouter 

```python
mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
mon_zoo.ajouter_animaux("lion", 3)
print(mon_zoo.liste_animaux)
>>> [('lion', 3)]
```

*A noter : notre ajout n'est pas le meilleur, en effet, si l'on veut être très rigoureux, il faudra créer une classe Lion et ajouter à notre zoo des objets de la classe Lion. Ici, nous simplifions le fonctionnement et l'utilisation, le but n'est pas pour l'instant de faire le meilleur code possible mais plutôt de comprendre comment la POO fonctionne.*

Notre zoo compte à présent 3 lions. Bien que cela fonctionne, notre mode de fonctionnement présente des défauts :

- avec la définition de notre méthode ```ajouter_animaux()```, il est possible de mettre tous les animaux du zoo dans le même enclos

- notre structure de données pour stocker différents animaux du zoo n'est pas la meilleure

Pour parer à ces 2 problèmes nous pourrions :

- créer un attribut ```enclos_libres``` dans le constructeur de ```Zoo``` et : 
    - si on ajoute un animal qui n'est pas déjà dans le zoo, on l'ajoute si et seulement si au moins un enclos est libre

    - si on ajoute un animal déjà présent dans le zoo, alors on ajoute sans prendre en compte l'attribut ```enclos_libres```

- afin de tenir le compte de nos animaux, il sera plus judicieux d'utiliser un tableau associatif (dictionnaire en Python) où la clé serait le nom de l'animal et la valeur combien de cet animal il y a dans notre zoo. Par la même occasion, nous allons modifier le nom de l'attribut pour qu'il "colle plus" avec la structure de données.

Ainsi, notre classe ```Zoo``` deviendrait :

```python
class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.animaux = {}
        self.enclos_libres = 0

    # méthode ajouter_enclos
    def ajouter_enclos(self):
        self.nb_enclos = self.nb_enclos + 1
        self.enclos_libres = self.enclos_libres + 1

    # méthode ajouter_animaux
    def ajouter_animaux(self, nom_animal, nombre_animal):
        if nom_animal not in self.animaux.keys():
            if self.enclos_libres > 0:
                self.animaux[nom_animal] = nombre_animal
                self.enclos_libres = self.enclos_libres - 1
            else:
                print(f"L'ajout de {nombre_animal} {nom_animal} est impossible : plus d'enclos libres")
        else:
            self.animaux[nom_animal] = self.animaux[nom_animal] + nombre_animal
```

Nous pouvons tester notre classe avec le code suivant :

```python
mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
mon_zoo.ajouter_animaux("lion", 3)
print(mon_zoo.animaux)
>>> {'lion': 3}

mon_zoo.ajouter_animaux("gazelle", 2)
>>> "L'ajout de 2 gazelle est impossible : plus d'enclos libres"

print(mon_zoo.animaux)
>>> {'lion': 3}

mon_zoo.ajouter_animaux("lion", 1)
print(mon_zoo.animaux)
>>> {'lion': 4}
```

Nous pouvons remarquer qu'il n'est pas possible d'ajouter des gazelles car aucun enclos n'est pas libre et les ajouter dans le zoo reviendrait à les mettre dans l'enclos de lions. De plus, si l'on ajoute un animal déjà présent dans le zoo, alors on le met dans l'enclos avec les animaux de son espèce.

Nous pourrions améliorer notre méthode ```ajouter_animaux()``` en faisant en sorte que s'il n'y a plus d'emplacement vide, alors on en rajoute un en appelant la méthode ```ajouter_enclos()```.

```python
class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.animaux = {}
        self.enclos_libres = 0

    # méthode ajouter_enclos
    def ajouter_enclos(self):
        self.nb_enclos = self.nb_enclos + 1
        self.enclos_libres = self.enclos_libres + 1

    # méthode ajouter_animaux
    def ajouter_animaux(self, nom_animal, nombre_animal):
        if nom_animal not in self.animaux.keys():
            if self.enclos_libres == 0:
                self.ajouter_enclos()
            self.animaux[nom_animal] = nombre_animal
            self.enclos_libres = self.enclos_libres - 1
        else:
            self.animaux[nom_animal] = self.animaux[nom_animal] + nombre_animal
```

Nous pouvons tester notre classe en utilisant le code du test précédent :

```python
mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
mon_zoo.ajouter_animaux("lion", 3)
print(mon_zoo.animaux)
>>> {'lion': 3}

mon_zoo.ajouter_animaux("gazelle", 2)
print(mon_zoo.animaux)
>>> {'lion': 3, 'gazelle': 2}

mon_zoo.ajouter_animaux("lion", 1)
print(mon_zoo.animaux)
>>> {'lion': 4, 'gazelle': 2}
```
*A noter : ```mon_zoo.ajouter_enclos()``` n'est pas nécessaire et peut être enlevée car un enclos est ajouté (si besoin) lors de l'ajout d'un animal*


## Améliorer la classe ```Zoo``` par vous-même

Le code de la classe ```Zoo``` est disponible dans **Zoo.py**. Les améliorations sont données titre d'exemple.

Afin d'améliorer cette classe, vous pouvez :

- créer des classes d'animaux (```Lion``` ou ```Gazelle``` par exemple) et ajouter des objets des classes d'animaux (à vous de définir ces classes comme vous le souhaitez)

- créer une classe ```Enclos```. Un enclos aurait un type d'animal précis, un nombre d'animaux, savoir s'il est libre ou non et même un employé...

- créer une classe ```Employe``` avec des attributs et des méthodes (à vous de voir)

- ajouter des méthodes à la classe ```Zoo``` qui permettrait de : 
    - mettre un employé en poste sur un enclos
    - changer des animaux d'enclos
    - mettre en place un tarif pour entrer dans le zoo en fonction du nombre d'animaux que l'on a ou du nombre d'enclos

