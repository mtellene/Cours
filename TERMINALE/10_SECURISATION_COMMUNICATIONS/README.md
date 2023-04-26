## Dossier sécurisation des communications


## Indications et exercices faits en cours

**Modèle OSI** : norme de communication de tous les systèmes informatiques. Cadre conceptuel qui définit comment les systèmes réseaux communiquent et envoie des données d'un expéditeur à un destinataire. Le **modèle OSI** correspond à la théorie, alors que le **modèle TCP/IP** correspond à la pratique.


### Chiffrement asymétrique

- **Principe** : le cryptosystème met en jeu 2 clés, une pour le chiffrement (**Kp**) et une pour le déchiffrement (**Kpr**)
- Chaque utilisateur possède une paire de clé (Kp, Kpr)
- Kp est la clé publique. Elle peut être connue de tous et diffusée dans un annuaire
- Kpr est la clé privée. Elle doit être gardée secrète et connue uniquement de son propriétaire


**Avantages du chiffrement asymétrique**
- échange des clés publiques sur un canal non sécurisé
- possibilité de créer une base de données de clé publique
- authentification des messages (signature électronique)
- le nombre de clé croît linéairement avec le nombre d'utilisateur

**Inconvéntients du chiffrement asymétrique**
- temps de calcul et espace mémoire utilisé important
- moins rapide que les cryptosystème symétriques
- problème de validité de clé publique : il faut avoir confiance en l'organisme tierce qui fournit et certifie les clés
- afin de garantir la sécurité, la longueur des clés doit être très grandes (1024 --> 4096 bits)


##### Exercices sur la génération de clés

Soient *p = 3* et *q = 5*, calculer les clés

1. *n = p x q = 3 x 5 = 15*
2. *&phi;(n) = (p-1)(q-1) = 2 x 4 = 8*
3. *e = 3*  #pour rappel *e* est générer de tel sorte qu'il est premier avec *&phi;(n)*
4. Calcul de *d* :

*e x d = 1 mod &phi;(n)*

*=> 3 x d = 1 mod 8*

*=> 3 x d = 1 + k x 8*

Afin de calculer *d*, on applique l'algorithme d'Euclide étendue. Ici, nous allons le faire à la main (l'algorithme n'est pas expliqué, seulement les calculs sont donnés)

*=> 8 = 3 x 2 + 2*

*=> 3 = 2 x 1 + 1*

*=> 1 = 3 - 2*

*=> 1 = 3 - (8 - 3 x 2)*

*=> 1 = 3 - 8 + 3 x 2*

*=> 1 = 3 x 3 - 8*


*=> 3 x 3 = 1 + 8*

Donc *d = 3*. On a *Kp(3, 15)* et *Kpr(3, 15)*

---------------------------------------------------------------------

Soient *p = 11* et *q = 7*, calculer les clés

1. *n = p x q = 11 x 7 = 77*
2. *&phi;(n) = (p-1)(q-1) = 10 x 6 = 60*
3. *e = 11*
4. Calcul de *d* :

*e x d = 1 mod &phi;(n)*

*=> 11 x d = 1 mod 60*

*=> 11 x d = 1 + k x 60*

Afin de calculer *d*, on applique l'algorithme d'Euclide étendue.

*=> 60 = 11 x 5 + 5*

*=> 11 = 5 x 2 + 1*

*=> 1 = 11 - 5 x 2*

*=> 1 = 11 - (60 - 11 x 5) x 2*

*=> 1 = 11 - 60 x 2 + 11 x 10*

*=> 1 = 11 x 11 - 60 x 2*

*=> 11 x 11 = 1 + 2 x 60*

Donc *d = 11*. On a *Kp(11, 77)* et *Kpr(11, 77)*

---------------------------------------------------------------------

Soient *p = 3* et *q = 5* et *e = 5*, calculer les clés

1. *n = p x q = 3 x 5 = 15*
2. *&phi;(n) = (p-1)(q-1) = 2 x 4 = 8*
3. Calcul de *d* :

*e x d = 1 mod &phi;(n)*

*=> 5 x d = 1 mod 8*

*=> 5 x d = 1 + k x 8*

Afin de calculer *d*, on applique l'algorithme d'Euclide étendue. Ici, nous allons le faire à la main (l'algorithme n'est pas expliqué, seulement les calculs sont donnés)

*=> 8 = 5 x 1 + 3*

*=> 5 = 3 x 1 + 2*

*=> 3 = 2 x 1 + 1*

*=> 1 = 3 - 2*

*=> 1 = 3 - (5 - 3)*

*=> 1 = 3 - 5 + 3*

*=> 1 = 3 x 2 - 5*

*=> 1 = (8 - 5) x 2 - 5*

*=> 1 = 8 x 2 - 5 x 2 - 5*

*=> 1 = 8 x 2 - 5 x 3*

*=> (-5) x 3 = 1 - 2 x 8*
Ici on a un problème car on a un *e* négatif, on ajoute donc *e x &phi;(n)* des deux côtés.

*=> (-5) x 3 + 5 x 8 = 1 - 2 x 8 + 5 x 8*

*=> 5 x 5 = 1 - 3 x 8*

Donc *d = 5*. On a *Kp(5, 15)* et *Kpr(5, 15)*

---------------------------------------------------------------------

Soient *p = 11* et *q = 13* et *e = 24*

1. Calculer le module clé publique/privée.
salut
2. t







