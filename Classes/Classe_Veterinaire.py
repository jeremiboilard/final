

# import date
import datetime
from datetime import date

# import Classe_Enclos
from Classe_Enclos import *

class Veterinaire:
    """
    Classe Vétérinaire
    """
    # attribut de classe
    ls_veterinaire = []

    def __init__(self, p_numero_emp: str = "", p_nom: str = "", p_prenom: str = "", p_date_naiss: date = "",
                 p_list_enclos: list = []):
        """
        Contstructeur de la classe Vétérinaire
        :param p_numero_emp: Numéro de l'employé
        :param p_nom: Nom du vétérinaire
        :param p_prenom: Prénom du vétérinaire
        :param p_date_naiss: Date de naissance du vétérinaire
        :param p_list_enclos: Liste qui contient les enclos assignés au vétérinaire
        """
        self._numero_emp = p_numero_emp  # Attribut privé
        self._nom = p_nom  # Attribut privé
        self._prenom = p_prenom  # Attribut privé
        self._date_naiss = p_date_naiss  # Attribut privé
        if p_list_enclos is None:
            self.list_enclos = []
        else:
            self.list_enclos = p_list_enclos  # Attribut publique


    # Propriété Numero_emp
    @property
    def Numero_emp(self):
        return self._numero_emp

    @Numero_emp.setter
    def Numero_emp(self, p_num_emp):
        if p_num_emp[0:3].isalpha() and p_num_emp[3:5].isnumeric():
            self._numero_emp = p_num_emp

    # Propriété Nom
    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, p_nom):
        if len(p_nom) <= 50 and p_nom.isalpah():
            self._nom = p_nom

    # Propriété Prenom
    @property
    def Prenom(self):
        return self._prenom

    @Prenom.setter
    def Prenom(self, p_prenom):
        if p_prenom <= 50 and p_prenom.isalpha():
            self._prenom = p_prenom

    # Propriété Date_naiss
    @property
    def Date_naiss(self):
        return self._date_naiss

    @Date_naiss.setter
    def Date_naiss(self, p_date_naiss):
        if p_date_naiss < datetime.date.today():
            self._date_naiss = p_date_naiss

    def calculer_age(self):
        date_ajd = datetime.date.today()
        age = date_ajd - self._date_naiss
        return age

    def prendreRetraite(age):
        if age >= 60:
            return True
        else:
            return False
    def ajouterEnclos(self):
        enclos1 = Enclos()
        return self.list_enclos.append(enclos1)

    def verifier_enclos(self):
        if Enclos.veterinaire == self._nom:
            Veterinaire.ls_veterinaire.append(Enclos)