# TP - Création d'une page web dynamique (HTML/CSS/JavaScript)

## I - Historique
## II - Manipulations simples en console
## III - Intégrer du Javascript dans une page web
### 1. Création d'un compteur
### 2. Changement de couleur
### 3. Le Snake
### 4. Améliorations du Snake
---

## I - Historique

JavaScript (1995) est un langage de programmation de scripts principalement employé dans les pages web interactives et à ce titre est une partie essentielle des applications web. Avec les langages HTML et CSS, JavaScript est au cœur des langages utilisés par les développeurs web. Une grande majorité des sites web l'utilisent, et la majorité des navigateurs web disposent d'un moteur JavaScript5 pour l'interpréter.

Tout d'abord créer un dosser "TP3" dans votre dossier "web". Dans ce dossier créer un fichier "index.html". Pour le moment, ce fichier contiendra une page HTML vide, vous pouvez recopier le code suivant :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>TP3</title>
        <meta charset="utf-8">
    </head>

    <body>
        <script src="script.js"></script>
    </body>
</html>
```

La ligne 

```html
<script src="script.js"></script>
```

permet de faire un lien entre votre fichier HTML et un fichier JavaScript ```script.js```. Cette devra être la dernière avec la balise ```</body>``` Une fois fait, ouvrez votre page dans un navigateur et ouvrez la console. La touche habituelle pour ouvrir la console est ```F12```, puis aller dans l'onglet "console".


## II - Manipulations simples en console

Ce que vous venez d'ouvrir est la console du navigateur. Cette console peut être comparée à la partie basse de Thonny, elle permet de faire des affichages et de taper du code JavaScript.

Dans la console, tapez les instructions suivantes :

- ```3+4```
- ```"salut" + "ça va ?"```
- ```3 == 3```
- ```3 === 3```
- ```"3" == 3```
- ```"3" === 3```

Vous pouvez remarquer que les derniers appels sont intrigants. Le JavaScript possède un opérateur de comparaison particulier, le ```===```. Pour résumé : l'égalité faible (```==```) effectuera une conversion des deux éléments à comparer avant d'effectuer la comparaison. L'égalité stricte (```===```) effectuera la même comparaison mais sans conversion préalable (elle renverra toujours false si les types des deux valeurs comparées sont différents).

Avant de passer à l'étape suivante, il est à noter que la console "sera votre meilleure amie". En effet, en plus de pouvoir faire des manipulations, cette dernière affiche les possibles erreurs de vos programmes mais fait également de l'affichage. Pour faire de l'affichage en Python, nous utilisons l'instruction ```print(machin_à_afficher)```, en JavaScript nous utiliserons ```console.log(machin_à_afficher)```


## III - Intégrer du Javascript dans une page web

### 1. Création d'un compteur

Le JavaScript est utilisé pour faire de la **programmation évenementielle**, c'est à dire faire des choses en fonction d'actions de l'utilisateur. Prenons le cas le plus simple : un bouton. Nous allons créer un compteur.

Commencez par créer une division ayant l'```id``` *partie1*. Dans cette division, créez un paragraphe ayant pour contenu *0* et comme ```id``` la valeur *compteur*.


Ensuite, créez un division (```div```) ayant comme ```id``` la valeur *boutons*. Cette division contiendra 3 boutons :

- Un premier bouton ayant comme ```ìd``` et comme ```value``` la valeur *baisser*. Dans le bouton, le message "Baisser" devra être écrit
- Un deuxième bouton ayant comme ```ìd``` et comme ```value``` la valeur *reset*. Dans le bouton, le message "Reset" devra être écrit
- Un troisième bouton ayant comme ```ìd``` et comme ```value``` la valeur *augmenter*. Dans le bouton, le message "Augmenter" devra être écrit

Maintenant, allons dans le fichier JavaScript. Commençons par créer une **variable**. En JavaScript, les variables doivent être précédées du mot clé ```let``` ou du mot-clé ```var```. ```let``` permet de déclarer des variables dont la portée est limitée à celle du bloc dans lequel elles sont déclarées. ```var```, quant à lui, permet de définir une variable globale ou locale à une fonction (sans distinction des blocs utilisés dans la fonction). Créez une variable ```valeur_compteur``` initialisée à 0.

**Il est à noter qu'en JavaScript, les instructions se terminent par un ";"**

Nous allons nous occuper du bouton *Augmenter*. Il faudra dans un premier temps, récupérer le bouton dans une variable. Pour ce faire, nous allons devoir utiliser la syntaxe suivante :

```js
let nom_variable = document.getElementById("id_de_l_element");
```

En utilisant la syntaxe, récupérez l'élément dans une variable.  
    
Une fois que l'élément est récupéré dans une variable, il faut lui mettre un **écouteur d'événements**. Cette mise en place se fait de la manière suivante :

```js
nom_variable.addEventListener("nature_evenement", action_a_faire);
```

Ici, la nature de l'événement est un clic (```click``` en anglais) et l'action à faire sera ```augmenter_compteur```.

Maintenant que l'écouteur est en place, il nous faut créer l'action. Pour ce faire nous allons créer la fonction ```augmenter_compteur```. En JavaScript, une fonction se défini de la manière suivante :

```js
function nom_de_la_fonction(argument.s_de_la_fonction){
    corps_de_la_fonction
}
```

Voici ce qu'il faudra faire dans votre fonction :

- Récupérer le paragraphe ayant l'```id``` *compteur* dans une variable JavaScript
- Augmenter la variable ```valeur_compteur``` de 1
- Remplacer le contenu du paragraphe récupéré par le contenu de la variable ```valeur_compteur```. Pour ce faire il va falloir utilisé une instruction de la forme :

```js
nom_de_la_variable_contenant_le_texte.innerHTML = valeur_a_mettre;
```

Si vous avez bien fait les différents liens, lorsque vous cliquez sur le bouton *Augmenter*, le texte devrait augmenter de *1*.

Faire de même pour le bouton *reset* et le bouton *baisser*.


### 2. Changement de couleur

Créez sous la division *partie1*, créez une nouvelle division ayant pour ```id``` la valeur *partie2*. Pour séparer avec la *partie1*, vous pouvez appliquer à *partie2* le style ```margin-top: 5%;```.

Dans cette division créez un paragraphe vide ayant pour ```id``` la valeur *paragraphe*.

Sous ce paragraphe, créez un élément ```select``` ayant comme ```id``` la valeur *couleurs*. Vous trouverez des informations [ici](https://fr.w3docs.com/apprendre-html/html-tag-select.html) sur la balise ```select```. Notre élément ```select``` contiendra 4 options (balise ```option```).

- Une option *-- Choisir une couleur --*. Cette option devra être présélectionnée lors du chargement de la page **MAIS** ne doit avoir aucun effet sur la page (vous pouvez obtenir de l'aide [ici](https://stackoverflow.com/questions/3518002/how-can-i-set-the-default-value-for-an-html-select-element)). Cette option devra avoir pour ```value``` une chaîne de caractères vide.

- Une option *Rouge*. Cette option devra avoir pour ```value``` la valeur *rouge*.

- Une option *Vert*. Cette option devra avoir pour ```value``` la valeur *vert*.

- Une option *Bleu*. Cette option devra avoir pour ```value``` la valeur *bleu*.

Le but de cette partie sera d'écrire un code JavaScript qui, lorsqu'une couleur est sélectionnée, met à jour la paragraphe. Cette mise fera en sorte que la couleur choisie soit écrit dans le paragraphe. De plus, la couleur de paragraphe devra être celle de la couleur choisie.

Afin de gérer la mise à jour, vous devrez utiliser la fonction ```setInterval()``` de JavaScript. Vous trouverez des informations sur cette fonction [ici](https://www.w3schools.com/jsref/met_win_setinterval.asp).

Vous devrez également utiliser une structure ```if```. Voici la syntaxe en JavaScript :

```js
if(condition_à_satisfaire){
    bloc_if;
} else if(condition_à_satisfaire){
    bloc_else_if;
} else{
    bloc_else;
}
```


### 3. Le Snake

Créez trois nouveaux fichiers ```snake.html```, ```styles.css``` et ```script_snake.js```. Liez ces trois fichiers.

Recopiez le ```body``` suivant :

```html
<body onload="init()">
    <h1 style="text-align: center; font-size: 2em;">SNAKE</h1>
    <canvas id="aire_jeu" width="300" height="300"></canvas>
    <script src="script_snake.js"></script>
