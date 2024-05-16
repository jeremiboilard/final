class Oiseau:
    def __init__(self, p_longueur_bec : float = 0.0):
        """
        Constructeur de la classe Oiseau
        :param p_longueur_bec: longueur du bec d'un oiseau
        """
        self._longueur_bec = p_longueur_bec

    # Propriété longueur_bec
    @property
    def longueur_bec(self):
        return self._longueur_bec

    @longueur_bec.setter
    def longueur_bec(self, p_longueur_bec):
        if p_longueur_bec.isnumeric() and p_longueur_bec >= 0.0:
            self._longueur_bec = p_longueur_bec