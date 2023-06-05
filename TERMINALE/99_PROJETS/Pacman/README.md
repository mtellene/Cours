# Pacman

![Pacman logo](https://github.com/mtellene/NSI/blob/main/TERMINALE/99_PROJETS/pacman/assets/pacman_logo.jpg)

## I - Le jeu
## II - Cahier des charges
### 1. Explications globales
### 2. Ne pas partir de 0

## III - Les différentes étapes du projet
### 1. Afficher le plateau
### 2. Gestion de Pacman
### 3. Gestion des fantômes
### 4. Quels algorithmes de déplacement ?

## IV - Pour aller plus loin

---

## I - Le jeu

Pac-Man (パックマン, Pakkuman) (initialement intitulé Puck-man) est un jeu vidéo créé par Tōru Iwatani pour l’entreprise japonaise Namco, sorti au Japon le 22 mai 1980. Le jeu consiste à déplacer Pac-Man, un personnage qui, vu de profil, ressemble à un diagramme circulaire à l’intérieur d’un labyrinthe, afin de lui faire manger toutes les pac-gommes qui s'y trouvent en évitant d’être touché par des fantômes.


## II - Cahier des charges
### 1. Explications globales

Dans notre version de Pacman, 3 classes seront utilisées :

- ```Labyrinthe```
- ```Pac_Man```
- ```Ghost```

Les classes sont données initialement vide, à vous de réfléchir aux différents attributs et aux différentes méthodes.

Dans un premier temps, nous n'utiliserons pas d'images; Ainsi vous pourrez représenter Pacman avec un rond et les fantômes avec des carrés (pour information, dans le jeu il y a un fantôme bleu, un rose, un rouge et un orange). 

### 2. Ne pas partir de 0

Vous trouverez dans ```ressources/``` un fichier python contenant le début du projet.

Si lorsque vous lancez le programme, vous avez une erreur qui vous indique que le module ```tkinter``` n'est pas installé, tapez dans le terminal la commande suivante :

```
sudo apt-get install python3-tk
```

## III - Les différentes étapes du projet
### 1. Afficher le plateau

Le labyrinthe est représenté, en machine, par une matrice de *31* cases de hauteur et *28* de largeur. Les cases de la matrice sont les suivantes :

- *0* pour une case de vide
- *1* pour un mur
- *2* pour une pac-gomme
- *3* pour une super pac-gomme (elles sont censées déclencher le mode panique des fantômes lorsque pacman les mangent)

la première étape est donc d'afficher ce plateau dans la fenêtre ```tkinter```. Le résultat devrait être le suivant :

![Pacman logo](https://github.com/mtellene/NSI/blob/main/TERMINALE/99_PROJETS/pacman/assets/plateau.png)


### 2. Gestion de Pacman

Compléter la classe ```Pac_man``` et le reste du code pour pouvoir afficher et déplacer le pacman dans le labyrinthe. Vous pourrez, dans un premier temps, représenter pacman avec un rond jaune.

```Tkinter``` utilise le paradigme de programmation événementielle : le programme attend qu'un événement se produise (ici un appui sur une touche du clavier). Une fois cet événement se produit, le gestionnaire d'évènement, qui est une fonction qui a été précédemment "liée" à cet évènement.

Le code contient déjà le "lien" entre l'évènement "appui sur n'importe quelle touche du clavier" et une méthode de déplacement de la classe ```Pac_man``` : la méthode ```move```

Dans le "vrai" jeu, pacman avance automatiquement dans une direction tant qu'il ne rencontre pas un mur : il n'y a donc pas besoin d'appuyer constamment sur une touche pour le déplacer, mais uniquement pour le faire changer de direction.

Afin de simplifier les choses, nous allons dans un premier temps, implémenter un déplacement qui nécessite de toujours appuyer sur une touche pour faire avancer pacman, qui sera donc au repos en l'absence de touche enfoncée.

En plus du mouvement, il faudra le fait que pacman mange les pac-gommes. Une fois que notre personnage sera passé sur l'une d'entre elles, celle-ci devra être enlevée du plateau.

### 3. Gestion des fantômes

Le gros du projet !

C'est là que vous allez mettre à profit vos connaissances sur les graphes et les parcours de graphes...

Dans le jeu original, il y a 4 fantômes qui ont chacun une couleur différente et une stratégie de déplacement qui leur est propre.

- Blinky, le fantôme rouge, traque pacman en le suivant partout à travers le labyrinthe
- Pinky, le fantôme rose, cherchera toujours à se placer devant lui pour lui tendre une embuscade
- Inky, le fantôme bleu, a la même stratégie que Pinky.
- Clyde, le fantôme orange, a un déplacement purement aléatoire

Chacun de ces fantômes correspondra à une instance de la classe ```Ghost```. Pour les représenter, on pourra se contenter dans un premier temps d'un simple carré coloré.

Les fantômes se trouvent initialement dans un espace appelé "la prison", espace se situant au centre du labyrinthe. Ils se déplacent dans les couloirs mais ne mangent pas les pac-gommes.

Les fantômes doivent se déplacer seuls dans le labyrinthe. Dans un premier temps, vous pourrez faire en sorte que si pacman se déplace, les fantômes se déplacent.

Afin de vous aider dans cette tâche, vous pouvez voir le labyrinthe comme un graphe. Les sommets de ce graphe seront les cases du labyrinthe et il existera une arête entre deux sommets si et seulement les cases sont voisines (attention au tunnel).

Cette structure de données sera particulièrement utile pour connaître les déplacements possibles des fantôme (ce seront les sommets voisins de la position actuelle du fantôme). De plus, cette structure de données sera créée une fois pour toute au début du jeu et non modifiée par la suite.


### 4. Quels algorithmes de déplacement ?

Vous avez le choix entre plusieurs méthode :


- déplacements aléatoire (:fire:). À chaque pas d’exécution, on choisit un sens de déplacement au hasard du fantôme. **Attention** le fantôme peut faire du sur-place et non un "vrai déplacement"

- déplacements en ligne droite avec changement de direction à la rencontre d'un obstacle/d'une bifurcation (:fire: :fire:). Le fantôme se déplace dans les couloirs tant qu'il ne rencontre pas un mur et/ou une bifurcation; à ce moment, il change aléatoirement de direction. **Attention** le fantôme peut faire des aller-retours dans un même couloir

- déplacement avec minimisation de la distance (:fire: :fire:). L'idée est de calculer à itération la distance "à vol d'oiseau" (sans tenir compte des obstacles) entre le fantôme et pacman, et rechercher la direction dans laquelle aller pour minimiser cette distance. On peut utiliser le calcul de la *distance de Manhattan*, qui correspond bien à un déplacement dans une grille avec 4 directions possibles

- déplacement avec "traque" (:fire: :fire: :fire:). L'idée est d'utiliser un algorithme pour déterminer le plus court chemin qui existe entre pacman et le fantôme, et le faire suivre à ce dernier. Vous avez plusieurs choix :

    - Parcours en profondeur un peu modifié (:fire: :fire:)
    - Algorithme de Dijsktra (:fire: :fire:)
    - Algorithme A* (:fire: :fire: :fire:)


## IV - Pour aller plus loin

Voici une liste non exhaustive d'améliorations possibles :

- rajouter plusieurs vies au joueur

- mettre les "vraies images" pour nos personnages, vous trouverez les images dans ```ressources/imgs```

- rajouter une gestion du score avec :
    - un fichier texte (:fire:)
    - un fichier excel (:fire: :fire:), il sera possible de rajouter un nom de joueur
    - une base de données (:fire: :fire: :fire:), il sera possible de rajouer un nom de joueur

- implémenter le mode panique des fantômes quand une grosse pac-gomme est mangée

- implémenter un déplacement continu et non un système de "tour par tour"

- dans le "vrai" jeu, des cerises et des pastèques apparaîssent de manière aléatoire à votre point de départ, implémenter cette fonctionnalité

- une fois que toutes les pac-gommes ont été mangées, faire changer de niveaux l'utilisateur. Qu'est-ce qui change ? La couleur du niveau, la vitesse des fantômes et leurs "intelligences"