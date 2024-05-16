import pytest
from Classe_Enclos import Enclos
from Classe_Veterinaire import Veterinaire


@pytest.mark.parametrize("taille, nb_animaux,retour_attendus", [
    ("petit", 2, True), # taille, nb_animaux, resultat_attendus
    ("moyen", 4, True), # taille, nb_animaux, resultat_attendus
    ("grand", 6, True), # taille, nb_animaux, resultat_attendus
    ("", 0, False), # taille, nb_animaux, resultat_attendus
    ("petit", 1, True), # taille, nb_animaux, resultat_attendus
    ("moyen", 3, True), # taille, nb_animaux, resultat_attendus
    ("grand", 1, True), # taille, nb_animaux, resultat_attendus

])
def test_estadapte(taille, nb_animaux, retour_attendus):
    assert Enclos.estAdapte(taille, nb_animaux) == retour_attendus

    # def estAdapte(taille, nb_animaux):
    #     if taille == "petit" and nb_animaux <= 2:
    #         return True
    #     elif taille == "moyen" and nb_animaux <= 4:
    #         return True
    #     elif taille == "grand" and nb_animaux <= 6:
    #         return True
    #     else:
    #         return False

