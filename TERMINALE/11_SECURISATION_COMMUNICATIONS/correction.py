# début de la correction -> crypto_symetrique.py

def codage_cesar(m, k):
  c = ""
  for caractere in m:
    if caractere.isupper():
      # trouver la position de la lettre dans l'alphabet
      position = ord(caractere)- 65   # 65 est le code ASCII du A
      
      # on applique le décalage de la clé et prendre le modulo 26 (26 lettres dans l'alphabet)
      nouvelle_position = (position + k) % 26
      
      # ajouter la lettre chiffrée au message chiffré
      c += chr(nouvelle_position + 65)
    
    else: # si par exemple on a un espace
      c += caractere
  return c


def decodage_cesar(c, k):
  m = ""
  for caractere in c:
    if ord(caractere) >= 65 and ord(caractere) <= 90: # si c'est une lettre majuscule
      # trouver la position de la lettre dans l'alphabet
      position = ord(caractere)- 65   # 65 est le code ASCII du A
      
      # on applique le décalage de la clé et prendre le modulo 26 (26 lettres dans l'alphabet)
      nouvelle_position = (position + k) % 26
      
      # ajouter la lettre chiffrée au message chiffré
      m += chr(nouvelle_position + 65)
    
    else: # si par exemple on a un espace
      m += caractere
  return m


def codage_xor(m, k):
  k_repeated = k
  pos = 0
  c = []
  while len(k_repeated) < len(m): # on fait correspondre la taille de la clé avec la taille du message
    k_repeated += k[pos]
    pos = (pos + 1) % len(k)
    
  for i in range(len(m)):
    c.append(ord(m[i]) ^ ord(k_repeated[i]))
    
  return c


def decodage_xor(c, k):
  m = ""
  k_repeated = k
  pos = 0
  while len(k_repeated) < len(c):
    k_repeated += k[pos]
    pos = (pos + 1) % len(k)

  for i in range(len(m)):
    m += chr(c[i] ^ ord(k_repeated[i]))
    
  return m
  
      
