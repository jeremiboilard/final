class Reptile :
    def __init__(self, p_venimeux : bool = False):
        """
        Constructeur de la classe Reptile
        :param p_venimeux: Venimeux ou non
        """
        self._venimeux = p_venimeux

    @property
    def venimeux(self):
        return self._venimeux

    @venimeux.setter
    def venimeux(self, p_venimeux):
        if p_venimeux is True or p_venimeux is False:
            self._venimeux = p_venimeux