</body>
```

Dans le fichier ```styles.css```, vous mettrez en noir le fond du canvas.

Maintenant, nous allons passer au code JavaScript, le plus gros du travail.

Tout d'abord, créez avec le mot-clé ```var``` une variable ```canvas``` ainsi qu'une variable ```ctx```. Ensuite, vous l'avez peut-être remarqué, mais dans la balise ```body```, il est écrit ```onload="init()"```. Cela veut dire que lorsque la page est chargée, la fonction ```init()``` va se lancer. Nous allons donc écrire cette fonction.

Recopiez et complétez la fonction à trous suivante :

```js
function init() {
    ..... //récupérer l'élément avec l'id "aire_jeu" dans la variable canvas
    ctx = canvas.getContext('2d');

    ..... // appeler la fonction charger_image (on l'écrira plus tard)
    ..... // appeler la fonction creer_serpent (on l'écrira plus tard)
    ..... // appeler la fonction placer_pomme (on l'écrira plus tard)
    setTimeout("cycle_jeu()", DELAY);
}   
```

Vous pouvez voir que la fonction utilise la constante ```DELAY```. En utilisant le mot-clé ```const```, créez la constante ```DELAY``` avec la valeur 140.

Une fois fait, nous allons nous occuper de la fonction ```charger_image```. Cette fonction sert à récupérer les images pour notre jeu. Tout d'abord, sous les variables ```canvas``` et ```ctx``` (au début de votre fichier), créez, en utilisant le mot-clé ```var```, trois variables : ```tete```, ```corps``` et ```pomme```. Maintenant créez la fonction ```charger_image```, et dans celle-ci, il va falloir pour chacune des variables ```tete```, ```corps``` et ```pomme``` :

- créez un nouvel objet ```Image```
- fixer la source avec l'image appropriée. Vous trouverez les images dans le dossier ```ressources/```

Vous trouverez [ici](https://developer.mozilla.org/fr/docs/Web/API/HTMLImageElement/Image) une aide concernant les images.

Occupons-nous à présent de la fonction ```creer_serpent```. Cette fonction sert à créer et garder les coordonnées du notre serpent. Pour ce faire, nous allons commencer par créer trois variables et une constante.

- Créez une constante ```TOUS_LES_POINTS``` initialisée avec la valeur *900*
- Créez deux variables (avec le mot-clé ```var```) : ```x``` et ```y```. Ces variables seront des tableaux ayant une taille de ```TOUS_LES_POINTS``` éléments. Pour créer un tableau en JavaScript, il faut utiliser la syntaxe suivante :

```js
var nom_variable = new Array(taille_du_tableau);
```

- Créez une dernière variable ```points``` non intiliasée. Vous utiliserez le mot-clé ```var```

Une fois que la constante et les variables sont créées, nous allons passer à la fonction. Recopier et compléter la fonction ```creer_serpent``` suivante :

```js
function creer_serpent() {
    ..... // fixer la valeur de la variable "points" à 3

    for(var z = .....; z < .....; z++) { // pour "z" allant de 0 à "points"
        ..... // fixer l'élément "z" du tableau "x" à 50-z*10
        ..... // fixer l'élément "z" du tableau "y" à 50
    }
}
```

Nous n'allons pas faire la fonction ```placer_pomme``` pour le moment, nous allons plutôt faire ```cycle_jeu```. La réalisation de cette fonction va nous permettre de tester une première version de notre jeu. L'idée de cette fontion est la suivante : tant que le joueur est en vie, en fait une étape de vérification, on se déplace et on met à jour le canvas. Cette fonction se répéte tant que le joueur est en vie, il va donc falloir créer une variable.

Créez une variable ```en_vie``` initialisée à ```true```. **A noter :** en JavaScript on écrit ```true``` et ```false``` et non ```True``` et ```False``` comme en Python.

Une fois cette variable créée, recopier et compléter la fonction ```cycle_jeu``` suivante : 

```js
function cycle_jeu() {
    
    ..... // si le joueur est en vie

        ..... // appeler la fonction verifier_pomme
        ..... // appeler la fonction verifier_collisions
        ..... // appeler la fonction deplacement
        ..... // appeler la fonction dessiner
        setTimeout("cycle_jeu()", DELAY);

}
```

Nous allons nous occuper de la fonction ```dessiner```, cette fonction va gérer l'affichage de notre jeu. Recopier et compléter la fonction suivante :

```js
function dessiner() {
    ctx.clearRect(0, 0, C_WIDTH, C_HEIGHT);

    ..... // si le joueur est en vie
        ctx.drawImage(pomme, pomme_x, pomme_y);

        ..... // pour z allant de 0 à "points" de 1 en 1

            if (z == 0) { ctx.drawImage(tete, x[z], y[z]); } 
            else { ctx.drawImage(corps, x[z], y[z]); }

    ..... // sinon on appel la fonction game_over
}
```

Vous pouvez remarquer que notre fonction utilise deux constantes : ```C_WIDTH``` et ```C_HEIGHT```. Créez ces deux constantes avec la valeur *300*. En plus, de ces deux constantes, la fonction ```dessiner``` utilise également deux variables : ```pomme_x``` et ```pomme_y```. Sous la variable ```pomme``` (en haut de votre fichier), créez les deux variables (elles n'ont pas besoin d'être initialisées).

**Si vous avez tout bien fait**, rafraîchissez votre page et vous devriez avoir ceci :

![snake1](https://github.com/mtellene/NSI/blob/main/PREMIERE/12_WEB/TP3/assets/snake1.png)

Si tout est bon, passons à la suite : occupons-nous du déplacement. En effet, le snake est jeu basé sur le déplacement d'un serpent, or nous ne pouvons pas le déplacer pour l'instant. Commencez par créer en haut de votre fichier quatre variables :

- ```direction_gauche``` initialisée à ```false```
- ```direction_droite``` initialisée à ```true```
- ```direction_haut``` initialisée à ```false```
- ```direction_bas``` initialisée à```false```

Pour la fonction ```deplacement```, il nous faudra également créer une constante ```TAILLE_POINT``` initialisée avec la valeur *10*.

Recopier et compléter la fonction ```deplacement``` suivante :

```js
function deplacement() {
    ..... // pour z allant de "points" à 1 en allant de -1 en -1
        ..... // fixer l'élément z de x avec la valeur de l'élément (z-1) de x
        ..... // fixer l'élément z de y avec la valeur de l'élémen (z-1) de y

    ..... // si direction_droite est à true
        ..... // on enlève à x[0] la valeur TAILLE_POINT

    
    ..... // si direction_gauche est à true
        ..... // on ajoute à x[0] la valeur TAILLE_POINT
    

    ..... // si direction_haut est à true
        ..... // on enlève à y[0] la valeur TAILLE_POINT

    
    ..... // si direction_bas est à true
        ..... // on ajoute à y[0] la valeur TAILLE_POINT
}
```

Si vous rafraîchisser votre page, vous allez voir le serpent se déplacement vers la droite de la fenêtre et sortir de celle-ci. Il va donc falloir fixer deux problèmes : gérer la sortie de la fenêtre **et** pouvoir changer de direction.

Occupons-nous de la gestion de la sortie de l'écran. Pour ce faire, nous allons écrire la fonction ```verification_collisions```. Recopier et compléter la fonction suivante :

```js
function verifier_collision() {

    ..... // pour z allant de "points" à 1 de -1 en -1
        ..... // si z>4 ET x[0] est égal à x[z] ET y[0] est égal à y[z]
            ..... // en_vie passe à false

    ..... // si y[0]>=C_HEIGHT OU y[0]<0 OU x[0]>=C_WIDTH OU x[0]<0
        ..... // en_vie passe à false

}
```

En JavaScript, le **et** se fait comme ceci ```&&```, et le **ou** se fait comme ceci ```||```.

Une fois fait, vous pouvez recopier la fonction ```game_over``` suivante :

```js
function game_over() {
    ctx.fillStyle = 'white';
    ctx.textBaseline = 'middle'; 
    ctx.textAlign = 'center'; 
    ctx.font = 'normal bold 18px serif';
    
    ctx.fillText('Game over', C_WIDTH/2, C_HEIGHT/2);
}
```

Maintenant, si vous rafraîchissez votre page, vous pouvez voir que lorsque le serpent sort de la fenêtre le message *Game Over* s'affiche. Nous avons réglé un premier problème, réglons maintenant le deuxième : déplacer le serpent. Premièrement, récupérons les touches du clavier, pour faire créer quatre constantes :

- ```TOUCHE_GAUCHE``` initialisée avec *37*
- ```TOUCHE_DROITE``` initialisée avec *39*
- ```TOUCHE_HAUT``` initialisée avec *38*
- ```TOUCHE_BAS``` initialisée avec *40*

Une fois fait, recopier et compléter le code suivant (ce dernier sera à mettre à la toute fin de ```script_snake.js```):


```js
onkeydown = function(e) {
    
    var key = e.keyCode; // ici on récupère la touche enfoncée
    
    ..... // si key égal à TOUCHE_GAUCHE et que direction_droite est false
        
        ..... // on met direction_gauche à true
        ..... // on met direction_haut à false
        ..... // on met direction_bas à false


    ..... // si key égal à TOUCHE_DROITE et que direction_gauche est false
        
        ..... // on met direction_droite à true
        ..... // on met direction_haut à false
        ..... // on met direction_bas à false


    ..... // si key égal à TOUCHE_HAUT et que direction_bas est false
        
        ..... // on met direction_haut à true
        ..... // on met direction_droite à false
        ..... // on met direction_gauche à false

    
    ..... // si key égal à TOUCHE_BAS et que direction_haut est false
        
        ..... // on met direction_bas à true
        ..... // on met direction_gauche à false
        ..... // on met direction_droite à false      
};
```

Rafraîchisser votre page, votre serpent devrait changer de direction. Vérifier également que la sortie de l'écran par le haut, le bas et la gauche fonctionne.

Passons maintenant à la dernière étape du projet : faire grandir le serpent. Pour ce faire, nous utiliserons un système simple :

- On génère des coordonnées aléatoires
- On place une pomme aux coordonnées correspondantes
- Si le serpent passe sur le pomme, celle-ci disparaît et la taille du serpent augmente
- Tant qu'il y a une pomme sur le plateau, aucune autre ne doit être générée

Commençons par la fonction ```placer_pomme```. Premièrement, nous allons créer une constante ```MAX_ALEATOIRE```. Vous attribuerez à cette constante la valeur *29*. Cette constante va nous servir à borner nos coordonnées. En effet, en JavaScript, il n'existe pas de fonction permettant de générer un nombre aléatoires entre deux bornes. Ce qu'il faut faire c'est multiplier un nombre aléatoire par la borne maximum, puis faire un arrondi du nombre obtenu :

- ```var alatoire = Math.floor(Math.random() * 10);``` : génère un nombre entier aléatoire en 0 et 10

- ```var alatoire = Math.floor(Math.random() * 1);``` : génère un nombre entier aléatoire en 0 et 1

Recopier et compléter la fonction ```placer_pomme``` :

```js
function placer_pomme() {
    ..... // génère un nombre aléatoire entre 0 et MAX_ALEATOIRE
    ..... // on met le produit du nombre précédent et de TAILLE_POINT dans la variable pomme_x

    // on suit la même démarche pour pomme_y

    .....
    .....
}
```

En rafraîchissant la page, vous verez qu'une pomme est placée sur le plateau de jeu, mais vous avez beau lui passer dessus avec le serpent, celle-ci ne disparaît pas **et** votre serpent n'augmente pas de taille. Ceci s'explique par le fait que nous ne vérifions pas si le serpent "entre en collision" avec la pomme. Cette fonctionnalité est gérée par la fonction ```verifier_pomme```. Cette fonction vérifie si les coordonnées de la tête sont égales aux coordonnées de la pomme. Si cela est vrai, alors on augmente la variable ```points``` de *1* (ici ```points``` symbolise le nombre parties qui composent le serpent). Ensuite, on place une nouvelle pomme.

Si ce n'est pas le cas, on ne fait rien.

Écrire la fonction ```verifier_pomme```.

Arrivé à ce point, votre snake devrait être fonctionnel.


### 4. Améliorations du Snake

Voici quelques idées d'améliorations :

- implémenter un score, celui-ci devra être affiché dynamiquement (donc mis à jour). Le score augmente quand le serpent passe sur une pomme

- créer un bouton rejouer qui s'affiche en cas de game over

- faire un tableau des scores affichant le nom et le score des 3 meilleurs joueurs. Ce tableau devra être mis à jour

- faire apparaître d'autres fruits, à d'autres fréquences qui augmente le score différemment

- faire apparaître des obstacles


