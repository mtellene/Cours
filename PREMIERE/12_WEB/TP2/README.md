# TP2 - Création d'une page web (HTML et CSS)

## I - Contexte

## II - Création de l'environnement de travail

## III - Poser les bases

---

**NS'EAT** est un restaurant basé à Avignon.

Il propose des petits plats à emporter.

Vous allez coder la page web du restaurant. Sur cette page, il sera possible de voir les differentes formules et boissons.


## II - Création de l'environnement de travail

Avant de commencer le TP, vous allez créer votre environnement de travail. Pour ce faire vous allez dans votre dossier personnel, puis dans le dossier "web". Une fois arrivé, créer un dossier "TP2". C'est dans ce dossier que vous sauvegarderez les exercices de ce TP.

Les ressources nécessaires sont dans le dossier ```ressources/```

Vous n’avez pas le droit d’utiliser de framework.


## III - Poser les bases

1. Commencer pour créer un fichier "index.html" et créer la structure de base d'une page web (```<!DOCTYPE html>```, ```<html>```, ```<head>```, ```<body>```). Vous pouvez aller chercher un template de page web vierge [ici](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/ressources/structure_base.html)

2. Dans le body, créer un header. Pour ce faire utiliser la balise ```<header>...</header>```

3. Dans le header, nous allons commencer pour créer l'espace de titre :

    1. Créer une division avec la balise ```<div>...</div>```
    2. Dans cette division, ajouter le titre **NS'EAT** sous la forme d’une balise h1
    3. Ajouter le slogan *Des petits plats pour les grands programmeurs* en italique

4. Une fois l'espace de titre réalisé, ajouter un menu de navigation contenant 4 éléments Pizza, Salade, Burger, Boisson. Pour créer ce menu, il va falloir utiliser la balise ```<nav>...</nav>``` et dans cette balise, créer une liste non ordonnée. **Attention le menu est dans le header mais pas dans la division créée précédemment**.

5. Créer un fichier **styles.css** dans un dossier

6. Mettre le fond de la page en bleu (code couleur #1695DA)

7. Appliquer les styles suivants à l'espace de titre :

    - centrer le texte de la division
    - mettre un fond blanc
    - appliquer un ```padding``` de 50px
    - changer la police d'écriture en *Kenia, cursive*. Pour ce faire rajouter la ligne suivante dans la partie ```<head>```

```html
<link rel="stylesheet href="https://fonts.googleapis.com/css2?family=Kenia&display=swap">
```
    
Pour réaliser cette étape, il va falloir : 

1. créer un ```id``` pour la division de l'espace titre
2. récupérer cet ```id``` dans **styles.css** en utilisant un #
3. appliquer les filtres demandés



## Niveau 2. Menu

- Utiliser les flexbox pour ajuster les boutons sous la forme d’une ligne

- Ajouter une image derrière chaque bouton
    
    - Pizza > pizza-banner.jpg
    - Salade > salade-banner.jpg
    - Burger > burger-banner.jpg
    - Boisson > boisson-banner.jpg

- Mettre en blanc la couleur du texte de chaque bouton

**L'aperçu attendu est donné par la capture d'écran *apercu_menu.jpg***

- Faire une animation de scroll vers la bonne section lors d’un clique (sans ```javascript```)

## Niveau 3. Sections

- Créer une section *pizza*, contenant l’arrière plan *pizza-banner.jpg*

- Créer un premier produit contenant :
    - Le titre *Caprapiquante*
    - Une description *Chevre, Miel, Graines toastés, piment rouge*
    - Un prix *12€00*
    - L’image *pizza1.jpg*

- Créer un second produit contenant :
    - Le titre *Strategia*
    - Une description *Tomates, Mozarella, Basilique*
    - Un prix *9€00*
    - L’image *pizza2.jpg*

- Créer un troisieme produit contenant :
    - Le titre *Naturale*
    - Une description *Chèvre, courgettes, basilique, carottes, huile végetale*
    - Un prix *10€00*
    - L’image *pizza3.jpg*

- Mettre en forme chaque produit pour avoir le résultat suivant :

**L'aperçu attendu est donné par la capture d'écran *apercçu_section.jpg***


- Reproduire la même chose pour les sections salade, burger et boissons

## Niveau 4. Bonus

- Ajouter un pied de page contenant
    - La mention Copyright sous la forme d’un paragraphe
    - Une iframe affichant la position sur google maps de la structure https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d22981.61919597009!2d4.7977169268332664!3d43.94483236286202!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1srestaurant%20avignon!5e0!3m2!1sfr!2sfr!4v1678530888013!5m2!1sfr!2sfr (pas de correction)
