from Crypto.Util.number import getPrime
from random import getrandbits

def key_gen(bits):
    p = getPrime(bits)
    q = getPrime(bits)

    n = p*q
    phi_n = (p-1)*(q-1)

    e = 65537
    # La valeur e = 65537 est couramment utilisée pour le chiffrement RSA car elle satisfait deux conditions importantes :
    # e doit être un nombre premier. La valeur 65537 est un nombre premier, et elle est suffisamment grande pour être utilisée en toute sécurité.
    # e doit être relativement petit par rapport à phi_n (où phi_n est la valeur de la fonction d'Euler pour n). Cela permet de garantir que le calcul de la clé privée d peut être effectué efficacement.
    # La valeur 65537 a l'avantage supplémentaire d'être facile à implémenter en binaire, ce qui permet d'accélérer les calculs de chiffrement et de déchiffrement.
    # Il convient de noter que d'autres valeurs de e peuvent également être utilisées avec succès pour le chiffrement RSA, à condition qu'elles satisfont les deux conditions mentionnées ci-dessus. Cependant, la valeur 65537 est largement utilisée et considérée comme une bonne pratique de sécurité pour le chiffrement RSA.

    d = pow(e, -1, phi_n)

    return (e,n), (d,n)


def encrypt(kp, m):
    return pow(m, kp[0], kp[1])

def decrypt(kpr, c):
    return pow(c, kpr[0], kpr[1])

def encrypt_texte(kp, m):
    crypted_list = []
    for char in m:
        crypted_list.append(encrypt(kp, ord(char)))
    return crypted_list

def decrypt_texte(kpr, c):
    s = ""
    for i in range(len(c)):
        s += chr(decrypt(kpr, c[i]))
    return s


kp, kpr = key_gen(1024)

m = 77
c = encrypt(kp, m)
print(c)
print(decrypt(kpr, c))


#m = getrandbits(100)   # pour générer un nombre aléatoire sur 100 bits
#c = encrypt(kp, m)
#m_2 = decrypt(kpr, c)

#print("m original =", m)
#print("c =", c)
#print("m déchiffré =", m_2)

#m = "Envoyez 2500e"
#c = encrypt_texte(kp, m)
#m_2 = decrypt_texte(kpr, c)

#print("m original =", m)
#print("c =", c)
#print("m déchiffré =", m_2)
