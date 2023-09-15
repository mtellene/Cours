# TP1 - Introduction au HTML

## I - HTML

## II - L'éditeur de code

## III - Quelques manipulations
### 1. Mise en place de la structure
### 2. Ajouter de l'information

## IV - À faire

## V - Pour aller plus loin

---

## I - HTML

Le HTML ou **HyperText Markup Language** est le langage de **balisage** cpnçu pour représenter les pages web. Ce langage a été conçu par **Tim Berners Lee** en **1993**.

Le HTML est une des trois inventions à la base du **World Wide Web (ou WWW)**. Les deux autres sont le **HyperText Transfer Protocol (HTTP)** et les **adresses web (URL)**. Le HTML a été inventé pour permettre d'écrire des documents hypertextuels liant les différentes ressources d'**Internet** avec des hyperliens. Pour reconnaître les documents HTML, il suffit de regarder leur extension : **.html**.

On dit que le langage HTML est une langage de balisage car il est composé de **balises**. Les balises HTML correspondent à des éléments du code HTML d'une page web sur Internet. Elles sont une partie intégrante de la composition de la page puisqu'elles permettent de **structurer les pages web**.

La structure d'une page web est la suivante :

![structure page web](https://github.com/mtellene/Cours/blob/main/NSI_PREMIERE/12_WEB/TP1/asset/structure_page_html.png)

- ```<! DOCTYPE html>``` sert à indiquer au navigateur que le document est un document HTML

- ```<html>...</html>``` sert à délimiter le code HTML de la page

- ```<head>...</head>``` fournit des informations générales (métadonnées) sur le document, incluant son titre et des liens ou des définitions vers des scripts et feuilles de style.

- ```<body>...</body>``` représente le contenu principal du document HTML. 


## II - L'éditeur de code

Avant de commencer à code, vous allez créer votre environnement de travail. Pour ce faire, allez dans votre dossier personnel. Une fois arrivé, créer un dossier "web". Dans ce dossier, créer un dossier "TP1". C'est dans ce dossier que vous sauvegarderez le travail demandé lors de ce TP.

Créons notre premier fichier HTML.

1. Ouvrir **Geany**

2. Sauvegarder votre fichier dans le dossier "web/TP1". Vous nommerez votre fichier "index.html"

3. Maintenant nous pouvons créer notre page web

## III - Quelques manipulations


### 1. Mise en place de la structure

Dans votre fichier créé, copiez le code suivant :

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
    </head>

    <body>

    </body>
</html>
```

---

**Explication du code :**

-  ```<!DOCTYPE html>``` : permet de spécifier que le document écrit est un fichier HTML

-  ```<html lang="fr">``` :
    - la balise ```<html>``` permet de délimiter le code HTML
    - ```lang="fr"``` permet d'indiquer que le document écrit est en français (```lang="en"``` indique un document en anglais par exemple)

-  ```<head>``` : permet de délimiter la partie métadonnées

-  ```<meta charset="utf-8">``` : permet d'indiquer l'encodage de la page, il vous est conseillé de tout le temps utilise l'utf-8 pour encoder vos pages HTML

-  ```<body>``` : permet de délimiter la partie contenu de la page web

- vous pouvez remarquer que le code est indenté. L'indentation se fait lorsque une balise est contenue dans une autre. Vous pouvez voir la page comme ceci : la balise ```<meta charset="utf-8">``` appartient à la balise ```<head>```, qui elle même appartient à la balise ```<html>```.

---

Une fois que le code a été recopié, **sauvegardez-le**. Pour visualiser votre page, allez dans le dossier où le fichier est sauvegardé, puis faites un double-clic sur **index.html**. Votre navigateur s'ouvre et vous pouvez visualiser votre page web. Normalement la page est vide, c'est normal ! Il n'y a rien dans entre les balises ```<body>```.

**Il est à noter que si vous ne sauvegardez pas votre fichier HTML après des modifications, ceeles-ci ne seront pas prises en compte lors de l'affichage de la page**.

Pour terminer la structure de notre page web, ajoutez entre les balises ```<head>``` la ligne suivante :

```html
<title>Ma premiere page</title>
```

Sauvegardez votre page et rafraîchissez-la, normalement le nom de l'onglet de la page est devenu *Ma premiere page*


### 2. Ajouter de l'information

Votre première page est créée, mais celle-ci est un peu vide. Rajoutons de l'informations

1. Commençons par rajouter un titre à notre page. **Le titre fait parti du contenu visible de la page, il faut donc le mettre dans le partie ```<body>```**. Pour ajouter un titre à notre page, nous allons utiliser la balise ```<h1>...</h1>```. Vous allez remplacer les "..." par "Histoire du Web".

Les balises du type ```<h1>...</h1>``` sont des balises de titres. Il existe 6 niveaux de titres. Si l'on veut mettre le titre "Mon titre" au niveau 5, il faudra écrire ```<h5>Mon titre</h5>```.

2. Une fois que c'est fait, nous allons mettre un paragraphe à notre page web. **Le paragraphe fait également parti du contenu visible de la page web**. Pour ce faire, nous allons utiliser une balise ```<p>...</p>``` en remplaçant les "..." par le texte suivant :

```text
Ce site est votre premier site web et il sera consacré à l'histoire du Web. Vous avez déjà écrit le titre de votre page et vous êtes en train d'écrire votre premier paragraphe.
```

Sauvegardez votre page et rafraîchissez-la. Votre page devrez ressembler à ceci :

![vérification page](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/TP1/asset/check_page_titre_p.png)

Vous avez toutes les clés en main pour créer une page web

## IV - À faire

Dans le dossier **ressources**, vous trouverez un fichier **paragraphes.txt** contenant tout le texte à mettre dans votre page.

Le but sera de reproduire la page suivante :

![vérification page](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/TP1/asset/resultat_final.png)

L'image à mettre sur votre page se trouve dans le dossier **ressources**. Un exemple de mise en place d'image est donné [ici](https://github.com/mtellene/NSI/tree/main/PREMIERE/12_WEB/ressources/image.html)


## V - Pour aller plus loin

Une fois que vous avez fini, voici le travail à faire (vous trouverez des exemples de code [ici](https://github.com/mtellene/NSI/tree/main/PREMIERE/12_WEB/ressources)) :

- mettre un lien hypertexte sur "W3C" du dernier paragraphe. Ce lien devra rediriger, au clic sur "W3C, sur la page suivante : https://fr.wikipedia.org/wiki/World_Wide_Web_Consortium

- mettre les mots suivants en gras :
    - ancêtre d'Internet
    - ARPanet
    - réseau militaire
    - base du langage HTML
    - concevoir des pages web

- souligner toutes les dates présentes dans votre page web

- regarder les pages suivantes pour commencer à se renseigner sur le CSS :
    - https://www.csszengarden.com
    - https://flukeout.github.io