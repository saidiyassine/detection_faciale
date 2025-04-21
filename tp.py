from PyQt5.QtWidgets import QInputDialog,QGridLayout, QApplication, QMainWindow, QComboBox, QLineEdit, QTableWidget, \
    QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QGroupBox, QMessageBox
from PyQt5.QtCore import Qt
from pymongo import MongoClient

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialiser la fenêtre
        self.setWindowTitle("Gestion de la Production")
        self.resize(800, 600)

        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['production']
        self.collection = self.database['productionC']

        # Créer les widgets
        self.region_label = QLabel("Région:")
        self.region_combo = QComboBox()
        self.region_combo.addItems(["fes_meknes", "rabat_salé", "casa_settat", "taza"])

        self.code_entreprise_label = QLabel("Code Entreprise:")
        self.code_entreprise_edit = QLineEdit()

        self.nombre_employe_label = QLabel("Nombre Employé:")
        self.nombre_employe_edit = QLineEdit()

        self.production = QLabel("Production:")
        self.production_edit = QLineEdit()

        self.perfermance = QLabel("Perfermance:")
        self.perfermance_edit = QLineEdit()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Code", "Région", "Nombre Employé", "Production", "Perfermance"])
        self.table.setFixedSize(745, 500)

        self.ajouter_btn = QPushButton("Ajouter")
        self.ajouter_btn.setStyleSheet("background-color:#4CAF50;color:white;font-weight:bold;")
        self.supprimer_btn = QPushButton("Supprimer")
        self.supprimer_btn.setStyleSheet("background-color:#f44336;color:white;font-weight:bold;")
        self.quitter_btn = QPushButton("Quitter")
        self.quitter_btn.setStyleSheet("background-color:#555555;color:white;font-weight:bold;")

        self.ajouter_btn.setFixedSize(150, 30)
        self.supprimer_btn.setFixedSize(150, 30)
        self.quitter_btn.setFixedSize(150, 30)

        # Créer des groupes pour entourer les widgets
        region_group = QGroupBox("Sélectionner la région")
        code_employe_group = QGroupBox("Information Production")

        # Organiser les widgets dans des layouts
        grid_layout_region = QGridLayout()
        grid_layout_region.addWidget(self.region_label, 0, 0)
        grid_layout_region.addWidget(self.region_combo, 0, 1)
        region_group.setLayout(grid_layout_region)
        region_group.setFixedSize(900, 130)

        grid_layout_code_employe = QGridLayout()
        grid_layout_code_employe.addWidget(self.code_entreprise_label, 0, 0)
        grid_layout_code_employe.addWidget(self.code_entreprise_edit, 0, 1)
        grid_layout_code_employe.addWidget(self.nombre_employe_label, 1, 0)
        grid_layout_code_employe.addWidget(self.nombre_employe_edit, 1, 1,)
        grid_layout_code_employe.addWidget(self.production, 2, 0)
        grid_layout_code_employe.addWidget(self.production_edit, 2, 1)
        grid_layout_code_employe.addWidget(self.perfermance, 3, 0)
        grid_layout_code_employe.addWidget(self.perfermance_edit, 3, 1)

        # Nouveau layout pour les boutons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.ajouter_btn)
        buttons_layout.addWidget(self.supprimer_btn)
        buttons_layout.addWidget(self.quitter_btn)

        grid_layout_code_employe.addLayout(buttons_layout, 4, 1, 1, 2)

        grid_layout_code_employe.addWidget(self.table, 5, 1, alignment=Qt.AlignCenter)
        code_employe_group.setLayout(grid_layout_code_employe)
        code_employe_group.setFixedSize(1400, 800)

        # Organiser les widgets
        layout = QVBoxLayout()

        # Ajouter les groupes au layout
        layout.addWidget(region_group, alignment=Qt.AlignCenter)
        layout.addWidget(code_employe_group, alignment=Qt.AlignCenter)

        # Ajouter le layout à la fenêtre principale
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connecter les boutons
        self.charger_donnees()

        self.ajouter_btn.clicked.connect(self.ajouter_ligne)
        self.supprimer_btn.clicked.connect(self.supprimer_ligne)

        self.quitter_btn.clicked.connect(self.close)

    def charger_donnees(self):
        # Charger les données depuis la base de données
        cursor = self.collection.find()
        self.table.setRowCount(0)

        for row_number, document in enumerate(cursor):
            self.table.insertRow(row_number)
            self.table.setItem(row_number, 0, QTableWidgetItem(str(document["code"])))
            self.table.setItem(row_number, 1, QTableWidgetItem(str(document["region"])))
            self.table.setItem(row_number, 2, QTableWidgetItem(str(document["Nombre_emplye"])))
            self.table.setItem(row_number, 3, QTableWidgetItem(str(document["production"])))
            self.table.setItem(row_number, 4, QTableWidgetItem(str(document["perfermance"])))

    
    def ajouter_ligne(self):
        # Récupérer les valeurs des champs d'entrée
        code_entreprise = self.code_entreprise_edit.text()
        region = self.region_combo.currentText()
        nombre_employe = self.nombre_employe_edit.text()
        production = self.production_edit.text()
        perfermance = self.perfermance_edit.text()

        # Vérifier si tous les champs sont remplis
        if not code_entreprise or not region or not nombre_employe or not production or not perfermance:
            QMessageBox.warning(self, "Attention", "Veuillez remplir tous les champs.")
            return

        # Ajouter les données à la base de données
        data = {
            "code": code_entreprise,
            "region": region,
            "Nombre_emplye": nombre_employe,
            "production": production,
            "perfermance": perfermance
        }

        self.collection.insert_one(data)

        # Mettre à jour l'affichage de la table
        self.charger_donnees()

        # Effacer les champs d'entrée après l'ajout
        self.code_entreprise_edit.clear()
        self.nombre_employe_edit.clear()
        self.production_edit.clear()
        self.perfermance_edit.clear()

        QMessageBox.information(self, "Succès", "Données ajoutées avec succès.")

    def supprimer_ligne(self):
        # Demander à l'utilisateur de saisir le code à supprimer
        code_a_supprimer, ok = QInputDialog.getText(self, "Supprimer une production", "Entrez le code à supprimer:")

        # Vérifier si l'utilisateur a appuyé sur OK et si le code est non vide
        if ok and code_a_supprimer.strip():
            # Supprimer la production de la base de données
            result = self.collection.delete_one({"code":code_a_supprimer})

            if result.deleted_count > 0:
                QMessageBox.information(self, "Succès", "Production supprimée avec succès.")
            else:
                QMessageBox.warning(self, "Avertissement", "Aucune production trouvée avec le code spécifié.")
            
            # Mettre à jour l'affichage de la table
            self.charger_donnees()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

