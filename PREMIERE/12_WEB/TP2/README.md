# TP2 - Création d'une page web (HTML et CSS)

## I - Contexte

## II - Création de l'environnement de travail

## III - Poser les bases

## IV - Un peu de mise en forme

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

À ce stade, vous devriez avoir une page comme ceci

![Vérfication 1](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/TP2/assets/verif_1.png)

La page commence à prendre mais l'affichage du header n'est pas incroyable, changeons ça.


## IV - Un peu de mise en forme

Dans cette partie, nous allons mettre en forme le header afin d'avoir un affichage plus propre.

1. Appliquer les styles suivants à la balise header :

    - appliquer à l'attribut ```display``` la valeur ```flex```. Ce style a pour effet de créer une *flexbox* (raccourci pour CSS Flexible Box Layout Module), un standard CSS3 de disposition des éléments dans une page web

    - après avoir écrit cette ligne, l'affichage est encore pire... nous allons alors appliqué à l'attribut ```flex-direction``` la valeur ```column```, à l'attribut ```justify-content``` la valeur ```center``` et à l'attribut ```align-items``` la valeur ```center```

    - maintenant l'affichage est bien mieux ! Stylisons encore notre page. Ajouter à l'espace de titre le style suivant :

```css
box-shadow : -13px 13px 2px 1px rgba(0, 0, 0, .2)
```

Maintenant, nous avons un super affichage pour notre page ! Mais notre menu de navigation laisse encore à désirer... Occupons-nous de ça.

1. Appliquer une flexbox à la liste non ordonnée et rajouter un attribut ```flex-direction``` ayant la valeur ```row```

2. Ajouter à chaque élément les styles suivants :

    - enlever les puces de liste avec l'attribut ```list-style-type``` à ```none```

    - appliquer un ```padding``` de 75px

    - passer la taille de la police à 20px

    - changer la police d'écriture pour mettre *Kenia, cursive* (la même police que l'espace de titre)

3. Ajouter une image derrière chaque élément du menu

    - Pizza > pizza-banner.jpg
    - Salade > salade-banner.jpg
    - Burger > burger-banner.jpg
    - Boisson > boisson-banner.jpg

4. Mettre en blanc la couleur du texte de chaque élément

À ce stade, l'affichage est pas mal mais non allons encore l'améliorer :

5. Rajouter les styles suivants pour chaque éléments du menu :

    - mettre l'attribut ```cursor``` avec la valeur ```pointer```

    - mettre l'attribut ```background-size``` avec la valeur ```cover```

    - mettre l'attribut ```background-repeat``` avec la valeur ```no-repeat```


À ce stade, vous devriez avoir une page comme ceci

![Vérfication 1](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/TP2/assets/verif_2.png)


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
