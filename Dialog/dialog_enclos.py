# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_enclos
from PyQt5 import QtWidgets
from Classes.Classe_Enclos import Enclos
######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue enclos")
        self.label.setVisible(False)
        self.label_3.setVisible(False)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        enclos = Enclos()
        enclos._nombre_enclos = self.lineEdit_numenclos.text()
        enclos._nombre_enclos = self.lineEdit_nomenclos.text()
        enclos._taille = self.comboBox_taille.currentText()
        enclos._localisation = self.comboBox_localisation.currentText()
        self.close()
