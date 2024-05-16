import jsonpickle
from Classe_Oiseau import Oiseau
from Classe_Mammifere import Mammifere
from Classe_Reptile import Reptile

class Animal:
    nb_animaux = 0
    ls_animaux = []
    def __init__(self, p_numero_animal: str = "", p_surnom: str = "",
                 p_poids: int = 0, p_famille: str = "", p_trait_animal : str = "", p_longueur_bec : Oiseau = Oiseau(),
                 p_couleur_poil : Mammifere = Mammifere(), p_venimeux : Reptile = Reptile(),):
        """
        Constructeur de la classe Animal
        :param p_numero_animal: numéro de l'animal
        :param p_surnom: surnom de l'animal
        :param p_poids: poids de l'animal
        :param p_famille: famille de l'animal
        """
        self._numero_animal = p_numero_animal
        self._surnom = p_surnom
        self._poids = p_poids
        self._famille = p_famille
        self.trait_animal = p_trait_animal
        p_longueur_bec = Oiseau.longueur_bec
        p_couleur_poil = Mammifere.couleur_poil
        p_venimeux = Reptile.venimeux
        #enclos
        #veterinaire

        Animal.nb_animaux +=1
        Animal.ls_animaux.append(self)

    # Propriété numero_animal
    @property
    def numero_animal(self):
        return self._numero_animal

    @numero_animal.setter
    def numero_animal(self, p_numero_animal):
        if p_numero_animal[0:1].isalpha() and p_numero_animal[2] == "-" and p_numero_animal[3:7].isnumeric() :
            self._numero_animal = p_numero_animal

    # Propriété surnom
    @property
    def surnom(self):
        return self._surnom

    @surnom.setter
    def surnom(self, p_surnom):
        self._numero_animal = p_surnom



    # Propriété poids
    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, p_poids):
        if p_poids.isnumeric() and p_poids >= 15:
            self._poids = p_poids

    # Propriété famille
    @property
    def famille(self):
        return self._famille

    @famille.setter
    def famille(self, p_famille):
        if p_famille.lower().capitalize in ["Mammifère", "Oiseau", "Réptile", "Mammifères", "Oiseaux", "Réptiles"] :
            self._famille = p_famille

    # | FONCTION MAGIQUE STR |#
    def __str__(self):
        return (f"Numéro de l'animal : {self._numero_animal}\nSurnom de l'animal : {self._surnom}\n"
                f"Poids de l'animal : {self._poids}\nFamille de l'animal : {self._famille}")

    def serialiser_animal(self):
        """
        Sérialiser un objet étudiant complexe
        :return: None
        """

        with open(self._numero_animal + ".json", "w") as F:
            donnee_objet = jsonpickle.encode(self)
            F.write(donnee_objet)