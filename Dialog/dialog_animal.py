# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        self.label_erreur_numero_animal_existe.setVisible(False)
        self.label_erreur_numero_animal_invalide.setVisible(False)
        self.label_erreur_poids_animal.setVisible(False)
        self.label_erreur_longueur_bec.setVisible(False)
        self.comboBox_famille_animal.currentIndexChanged.connect(self.Choisir_type_animal)
        enclos1 = "123456"
        enclos2 = "456789"
        enclos3 = "567894"
        self.comboBox_enclos_animal.addItem(enclos1)
        self.comboBox_enclos_animal.addItem(enclos2)
        self.comboBox_enclos_animal.addItem(enclos3)
        self.comboBox_enclos_animal.currentIndexChanged.connect(self.ajouter_animal)




    def Choisir_type_animal(self):
        """
        Permet de tester le choix de l'utilisateur (technique ou normal)
        et d'appeler la méthode qui active les contrôles
        """
        if self.comboBox_famille_animal.currentText() == "Mammifères":
            self.comboBox_couleur_poil.setDisabled(False)
            self.lineEdit_longueur_bec.setDisabled(True)
            self.comboBox_venimeux.setDisabled(True)
        if self.comboBox_famille_animal.currentText() == "Oiseaux":
            self.lineEdit_longueur_bec.setDisabled(False)
            self.comboBox_venimeux.setDisabled(True)
            self.comboBox_couleur_poil.setDisabled(True)
        if self.comboBox_famille_animal.currentText() == "Réptiles":
            self.comboBox_venimeux.setDisabled(False)
            self.comboBox_couleur_poil.setDisabled(True)
            self.lineEdit_longueur_bec.setDisabled(True)

    def ajouter_animal(self):
        enclos1 = "123456"
        enclos2 = "456789"
        enclos3 = "567894"
        self.comboBox_enclos_animal.addItem(enclos1)
        self.comboBox_enclos_animal.addItem(enclos2)
        self.comboBox_enclos_animal.addItem(enclos3)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        self.label_erreur_poids_animal.setText("doit être un nombre entier supérieur à 15 lb.")
        self.label_erreur_numero_animal_existe_pas.setText("Le numéro d'animal n'existe pas")
        self.label_erreur_poids_animal.setVisible(False)
        self.label_erreur_numero_animal_invalide.setVisible(False)
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        if self.lineEdit_numero_animal.text() == "":
            self.label_erreur_numero_animal_existe_pas.setVisible(True)
            self.label_erreur_numero_animal_invalide.setVisible(True)
        if self.lineEdit_numero_animal.text()[0:1].isalpha() == False and self.lineEdit_numero_animal.text()[2:6].isnumeric() == False:
            self.label_erreur_numero_animal_invalide.setVisible(True)
        if self.lineEdit_numero_animal.text()[0:1].isalpha() == True and self.lineEdit_numero_animal.text()[2] == "-" and self.lineEdit_numero_animal.text()[3:7].isnumeric() == True:
            self.label_erreur_numero_animal_existe_pas.setVisible(True)
            self.label_erreur_numero_animal_existe_pas.setText("Numéro Valide")
        else:
            self.label_erreur_numero_animal_invalide.setVisible(True)
        if self.lineEdit_poids_animal.text() not in ["15","16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                     "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36",
                                                     "37", "38", "39", "40", "41"]:
            self.label_erreur_poids_animal.setVisible(True)
        if self.lineEdit_poids_animal.text() in ["15","16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
                                                     "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36",
                                                     "37", "38", "39", "40", "41"]:
            self.label_erreur_poids_animal.setVisible(True)
            self.label_erreur_poids_animal.setText("Poids Valide")
        else:
            self.label_erreur_poids_animal.setVisible(True)







