import pytest
from Classe_Veterinaire import *
@pytest.mark.parametrize("age, retour_attendus", [
    (60, True), # age, résultat attendu
    (45, False), # age, résultat attendu
    (78, True), # age, résultat attendu
    (0, False), # age, résultat attendu
    (12, False), # age, résultat attendu
    (15, False), # age, résultat attendu
    (59, False), # age, résultat attendu
    (23423423, True) # age, résultat attendu

])
def test_estadapte(age, retour_attendus):
    assert Veterinaire.prendreRetraite(age) == retour_attendus


    # def prendreRetraite(age):
    #     if age >= 60:
    #         return True
    #     else:
    #         return False