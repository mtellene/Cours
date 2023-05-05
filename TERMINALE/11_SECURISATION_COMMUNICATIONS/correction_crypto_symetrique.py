def codage_cesar(m, k):
    c = ""

    for caractere in m:
        if caractere.isupper():
            # Trouver la position de la lettre dans l'alphabet
            position = ord(caractere) - 65

            # Appliquer le décalage de la clé et prendre le modulo 26
            nouvelle_position = (position + k) % 26

            # Ajouter la lettre chiffrée au message chiffré
            c += chr(nouvelle_position + 65)
        else:
            # Ajouter des caractères spéciaux tels quels
            c += caractere

    return c


def decodage_cesar(c, k):
    m = ""

    for caractere in c:
        if ord(caractere) >= 65 and ord(caractere) <= 90:
            # Trouver la position de la lettre dans l'alphabet
            position = ord(caractere) - 65

            # Décaler la lettre en fonction de la clé
            nouvelle_position = (position - k) % 26

            # Ajouter la lettre décryptée au message
            m += chr(nouvelle_position + 65)
        else:
            # Ajouter des caractères spéciaux tels quels
            m += caractere
    return m

def codage_xor(m, k):
    assert len(m) >= len(k), "La clé est trop grande !"
    k_repeat = k
    pos = 0
    c = []
    while len(k_repeat) < len(m):
        k_repeat += k[pos]
        pos = (pos + 1) % len(k)

    for i in range(len(m)):
        c.append(ord(m[i]) ^ ord(k_repeat[i]))

    return c


def decodage_xor(c, k):
    assert len(c) >= len(k), "La clé est trop grande !"
    m = ""
    k_repeat = k
    pos = 0
    while len(k_repeat) < len(c):
        k_repeat += k[pos]
        pos = (pos + 1) % len(k)

    for i in range(len(c)):
        m += chr(c[i] ^ ord(k_repeat[i]))
        
    return m


def attaque_brute_force_cesar(c):
    L = []
    for key in range(26):
        L.append(decodage_cesar(c, key))
    return L


def dict_occ(c):
    d_occ = {}
    for lettre in c:
        if lettre in d_occ.keys():
            d_occ[lettre] += 1
        else:
            d_occ[lettre] = 1
    return d_occ

def attaque_analyse_frequentielle_cesar(c):
    d_occ = dict_occ(c)
    d_occ = dict(sorted(d_occ.items(), key=lambda item: item[1], reverse=True))
    L = []
    for key in d_occ.keys():
        k = ord(key) - ord("E")
        L.append(decodage_cesar(c, k))
    return L


def generer_cles(taille_cle, prefixe="", L=[]):
    if taille_cle == 0:
        L.append(prefixe)
    else:
        for i in range(65, 91):
            generer_cles(taille_cle - 1, prefixe + chr(i), L)
        return L


def attaque_force_brute_xor(c):
    taille_cle = 2
    d = {}

    cles = generer_cles(taille_cle)
    for cle in cles:
        d[cle] = decodage_xor(c, cle)
    return d

def recherche_automatique(d):
    f = open("tous_les_mots.txt", "r")
    ligne = f.readline()
    while ligne != "":
        for (k,v) in d.items():
            if v == ligne.upper()[:-1]: print(k)
        ligne = f.readline()


#c = codage_cesar("PROGRAMMATION", 6)
#print(c)
#print(decodage_cesar(c, 6))
#print(attaque_brute_force_cesar(c))
#print(attaque_analyse_frequentielle_cesar(c))


c = codage_xor("PROGRAMMATION", "NSI")
print(c)
print(decodage_xor(c, "NSI"))
#d = attaque_force_brute_xor(c)
#print(d)
#recherche_automatique(d)


