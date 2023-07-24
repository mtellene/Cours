def lecture_fichier():
    f = open("tous_les_mots.txt", "r")
    ligne = f.readline()
    while ligne != "":
        print(ligne)
        ligne = f.readline()
        
