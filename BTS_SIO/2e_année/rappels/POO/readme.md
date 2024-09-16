# MonopN-SI

## I - Mise en place
## II - Le projet
## III - Explication des classes
## IV - Déplacement
## V - Exemple d'exécution du programme
## VI - Notation
### 1/ ```Partie.py```
### 2/ ```Joueur.py```
### 3/ ```Terrain.py```
### 4/ ```Plateau.py```
### 5/ Autre

## VII - Bonus

---

## I - Mise en place

Vous n’allez pas partir de rien pour ce projet, la base du projet se trouve dans le dossier ```code/```. Les fichiers de ce dossier sont incomplets et le but de ce projet est de rendre tout ceci fonctionnel.


## II - Le projet

Dans ce projet, vous serez amenés à créer le jeu du MonopN’SI (jeu fortement inspiré par le Monopoly) en Python.

Le Monopoly (litt. « monopole » en anglais) est un jeu de société américain. Le but du jeu consiste à ruiner ses adversaires par des opérations immobilières (selon Wikipédia : https://fr.wikipedia.org/wiki/Monopoly).

Les règles de ce jeu étant multiples et complexes, nous allons simplifier quelques points afin de rendre la réalisation plus simple (certains points pourront être ajoutés en tant que bonus) :

— l’hypothèque est supprimée

— nous utiliserons un seul dé

— un joueur a un solde, mais pas de liste de billets ; par exemple si un joueur a un solde de 10, on ne se demande pas si c’est un billet de 10, deux de 5, dix de 1, ...

— les gares, les cases « chance », caisse de communauté, impôts et compagnie d’eau et d’électricité, ne seront pas traitées

— les cases « Départ », « Prison », « Parc gratuit » et « Aller en prison », seront des cases sans traitement (rien ne se passe)

— un joueur passant par la case « Départ » reçoit 200

— une maison augmente le loyer du terrain de 1.2, un hôtel de 1.4


## III - Explication des classes

```Plateau.py``` : un plateau est défini par une liste de terrains.

Méthode de ```Plateau``` :

— ```avoir_terrain_i_j``` : donne le terrain qui se trouve aux coordonnées *(i, j)*

```Case_speciale.py``` : les équivalents des cases spéciales dans le « vrai » jeu sont les gares, les cases chance, ... . Une case spéciale est définie
par un nom.

```Joueur.py``` : un joueur est défini par un nom, un compte, une liste de propriétés et une position. Tous les joueurs démarrent avec 1500, aucune propriété et une position égale à *(0, 0)*.

Méthodes de ```Joueur``` :

— ```tirer_de``` : le joueur tire le dé

— ```deplacement``` : le joueur se déplace sur le plateau

— ```acheter``` : le joueur achète un terrain

— ```payer``` : le joueur est sur une propriété appartenant à quelqu’un, il paye alors le loyer

```Terrain.py``` : un terrain est défini par un nom, une couleur, un nombre de maisons, un nombre d’hôtels, un propriétaire, un coût d’achat, un loyer, un coût pour mettre une maison et un coût pour mettre un hôtel. Ces 4 derniers attributs sont déterminés en fonction
de couleur du terrain (voir plus bas)

Méthodes de ```Terrain``` :

— ```est_achetable``` : indique si le terrain est achetable (si le terrain a un propriétaire ou non)

— ```ameliorer_terrain``` : améliore un terrain, rajoute d’abord une maison (si le joueur le peut et le veut) ; s’il y a 4 maisons sur le terrain, rajoute un hôtel (si le joueur le peut et le veut) ; s’il y a un hôtel, le terrain ne peut plus être augmenté

| couleur du terrain | marron | bleu | rose | orange | rouge | jaune | vert | violet |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| coût d'achat | 60 | 100 | 140 | 180 | 220 | 260 | 300 | 350 |
| loyer | 40 | 80 | 120 | 160 | 200 | 240 | 280 | 330 |
| coût construction d'une maison | 100 | 100 | 150 | 150 | 200 | 200 | 300 | 350 |
| coût construction d'un hôtel | 500 | 500 | 700 | 700 | 900 | 900 | 950 | 1000 |


```Partie.py``` : une partie est définie par une liste de joueurs et un plateau.

Méthodes de ```Partie``` :

— ```avoir_joueur_avec_nom``` : indique le joueur ayant le nom passé en paramètre

— ```choix_action``` : le joueur choisit une action à faire

— ```deplacement``` : le joueur tire le dé et se déplace du nombre de cases correspondant, le système de déplacement est décrit plus bas

— ```traitement_post_deplacement``` :
    
    — si la case actuelle est un terrain et qu’il est achetable et que le joueur peut l’acheter, alors on propose le terrain à l’achat

    — sinon si la case actuelle est un terrain et qu’il est achetable et que le joueur ne peut pas l’acheter, alors on indique au joueur qu’il ne peut pas l’acheter

    — sinon si la case actuelle est un terrain et qu’il appartient au joueur qui est tombé dessus alors le terrain peut être amélioré

    — sinon si la case actuelle est un terrain et qu’il appartient à un autre joueur que celui qui est tombé dessus alors le joueur paye le propriétaire

    — sinon si la case actuelle n’est pas un terrain (c’est une case que l’on appelle « spéciale »), alors on indique au joueur que cette case n’est pas achetable

— ```tour``` : le joueur choisit l’action à faire, se déplace et fait l’action post déplacement

— ```joueur_faillite``` : indique si un joueur un en faillite (attention un joueur ayant un compte à 0 n’est pas en faillite)

— ```definir_gagnant``` : indique le joueur ayant le plus haut compte en banque


## IV - Déplacement

Le plateau peut être représenté de la manière suivante :

![graphe TP](https://github.com/mtellene/Cours/blob/main/BTS_SIO/2e_ann%C3%A9e/rappels/POO/asset/plateau.png)

Si le joueur se trouve sur la case « Boulevard de Belleville », alors les coordonnées du joueur sont *(0,1)*. De la même manière s’il se trouve sur la case « Prison »(case qui fait l’angle gauche
inférieur), les coordonnées du joueur sont *(1,0)*.

Si le système de coordonnées n’est pas clair, le constructeur du plateau devrait vous aider à mieux comprendre. Ainsi, pour le déplacement, si le joueur se trouve aux coordonnées *(1,3)* (cf.
« Boulevard de Paradis ») et qu’il doit se déplacer de 6 cases (il a obtenu 6 avec le dé), il arrivera aux coordonnées *(2,2)*.


## V - Exemple d'exécution du programme

Ceci est un exemple, vous pouvez faire l’affichage que vous souhaitez, il faut que le joueur comprenne ce qu’il peut et ce qu’il doit faire.

```python
Tour de Victor

# # # # début choix_action # # # #
Que voulez-vous faire ?
1 - Tirer le dé
2 - Consulter mon compte
3 - Voir sur quelle case je suis
Mon choix : 2
Victor a sur son compte 1500

Que voulez-vous faire ?
1 - Tirer le dé
2 - Consulter mon compte
3 - Voir sur quelle case je suis
Mon choix : 3
Victor est sur la case : Départ

Que voulez-vous faire ?
1 - Tirer le dé
2 - Consulter mon compte
3 - Voir sur quelle case je suis
Mon choix : 1
# # # # fin choix_action # # # #

# # # # début deplacement # # # #
Victor tire le dé
Victor a fait 6
Victor se déplace de 6 case(s)
Victor est arrivé sur la case Avenue de la République
# # # # fin deplacement # # # #

# # # # début traitement_post_deplacement # # # #
Avenue de la République n a pas de propriétaire
Avenue de la République coûte 100 et Victor a 1500
Voulez-vous l acheter (1/0) ? 1
Victor a acheté Avenue de la République
# # # # fin traitement_post_deplacement # # # #
```


## VI - Notation

### 1/ ```Partie.py```

| Tâche | Barème |
| :-: | :-: |
| ```__init__``` | 1 |
| ```avoir_joueur_avec_nom``` | 1 |
| ```deplacement``` | 1 |
| ```traitement_post_deplacement``` | 2 |
| ```joueur_faillite``` | 0.5 |
| ```definir_gagnant``` | 0.5 |


### 2/ ```Joueur.py```


| Tâche | Barème |
| :-: | :-: |
| ```__init__``` | 1 |
| ```tirer_de``` | 0.5 |
| ```deplacement``` | 1 |
| ```acheter``` | 1 |
| ```payer``` | 1 |

### 3/ ```Terrain.py```

| Tâche | Barème |
| :-: | :-: |
| ```__init__``` | 1 |
| ```est_achetable``` | 0.5 |
| ```ameliorer_terrain``` | 2 |

### 4/ ```Plateau.py```

| Tâche | Barème |
| :-: | :-: |
| ```avoir_terrain_i_j``` | 0.5 |

### 5/ Autre

| Tâche | Barème |
| :-: | :-: |
| Affichage clair | 1 |
| Code propre | 1 |
| Code optimisé | 1 |
| Commentaire | 1 |
| Le jeu s’arrête quand un joueur est en faillite | 0.5 |


## VII - Bonus

Si tous les points précédents ont été faits, vous pouvez ajouter des éléments à votre jeu. Voici une liste non exhaustive d’éléments à rajouter :

— jouer avec 2 dés et rajouter la règle du double, ainsi que celle du troisième double consécutif 🎲🎲 

— la case « Aller en prison » déplace un joueur en prison et ne peux plus jouer de trois tours

— rajouter le système de l’hypothèque 🏠

— rajouter des cases chances 🍀

— rajouter des gares 🚄

— rajouter une interface graphique
