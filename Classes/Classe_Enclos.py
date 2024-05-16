#import Classe_Animal
#from Classe_Animal import *
#from Classe_Veterinaire import *
class Enclos:
    ls_enclos = []
    nb_enclos = 0
    def __init__(self, p_numero_enclos: str = "", p_nom_enclos: str = "",
                 p_taille: str = "", p_type: str = "", p_localisation: str = "",
                 p_nb_animaux : int = 0, p_veterinaire: str = ""):
        """
        Constructeur de la classe Enclos
        :param p_numero_enclos: numéro de l'enclos
        :param p_nom_enclos: nom de l'enclos
        :param p_taille: taille de l'enclos
        :param p_type: type de l'enclos
        :param p_localisation: localisation de l'enclos
        """
        self._numero_enclos = p_numero_enclos
        self._nom_enclos = p_nom_enclos
        self._taille = p_taille
        self._type = p_type
        self._localisation = p_localisation
        self._nb_animaux = p_nb_animaux
        self._veterinaire = p_veterinaire
        Enclos.ls_enclos.append(self)
        Enclos.nb_enclos += 1

    # Propriété numero_enclos
    @property
    def numero_enclos(self):
        return self._numero_enclos

    @numero_enclos.setter
    def numero_enclos(self, p_numero_enclos):
        if p_numero_enclos[0:4].isnumeric() and p_numero_enclos[5:7].isalpha():
            self._numero_enclos = p_numero_enclos


    # Propriété nom_enclos
    @property
    def nom_enclos(self):
        return self._nom_enclos

    @nom_enclos.setter
    def nom_enclos(self, p_nom_enclos):
        if p_nom_enclos.len() <= 25 and p_nom_enclos.isalpha():
            self._nom_enclos = p_nom_enclos

    # Propriété taille
    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, p_taille):
        if p_taille.isalpha() and p_taille.lower() in ["petit", "moyen", "grand"] :
            self._taille = p_taille

    # Propriété localisation
    @property
    def localisation(self):
        return self._localisation

    @localisation.setter
    def localisation(self, p_localisation):
        if p_localisation.isalpha() and p_localisation.upper() in ["A", "B", "C"]:
            self._localisation = p_localisation

    # Propriété veterinaire
    @property
    def veterinaire(self):
        return self._veterinaire

    @veterinaire.setter
    def veterinaire(self, p_veterinaire):
        if p_veterinaire.isalpha() and p_veterinaire in Veterinaire.ls_veterinaire :
            self._veterinaire = p_veterinaire


    def estAdapte(taille, nb_animaux):
        if taille == "petit" and nb_animaux <= 2 :
            return True
        elif taille == "moyen" and nb_animaux <= 4 :
            return True
        elif taille == "grand" and nb_animaux <= 6 :
            return True
        else:
            return False
