class Zoo:

    # constructeur
    def __init__(self, nom):
        self.nom = nom
        self.nb_enclos = 0
        self.animaux = {}
        self.enclos_libres = 0

    # méthode ajouter_enclos
    def ajouter_enclos(self):
        self.nb_enclos = self.nb_enclos + 1
        self.enclos_libres = self.enclos_libres + 1

    # méthode ajouter_animaux
    def ajouter_animaux(self, nom_animal, nombre_animal):
        if nom_animal not in self.animaux.keys():
            if self.enclos_libres == 0:
                self.ajouter_enclos()
            self.animaux[nom_animal] = nombre_animal
            self.enclos_libres = self.enclos_libres - 1
        else:
            self.animaux[nom_animal] = self.animaux[nom_animal] + nombre_animal


mon_zoo = Zoo("ZPoo")
mon_zoo.ajouter_enclos()
mon_zoo.ajouter_animaux("lion", 3)
print(mon_zoo.animaux)
mon_zoo.ajouter_animaux("gazelle", 2)
print(mon_zoo.animaux)
mon_zoo.ajouter_animaux("lion", 1)
print(mon_zoo.animaux)
