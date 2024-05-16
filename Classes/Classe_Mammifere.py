class Mammifere:
    def __init__(self, p_couleur_poil : str = ""):
        """
        Constructeur de la classe Mammifere
        :param p_couleur_poil: couleur du poil du mammifere
        """
        self._couleur_poil = p_couleur_poil

    # Propriété couleur_poil
    @property
    def couleur_poil(self):
        return self._couleur_poil

    @couleur_poil.setter
    def couleur_poil(self, p_couleur_poil):
        if p_couleur_poil.isalpha() and p_couleur_poil.lower() in ["noir", "blanche", "brune", "grise", "beige", "multi couleurs"]:
            self._couleur_poil = p_couleur_poil

    # | FONCTION MAGIQUE STR |#
    def __str__(self):
        return f"Mammifère : {self._couleur_poil}"