## Dossier sécurisation des communications


## Indications et exercices faits en cours

**Modèle OSI** : norme de communication de tous les systèmes informatiques. Cadre conceptuel qui définit comment les systèmes réseaux communiquent et envoie des données d'un expéditeur à un destinataire. Le **modèle OSI** correspond à la théorie, alors que le **modèle TCP/IP** correspond à la pratique.


### Chiffrement asymétrique

- <u>**Principe**</u> : le cryptosystème met en jeu 2 clés, une pour le chiffrement (**Kp**) et une pour le déchiffrement (**Kpr**)
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
2. *&phi; (n)*




