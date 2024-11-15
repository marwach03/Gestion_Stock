import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenu, QAction, QMessageBox, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
import mysql.connector


class SuppressionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un article")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_codeA = QLabel("Code de l'article à supprimer:")
        self.champ_codeA = QLineEdit()
        layout.addWidget(label_codeA)
        layout.addWidget(self.champ_codeA)

        # Bouton pour supprimer l'article
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_article_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_article_db(self):
        codeA = self.champ_codeA.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'article existe
        check = "SELECT codeA FROM article WHERE codeA = %s"
        cursor.execute(check, (codeA,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'article spécifié n'existe pas dans la table 'article'.")
            return

        # Requête de suppression
        delete = "DELETE FROM article WHERE codeA = %s"
        cursor.execute(delete, (codeA,))
        conn.commit()

        QMessageBox.information(None, "Succès", "L'article a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class InsertionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un article")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_codeA = QLabel("Code de l'article:")
        self.champ_codeA = QLineEdit()
        layout.addWidget(label_codeA)
        layout.addWidget(self.champ_codeA)

        label_nomA = QLabel("Nom de l'article:")
        self.champ_nomA = QLineEdit()
        layout.addWidget(label_nomA)
        layout.addWidget(self.champ_nomA)

        label_descriptionA = QLabel("Description de l'article:")
        self.champ_descriptionA = QLineEdit()
        layout.addWidget(label_descriptionA)
        layout.addWidget(self.champ_descriptionA)

        label_coutA = QLabel("Coût de l'article:")
        self.champ_coutA = QLineEdit()
        layout.addWidget(label_coutA)
        layout.addWidget(self.champ_coutA)

        label_prixV = QLabel("Prix de vente de l'article:")
        self.champ_prixV = QLineEdit()
        layout.addWidget(label_prixV)
        layout.addWidget(self.champ_prixV)

        label_qteA = QLabel("Quantité de l'article:")
        self.champ_qteA = QLineEdit()
        layout.addWidget(label_qteA)
        layout.addWidget(self.champ_qteA)

        label_numEmp = QLabel("Numéro d'emplacement de l'article:")
        self.champ_numEmp = QLineEdit()
        layout.addWidget(label_numEmp)
        layout.addWidget(self.champ_numEmp)

        label_nomF = QLabel("Nom du fournisseur:")
        self.champ_nomF = QLineEdit()
        layout.addWidget(label_nomF)
        layout.addWidget(self.champ_nomF)

        label_nomCat = QLabel("Nom de la catégorie:")
        self.champ_nomCat = QLineEdit()
        layout.addWidget(label_nomCat)
        layout.addWidget(self.champ_nomCat)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_article_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_article_db(self):
        codeA = self.champ_codeA.text()
        nomA = self.champ_nomA.text()
        descriptionA = self.champ_descriptionA.text()
        coutA = self.champ_coutA.text()
        prixV = self.champ_prixV.text()
        qteA = self.champ_qteA.text()
        numEmp = self.champ_numEmp.text()
        nomF = self.champ_nomF.text()
        nomCat = self.champ_nomCat.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'emplacement existe
        check = "SELECT numEmp FROM emplacement WHERE numEmp = %s"
        cursor.execute(check, (numEmp,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'emplacement spécifié n'existe pas dans la table 'emplacement'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO article (codeA, nomA, descriptionA, coutA, qteA, prixV, nomF, nomCat, numEmp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (codeA, nomA, descriptionA, coutA, qteA, prixV, nomF, nomCat, numEmp)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'article a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un article")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de l'article à modifier
        label_codeA = QLabel("Code de l'article à modifier:")
        self.champ_codeA = QLineEdit()
        layout.addWidget(label_codeA)
        layout.addWidget(self.champ_codeA)

        # Bouton pour afficher les informations de l'article
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_article)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'article
        label_nomA = QLabel("Nom de l'article:")
        self.champ_nomA = QLineEdit()
        layout.addWidget(label_nomA)
        layout.addWidget(self.champ_nomA)

        label_descriptionA = QLabel("Description de l'article:")
        self.champ_descriptionA = QLineEdit()
        layout.addWidget(label_descriptionA)
        layout.addWidget(self.champ_descriptionA)

        label_coutA = QLabel("Coût de l'article:")
        self.champ_coutA = QLineEdit()
        layout.addWidget(label_coutA)
        layout.addWidget(self.champ_coutA)

        label_quantite = QLabel("Quantité de l'article:")
        self.champ_quantite = QLineEdit()
        layout.addWidget(label_quantite)
        layout.addWidget(self.champ_quantite)

        label_prix_vente = QLabel("Prix de vente de l'article:")
        self.champ_prix_vente = QLineEdit()
        layout.addWidget(label_prix_vente)
        layout.addWidget(self.champ_prix_vente)

        # Bouton pour modifier l'article
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_article)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_article(self):
        codeA = self.champ_codeA.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'article
        select = "SELECT nomA, descriptionA, coutA, qteA, prixV FROM article WHERE codeA = %s"
        cursor.execute(select, (codeA,))
        result = cursor.fetchone()

        if result:
            nomA, descriptionA, coutA, qteA, prixV = result
            self.champ_nomA.setText(nomA)
            self.champ_descriptionA.setText(descriptionA)
            self.champ_coutA.setText(str(coutA))
            self.champ_quantite.setText(str(qteA))
            self.champ_prix_vente.setText(str(prixV))
        else:
            QMessageBox.warning(self, "Erreur", "L'article spécifié n'existe pas dans la table 'article'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_article(self):
        codeA = self.champ_codeA.text()
        nomA = self.champ_nomA.text()
        descriptionA = self.champ_descriptionA.text()
        coutA = self.champ_coutA.text()
        quantite = self.champ_quantite.text()
        prixVente = self.champ_prix_vente.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'article existe
        check = "SELECT codeA FROM article WHERE codeA = %s"
        cursor.execute(check, (codeA,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'article spécifié n'existe pas dans la table 'article'.")
            return

        # Requête de modification
        update = "UPDATE article SET nomA = %s, descriptionA = %s, coutA = %s, qteA = %s, prixV = %s WHERE codeA = %s"
        data = (nomA, descriptionA, coutA, quantite, prixVente, codeA)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "L'article a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class ListerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des articles")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the articles
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(9)
        self.table_widget.setHorizontalHeaderLabels(["Code", "Nom", "Description", "Coût", "Quantité", "Prix de vente",  "nomF", "nomCat", "numEmp"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the articles
        self.load_articles()

    def load_articles(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the articles
        select = "SELECT codeA, nomA, descriptionA, coutA, qteA, prixV, nomF, nomCat, numEmp FROM article"
        cursor.execute(select)
        articles = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(articles))

        # Populate the table widget with the articles
        for row, article in enumerate(articles):
            for col, value in enumerate(article):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#///////////////////////////////////////////////////////////


class InsertionDialogCat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une categorie")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_nomCat = QLabel("Nom de categorie:")
        self.champ_nomCat = QLineEdit()
        layout.addWidget(label_nomCat)
        layout.addWidget(self.champ_nomCat)

        label_descriptionCat = QLabel("Description de categorie:")
        self.champ_descriptionCat = QLineEdit()
        layout.addWidget(label_descriptionCat)
        layout.addWidget(self.champ_descriptionCat)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_categorie_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_categorie_db(self):
        nomCat = self.champ_nomCat.text()
        descriptionCat = self.champ_descriptionCat.text()
        

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'emplacement existe
        # Requête d'insertion
        insert = "INSERT INTO categorie (nomCat, descriptionCat) VALUES (%s, %s)"
        data = (nomCat,descriptionCat)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "La categorie a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogCat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un categorie")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de la categorie à modifier
        label_nomCat = QLabel("nom de categorie à modifier:")
        self.champ_nomCat = QLineEdit()
        layout.addWidget(label_nomCat)
        layout.addWidget(self.champ_nomCat)

        # Bouton pour afficher les informations de la categorie
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_categorie)
        layout.addWidget(bouton_afficher)

        label_descriptionCat = QLabel("Description de la categorie:")
        self.champ_descriptionCat = QLineEdit()
        layout.addWidget(label_descriptionCat)
        layout.addWidget(self.champ_descriptionCat)

        # Bouton pour modifier la categorie
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_categorie)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_categorie(self):
        nomCat = self.champ_nomCat.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'article
        select = "SELECT nomCat, descriptionCat FROM categorie WHERE nomCat = %s"
        cursor.execute(select, (nomCat,))
        result = cursor.fetchone()

        if result:
            nomCat, descriptionCat = result
            self.champ_nomCat.setText(nomCat)
            self.champ_descriptionCat.setText(descriptionCat)
        else:
            QMessageBox.warning(self, "Erreur", "La categorie spécifié n'existe pas dans la table 'categorie'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_categorie(self):
        nomCat = self.champ_nomCat.text()
        descriptionCat = self.champ_descriptionCat.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la categorie existe
        check = "SELECT nomCat FROM categorie WHERE nomCat = %s"
        cursor.execute(check, (nomCat,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "La categorie spécifié n'existe pas dans la table 'categorie'.")
            return

        # Requête de modification
        update = "UPDATE categorie SET descriptionCat = %s WHERE nomCat = %s"
        data = (descriptionCat,nomCat)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "La categorie a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()



class SuppressionDialogCat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une categorie")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_nomCat = QLabel("nom de la categorie à supprimer:")
        self.champ_nomCat = QLineEdit()
        layout.addWidget(label_nomCat)
        layout.addWidget(self.champ_nomCat)

        # Bouton pour supprimer la categorie
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_categorie_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_categorie_db(self):
        nomCat = self.champ_nomCat.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la categorie existe
        check = "SELECT nomCat FROM categorie WHERE nomCat = %s"
        cursor.execute(check, (nomCat,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "La categorie spécifié n'existe pas dans la table 'categorie'.")
            return

        # Requête de suppression
        delete = "DELETE FROM categorie WHERE nomCat = %s"
        cursor.execute(delete, (nomCat,))
        conn.commit()

        QMessageBox.information(None, "Succès", "La categorie a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()



class ListerDialogCat(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des categories")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the categories
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["NomCat","DescriptionCat"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the categories
        self.load_categories()

    def load_categories(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the categories
        select = "SELECT nomCat, descriptionCat FROM categorie"
        cursor.execute(select)
        categories = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(categories))

        # Populate the table widget with the categories
        for row, categorie in enumerate(categories):
            for col, value in enumerate(categorie):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()


#//////////////////////////////////////////////////////////////////


class InsertionDialogEmp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une emplacement")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numEmp = QLabel("Numero de emplacement:")
        self.champ_numEmp = QLineEdit()
        layout.addWidget(label_numEmp)
        layout.addWidget(self.champ_numEmp)

        label_nomEmp = QLabel("Nom de emplacement:")
        self.champ_nomEmp = QLineEdit()
        layout.addWidget(label_nomEmp)
        layout.addWidget(self.champ_nomEmp)

        label_descriptionEmp = QLabel("Description de emplacement:")
        self.champ_descriptionEmp = QLineEdit()
        layout.addWidget(label_descriptionEmp)
        layout.addWidget(self.champ_descriptionEmp)

        label_capEmp = QLabel("Capacite de emplacement:")
        self.champ_capEmp = QLineEdit()
        layout.addWidget(label_capEmp)
        layout.addWidget(self.champ_capEmp)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_emplacement_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_emplacement_db(self):
        numEmp = self.champ_numEmp.text()
        nomEmp = self.champ_nomEmp.text()
        descriptionEmp = self.champ_descriptionEmp.text()
        capaciteEmp = self.champ_capEmp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'emplacement existe
        # Requête d'insertion
        insert = "INSERT INTO emplacement (numEmp,nomEmp, descriptionEmp , capaciteEmp) VALUES (%s, %s,%s,%s)"
        data = (numEmp,nomEmp, descriptionEmp , capaciteEmp)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'emplacement a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()



class ModificationDialogEmp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier l'emplacement")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de l'emplacement à modifier
        label_numEmp = QLabel("Numero de l'emplacement à modifier:")
        self.champ_numEmp = QLineEdit()
        layout.addWidget(label_numEmp)
        layout.addWidget(self.champ_numEmp)

        # Bouton pour afficher les informations de l'emplacement
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_emplacement)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'emplacement
        label_nomEmp = QLabel("Nom de l'emplacement:")
        self.champ_nomEmp = QLineEdit()
        layout.addWidget(label_nomEmp)
        layout.addWidget(self.champ_nomEmp)

        label_descriptionEmp = QLabel("Description de l'emplacement:")
        self.champ_descriptionEmp = QLineEdit()
        layout.addWidget(label_descriptionEmp)
        layout.addWidget(self.champ_descriptionEmp)

        label_capaciteEmp = QLabel("Capacite de l'emplacement:")
        self.champ_capaciteEmp = QLineEdit()
        layout.addWidget(label_capaciteEmp)
        layout.addWidget(self.champ_capaciteEmp)

        # Bouton pour modifier l'emplacement
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_emplacement)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_emplacement(self):
        numEmp = self.champ_numEmp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'emplacement
        select = "SELECT nomEmp, descriptionEmp, capaciteEmp FROM emplacement WHERE numEmp = %s"
        cursor.execute(select, (numEmp,))
        result = cursor.fetchone()

        if result:
            nomEmp, descriptionEmp, capaciteEmp = result
            self.champ_nomEmp.setText(nomEmp)
            self.champ_descriptionEmp.setText(descriptionEmp)
            self.champ_capaciteEmp.setText(str(capaciteEmp))
        else:
            QMessageBox.warning(self, "Erreur", "L'emplacement spécifié n'existe pas dans la table 'emplacement'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_emplacement(self):
        numEmp = self.champ_numEmp.text()
        nomEmp = self.champ_nomEmp.text()
        descriptionEmp = self.champ_descriptionEmp.text()
        capaciteEmp = self.champ_capaciteEmp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'emplacement existe
        check = "SELECT numEmp FROM emplacement WHERE numEmp = %s"
        cursor.execute(check, (numEmp,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'emplacement spécifié n'existe pas dans la table 'emplacement'.")
            return

        # Requête de modification
        update = "UPDATE emplacement SET nomEmp = %s, descriptionEmp = %s, capaciteEmp = %s WHERE numEmp = %s"
        data = (nomEmp, descriptionEmp, capaciteEmp, numEmp)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "L'emplacement a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class SuppressionDialogEmp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un emplacement")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numEmp = QLabel("Code de l'emplacement à supprimer:")
        self.champ_numEmp = QLineEdit()
        layout.addWidget(label_numEmp)
        layout.addWidget(self.champ_numEmp)

        # Bouton pour supprimer l'emplacement
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_emplacement_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_emplacement_db(self):
        numEmp = self.champ_numEmp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'emplacement existe
        check = "SELECT numEmp FROM emplacement WHERE numEmp = %s"
        cursor.execute(check, (numEmp,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'emplacement spécifié n'existe pas dans la table 'emplacement'.")
            return

        # Requête de suppression
        delete = "DELETE FROM emplacement WHERE numEmp = %s"
        cursor.execute(delete, (numEmp,))
        conn.commit()

        QMessageBox.information(None, "Succès", "L'emplacement a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ListerDialogEmp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des emplacements")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the emplacements
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["NumEmp","NomEmp","DescriptionEmp" , "CapaciteEmp"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the emplacements
        self.load_emplacements()

    def load_emplacements(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the emplacements
        select = "SELECT NumEmp,NomEmp, DescriptionEmp,CapaciteEmp FROM emplacement"
        cursor.execute(select)
        emplacements = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(emplacements))

        # Populate the table widget with the emplacements
        for row, emplacement in enumerate(emplacements):
            for col, value in enumerate(emplacement):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()


#////////////////////////////////////////////////////////////////////////

class InsertionDialogCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un commande")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numCom = QLabel("Numero de la commande:")
        self.champ_numCom = QLineEdit()
        layout.addWidget(label_numCom)
        layout.addWidget(self.champ_numCom)

        label_dateCom = QLabel("Date de la commande (AAAA-MM-JJ):")
        self.champ_dateCom = QLineEdit()
        layout.addWidget(label_dateCom)
        layout.addWidget(self.champ_dateCom)

        label_statut = QLabel("Statut de la commande:")
        self.champ_statut = QLineEdit()
        layout.addWidget(label_statut)
        layout.addWidget(self.champ_statut)


        label_numLiv = QLabel("Numero de la livraison:")
        self.champ_numLiv = QLineEdit()
        layout.addWidget(label_numLiv)
        layout.addWidget(self.champ_numLiv)


        label_nomF = QLabel("Nom du fournisseur:")
        self.champ_nomF = QLineEdit()
        layout.addWidget(label_nomF)
        layout.addWidget(self.champ_nomF)

        label_numCli = QLabel("Numero de Client:")
        self.champ_numCli = QLineEdit()
        layout.addWidget(label_numCli)
        layout.addWidget(self.champ_numCli)

        # Bouton pour insérer la commande
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_commande_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_commande_db(self):
        numCom = self.champ_numCom.text()
        dateCom = self.champ_dateCom.text()
        statut = self.champ_statut.text()
        numLiv = self.champ_numLiv.text()
        nomF = self.champ_nomF.text()
        numCli = self.champ_numCli.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête d'insertion
        insert = "INSERT INTO commande (numCom, dateCom, statut, numLiv, nomF, numCli) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (numCom, dateCom, statut, numLiv, nomF, numCli)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "La commande a été insérée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class ModificationDialogCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier une commande")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de la commande à modifier
        label_numCom = QLabel("Code de la commande à modifier:")
        self.champ_numCom = QLineEdit()
        layout.addWidget(label_numCom)
        layout.addWidget(self.champ_numCom)

        # Bouton pour afficher les informations de la commande
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_commande)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de la commande
        label_dateCom = QLabel("Date de la commande:")
        self.champ_dateCom = QLineEdit()
        layout.addWidget(label_dateCom)
        layout.addWidget(self.champ_dateCom)

        label_statut = QLabel("Statut de la commande:")
        self.champ_statut = QLineEdit()
        layout.addWidget(label_statut)
        layout.addWidget(self.champ_statut)

        # Bouton pour modifier la commande
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_commande)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_commande(self):
        numCom = self.champ_numCom.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de la commande
        select = "SELECT dateCom, statut FROM commande WHERE numCom = %s"
        cursor.execute(select, (numCom,))
        result = cursor.fetchone()

        if result:
            dateCom, statut = result
            self.champ_dateCom.setText(str(dateCom))
            self.champ_statut.setText(statut)
        else:
            QMessageBox.warning(None, "Erreur", "La commande spécifiée n'existe pas dans la table 'commande'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_commande(self):
        numCom = self.champ_numCom.text()
        dateCom = self.champ_dateCom.text()
        statut = self.champ_statut.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la commande existe
        check = "SELECT numCom FROM commande WHERE numCom = %s"
        cursor.execute(check, (numCom,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "La commande spécifiée n'existe pas dans la table 'commande'.")
            return

        # Requête de modification
        update = "UPDATE commande SET dateCom = %s, statut = %s WHERE numCom = %s"
        data = (dateCom, statut, numCom)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "La commande a été modifiée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class SuppressionDialogCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une commande")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numCom = QLabel("Numero de la commande à supprimer:")
        self.champ_numCom = QLineEdit()
        layout.addWidget(label_numCom)
        layout.addWidget(self.champ_numCom)

        # Bouton pour supprimer la commande
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_commande_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_commande_db(self):
        numCom = self.champ_numCom.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la commande existe
        check = "SELECT numCom FROM commande WHERE numCom = %s"
        cursor.execute(check, (numCom,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "La commande spécifié n'existe pas dans la table 'commande'.")
            return

        # Requête de suppression
        delete = "DELETE FROM commande WHERE numCom = %s"
        cursor.execute(delete, (numCom,))
        conn.commit()

        QMessageBox.information(None, "Succès", "La commade a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ListerDialogCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des commandes")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the commandes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["NumCom", "dateCom", "statut", "numLiv", "nomF", "numCli"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the commandes
        self.load_commandes()

    def load_commandes(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the commandes
        select = "SELECT numCom, dateCom, statut, numLiv, nomF, numCli FROM commande"
        cursor.execute(select)
        commandes = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(commandes))

        # Populate the table widget with the commandes
        for row, commande in enumerate(commandes):
            for col, value in enumerate(commande):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()


#//////////////////////////////////////////////////////

class InsertionDialogDetCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un détail commande")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_ndc = QLabel("NDC du détail :")
        self.champ_ndc = QLineEdit()
        layout.addWidget(label_ndc)
        layout.addWidget(self.champ_ndc)

        label_qteCom = QLabel("Quantité :")
        self.champ_qteCom = QLineEdit()
        layout.addWidget(label_qteCom)
        layout.addWidget(self.champ_qteCom)

        label_coutU = QLabel("Coût :")
        self.champ_coutU = QLineEdit()
        layout.addWidget(label_coutU)
        layout.addWidget(self.champ_coutU)

        label_prixU = QLabel("Prix unitaire :")
        self.champ_prixU = QLineEdit()
        layout.addWidget(label_prixU)
        layout.addWidget(self.champ_prixU)

        # Bouton pour insérer le détail commande
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_detailCom_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_detailCom_db(self):
        ndc = self.champ_ndc.text()
        qteCom = self.champ_qteCom.text()
        coutU = self.champ_coutU.text()
        prixU = self.champ_prixU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête d'insertion
        insert = "INSERT INTO detalCom (NDC, qteCom, coutU, prixU) VALUES (%s, %s, %s, %s)"
        data = (ndc, qteCom, coutU, prixU)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "Le détail commande a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogDetCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un détail commande")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le NDC du détail à modifier
        label_ndc = QLabel("NDC du détail à modifier:")
        self.champ_ndc = QLineEdit()
        layout.addWidget(label_ndc)
        layout.addWidget(self.champ_ndc)

        # Bouton pour afficher les informations du détail
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_detailCom)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs du détail
        label_qteCom = QLabel("Quantité du détail :")
        self.champ_qteCom = QLineEdit()
        layout.addWidget(label_qteCom)
        layout.addWidget(self.champ_qteCom)

        label_coutU = QLabel("Coût du détail :")
        self.champ_coutU = QLineEdit()
        layout.addWidget(label_coutU)
        layout.addWidget(self.champ_coutU)

        label_prixU = QLabel("Prix unitaire du détail :")
        self.champ_prixU = QLineEdit()
        layout.addWidget(label_prixU)
        layout.addWidget(self.champ_prixU)

        # Bouton pour modifier le détail
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_detailCom)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_detailCom(self):
        NDC = self.champ_ndc.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations du détail
        select = "SELECT NDC, qteCom, coutU, prixU FROM detalCom WHERE NDC = %s"
        cursor.execute(select, (NDC,))
        result = cursor.fetchone()

        if result:
            NDC, qteCom, coutU, prixU = result
            self.champ_qteCom.setText(str(qteCom))
            self.champ_coutU.setText(str(coutU))
            self.champ_prixU.setText(str(prixU))
        else:
            QMessageBox.warning(self, "Erreur", "Le détail spécifié n'existe pas dans la table 'detalCom'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_detailCom(self):
        NDC = self.champ_ndc.text()
        qteCom = self.champ_qteCom.text()
        coutU = self.champ_coutU.text()
        prixU = self.champ_prixU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le détail existe
        check = "SELECT NDC FROM detalCom WHERE NDC = %s"
        cursor.execute(check, (NDC,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "Le détail spécifié n'existe pas dans la table 'detalCom'.")
            return

        # Requête de modification
        update = "UPDATE detalCom SET qteCom = %s, coutU = %s, prixU = %s WHERE NDC = %s"
        data = (qteCom, coutU, prixU, NDC)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le détail a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class SuppressionDialogDetCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un detailCom")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_ndc = QLabel("NDC  de detailCom à supprimer:")
        self.champ_ndc = QLineEdit()
        layout.addWidget(label_ndc)
        layout.addWidget(self.champ_ndc)

        # Bouton pour supprimer l'article
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_detailCom_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_detailCom_db(self):
        NDC = self.champ_ndc.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si detailCom existe
        check = "SELECT NDC FROM detalCom WHERE NDC = %s"
        cursor.execute(check, (NDC,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "detailCom spécifié n'existe pas dans la table 'detalCom'.")
            return

        # Requête de suppression
        delete = "DELETE FROM detalCom WHERE NDC = %s"
        cursor.execute(delete, (NDC,))
        conn.commit()

        QMessageBox.information(None, "Succès", "deatilCom a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ListerDialogDetCom(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des details commandes")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the details commandes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["NDC", "qteCom",  "CoûtU", "PrixU"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the details commandes
        self.load_detailcoms()

    def load_detailcoms(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the detailcoms
        select = "SELECT NDC, qteCom, coutU,prixU FROM detalCom"
        cursor.execute(select)
        detailcoms = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(detailcoms))

        # Populate the table widget with the detailcoms
        for row, detailcom in enumerate(detailcoms):
            for col, value in enumerate(detailcom):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////////
class InsertionDialogFou(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un fournisseur")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        label_nomF = QLabel("Nom du fournisseur:")
        self.champ_nomF = QLineEdit()
        layout.addWidget(label_nomF)
        layout.addWidget(self.champ_nomF)

        label_adresseF = QLabel("Adresse du fournisseur:")
        self.champ_adresseF  = QLineEdit()
        layout.addWidget(label_adresseF)
        layout.addWidget(self.champ_adresseF)

        label_teleF = QLabel("Téléphone du fournisseur:")
        self.champ_teleF = QLineEdit()
        layout.addWidget(label_teleF)
        layout.addWidget(self.champ_teleF)

        label_faxF = QLabel("Fax du fournisseur:")
        self.champ_faxF = QLineEdit()
        layout.addWidget(label_faxF)
        layout.addWidget(self.champ_faxF)

        label_courrielF = QLabel("Courriel du fournisseur:")
        self.champ_courrielF = QLineEdit()
        layout.addWidget(label_courrielF)
        layout.addWidget(self.champ_courrielF)

        label_contact = QLabel("Contact du fournisseur:")
        self.champ_contact = QLineEdit()
        layout.addWidget(label_contact)
        layout.addWidget(self.champ_contact)

        # Bouton pour insérer le fournisseur
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_fournisseur_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_fournisseur_db(self):
        nomF = self.champ_nomF.text()
        adresseF = self.champ_adresseF.text()
        teleF = self.champ_teleF.text()
        faxF = self.champ_faxF.text()
        courrielF = self.champ_courrielF.text()
        contact = self.champ_contact.text() 

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le fournisseur existe déjà
        select = "SELECT nomF FROM fournisseur WHERE nomF = %s"
        cursor.execute(select, (nomF,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "Le fournisseur spécifié existe déjà dans la table 'fournisseur'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO fournisseur (nomF, adresseF, teleF, faxF, courrielF, contact) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (nomF, adresseF, teleF, faxF, courrielF, contact)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "Le fournisseur a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogFou(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un fournisseur")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        label_nomF = QLabel("Nom du fournisseur à modifier:")
        self.champ_nomF = QLineEdit()
        layout.addWidget(label_nomF)
        layout.addWidget(self.champ_nomF)

        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_fournisseur)
        layout.addWidget(bouton_afficher)

        label_adresseF = QLabel("Adresse du fournisseur:")
        self.champ_adresseF = QLineEdit()
        layout.addWidget(label_adresseF)
        layout.addWidget(self.champ_adresseF)

        label_teleF = QLabel("Téléphone du fournisseur:")
        self.champ_teleF = QLineEdit()
        layout.addWidget(label_teleF)
        layout.addWidget(self.champ_teleF)

        label_faxF = QLabel("Fax du fournisseur:")
        self.champ_faxF = QLineEdit()
        layout.addWidget(label_faxF)
        layout.addWidget(self.champ_faxF)

        label_courrielF = QLabel("Courriel du fournisseur:")
        self.champ_courrielF = QLineEdit()
        layout.addWidget(label_courrielF)
        layout.addWidget(self.champ_courrielF)

        label_contact = QLabel("Contact du fournisseur:")
        self.champ_contact = QLineEdit()
        layout.addWidget(label_contact)
        layout.addWidget(self.champ_contact)

        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_fournisseur)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_fournisseur(self):
        nomF = self.champ_nomF.text()

        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        select = "SELECT nomF, adresseF, teleF, faxF, courrielF, contact FROM fournisseur WHERE nomF = %s"
        cursor.execute(select, (nomF,))
        result = cursor.fetchone()

        if result:
            nomF, adresseF, teleF, faxF, courrielF, contact = result
            self.champ_adresseF.setText(str(adresseF))
            self.champ_teleF.setText(str(teleF))
            self.champ_faxF.setText(str(faxF))
            self.champ_courrielF.setText(str(courrielF))
            self.champ_contact.setText(str(contact))
        else:
            QMessageBox.warning(self, "Erreur", "Le fournisseur spécifié n'existe pas dans la table 'fournisseur'.")

        cursor.close()
        conn.close()

    def modifier_fournisseur(self):
        nomF = self.champ_nomF.text()
        adresseF = self.champ_adresseF.text()
        teleF = self.champ_teleF.text()
        faxF = self.champ_faxF.text()
        courrielF = self.champ_courrielF.text()
        contact = self.champ_contact.text()

        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        check = "SELECT nomF FROM fournisseur WHERE nomF = %s"
        cursor.execute(check, (nomF,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "Le fournisseur spécifié n'existe pas dans la table 'fournisseur'.")
            return

        update = "UPDATE fournisseur SET adresseF = %s, teleF = %s, faxF = %s, courrielF = %s, contact = %s WHERE nomF = %s"
        data = (adresseF, teleF, faxF, courrielF, contact, nomF)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le fournisseur a été modifié avec succès!")

        cursor.close()
        conn.close()

        self.accept()

class SuppressionDialogFou(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un fournisseur")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_nomF = QLabel("Nom du fournisseur à supprimer:")
        self.champ_nomF = QLineEdit()
        layout.addWidget(label_nomF)
        layout.addWidget(self.champ_nomF)

        # Bouton pour supprimer le fournisseur
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_fournisseur_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_fournisseur_db(self):
        nomF = self.champ_nomF.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le fournisseur existe
        check = "SELECT nomF FROM fournisseur WHERE nomF = %s"
        cursor.execute(check, (nomF,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "Le fournisseur spécifié n'existe pas dans la table 'fournisseur'.")
            return

        # Requête de suppression
        delete = "DELETE FROM fournisseur WHERE nomF = %s"
        cursor.execute(delete, (nomF,))
        conn.commit()

        QMessageBox.information(None, "Succès", "Le fournisseur a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ListerDialogFou(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des fournisseurs")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the suppliers
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["NomF", "AdresseF", "TeleF", "FaxF", "CourrielF", "Contact"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the suppliers
        self.load_fournisseurs()

    def load_fournisseurs(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the suppliers
        select = "SELECT nomF, adresseF, teleF, faxF, courrielF, contact FROM fournisseur"
        cursor.execute(select)
        fournisseurs = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(fournisseurs))

        # Populate the table widget with the suppliers
        for row, fournisseur in enumerate(fournisseurs):
            for col, value in enumerate(fournisseur):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogUtile(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un utilisateur")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_nomU = QLabel("Nom de l'utilisateur:")
        self.champ_nomU = QLineEdit()
        layout.addWidget(label_nomU)
        layout.addWidget(self.champ_nomU)

        label_courrielU = QLabel("Courriel de l'utilisateur:")
        self.champ_courrielU = QLineEdit()
        layout.addWidget(label_courrielU)
        layout.addWidget(self.champ_courrielU)

        label_mdp = QLabel("Mot De Passe de l'utilisateur:")
        self.champ_mdp = QLineEdit()
        layout.addWidget(label_mdp)
        layout.addWidget(self.champ_mdp)

        label_admin = QLabel("Admin:")
        self.champ_admin = QLineEdit()
        layout.addWidget(label_admin)
        layout.addWidget(self.champ_admin)

        label_nomSys = QLabel("Nom du système:")
        self.champ_nomSys = QLineEdit()
        layout.addWidget(label_nomSys)
        layout.addWidget(self.champ_nomSys)

        # Bouton pour insérer l'utilisateur
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_utilisateur_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_utilisateur_db(self):
        nomU = self.champ_nomU.text()
        courrielU = self.champ_courrielU.text()
        mdp = self.champ_mdp.text()
        admin = self.champ_admin.text()
        nomSys = self.champ_nomSys.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'utilisateur existe
        check = "SELECT nomU FROM utilisateur WHERE nomU = %s"
        cursor.execute(check, (nomU,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'utilisateur spécifié existe déjà dans la table 'utilisateur'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO utilisateur (nomU, courrielU, mdp, admin, nomSys) VALUES (%s, %s, %s, %s, %s)"
        data = (nomU, courrielU, mdp, admin, nomSys)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'utilisateur a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class SuppressionDialogUtile(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un utilisateur")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_nomU = QLabel("Nom de l'utilisateur à supprimer:")
        self.champ_nomU = QLineEdit()
        layout.addWidget(label_nomU)
        layout.addWidget(self.champ_nomU)

        # Bouton pour supprimer l'utilisateur
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_utilisateur_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_utilisateur_db(self):
        nomU = self.champ_nomU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'utilisateur existe
        check = "SELECT nomU FROM utilisateur WHERE nomU = %s"
        cursor.execute(check, (nomU,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'utilisateur spécifié n'existe pas dans la table 'utilisateur'.")
            return

        # Requête de suppression
        delete = "DELETE FROM utilisateur WHERE nomU = %s"
        cursor.execute(delete, (nomU,))
        conn.commit()

        QMessageBox.information(None, "Succès", "L'utilisateur a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogUtile(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un utilisateur")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le nom de l'utilisateur à modifier
        label_nomU = QLabel("Nom de l'utilisateur à modifier:")
        self.champ_nomU = QLineEdit()
        layout.addWidget(label_nomU)
        layout.addWidget(self.champ_nomU)

        # Bouton pour afficher les informations de l'utilisateur
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_utilisateur)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'utilisateur
        label_courrielU = QLabel("Courriel de l'utilisateur:")
        self.champ_courrielU = QLineEdit()
        layout.addWidget(label_courrielU)
        layout.addWidget(self.champ_courrielU)

        label_mdp = QLabel("Mot de passe de l'utilisateur:")
        self.champ_mdp = QLineEdit()
        layout.addWidget(label_mdp)
        layout.addWidget(self.champ_mdp)

        # Bouton pour modifier l'utilisateur
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_utilisateur)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_utilisateur(self):
        nomU = self.champ_nomU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'utilisateur
        select = "SELECT nomU, courrielU, mdp FROM utilisateur WHERE nomU = %s"
        cursor.execute(select, (nomU,))
        result = cursor.fetchone()

        if result:
            nomU, courrielU, mdp = result
            self.champ_nomU.setText(nomU)
            self.champ_courrielU.setText(courrielU)
            self.champ_mdp.setText(mdp)
        else:
            QMessageBox.warning(self, "Erreur", "L'utilisateur spécifié n'existe pas dans la table 'utilisateur'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_utilisateur(self):
        nomU = self.champ_nomU.text()
        courrielU = self.champ_courrielU.text()
        mdp = self.champ_mdp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'utilisateur existe
        check = "SELECT nomU FROM utilisateur WHERE nomU = %s"
        cursor.execute(check, (nomU,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'utilisateur spécifié n'existe pas dans la table 'utilisateur'.")
            return

        # Requête de modification
        update = "UPDATE utilisateur SET courrielU = %s, mdp = %s WHERE nomU = %s"
        data = (courrielU, mdp, nomU)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "L'utilisateur a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class ListerDialogUtile(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des utilisateurs")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the utilisateurs
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["nomU", "courrielU", "mdp", "admin", "nomsys"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the utilisateurs
        self.load_utilisateurs()

    def load_utilisateurs(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the utilisateurs
        select = "SELECT nomU, courrielU, mdp, admin, nomsys FROM utilisateur"
        cursor.execute(select)
        utilisateurs = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(utilisateurs))

        # Populate the table widget with the utilisateurs
        for row, utilisateur in enumerate(utilisateurs):
            for col, value in enumerate(utilisateur):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogRole(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un rôle")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_admin = QLabel("Admin:")
        self.champ_admin = QLineEdit()
        layout.addWidget(label_admin)
        layout.addWidget(self.champ_admin)

        label_type = QLabel("Type:")
        self.champ_type = QLineEdit()
        layout.addWidget(label_type)
        layout.addWidget(self.champ_type)

        # Bouton pour insérer le rôle
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_role_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_role_db(self):
        admin = self.champ_admin.text()
        role_type = self.champ_type.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'admin existe
        select = "SELECT admin FROM role WHERE admin = %s"
        cursor.execute(select, (admin,))
        result = cursor.fetchone()
        if result:
            QMessageBox.warning(self, "Erreur", "L'admin spécifié existe déjà dans la table 'role'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO role (admin, type) VALUES (%s, %s)"
        data = (admin, role_type)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le rôle a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogRole(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier le rôle")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code du rôle à modifier
        label_admin = QLabel("Admin à modifier:")
        self.champ_admin = QLineEdit()
        layout.addWidget(label_admin)
        layout.addWidget(self.champ_admin)

        # Bouton pour afficher les informations du rôle
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_role)
        layout.addWidget(bouton_afficher)

        label_type = QLabel("Type du rôle:")
        self.champ_type = QLineEdit()
        layout.addWidget(label_type)
        layout.addWidget(self.champ_type)

        # Bouton pour modifier le rôle
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_role)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_role(self):
        admin = self.champ_admin.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations du rôle
        select = "SELECT admin, type FROM role WHERE admin = %s"
        cursor.execute(select, (admin,))
        result = cursor.fetchone()

        if result:
            admin, role_type = result
            self.champ_admin.setText(admin)
            self.champ_type.setText(role_type)
        else:
            QMessageBox.warning(self, "Erreur", "Le rôle spécifié n'existe pas dans la table 'Role'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_role(self):
        admin = self.champ_admin.text()
        role_type = self.champ_type.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour mettre à jour le rôle
        update = "UPDATE role SET type = %s WHERE admin = %s"
        cursor.execute(update, (role_type, admin))
        conn.commit()

        QMessageBox.information(self, "Succès", "Le rôle a été modifié avec succès.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

class SuppressionDialogRole(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un Rôle")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_admin = QLabel("L'admin à supprimer:")
        self.champ_admin = QLineEdit()
        layout.addWidget(label_admin)
        layout.addWidget(self.champ_admin)

        # Bouton pour supprimer le rôle
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_role_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_role_db(self):
        admin = self.champ_admin.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le rôle existe
        check = "SELECT admin FROM role WHERE admin = %s"
        cursor.execute(check, (admin,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "Le rôle spécifié n'existe pas dans la table 'role'.")
            return

        # Requête de suppression
        delete = "DELETE FROM role WHERE admin = %s"
        cursor.execute(delete, (admin,))
        conn.commit()

        QMessageBox.information(None, "Succès", "Le rôle a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ListerDialogRole(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des Rôles")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the roles
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["admin", "type"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the roles
        self.load_roles()

    def load_roles(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the roles
        select = "SELECT admin, type FROM role"
        cursor.execute(select)
        roles = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(roles))

        # Populate the table widget with the roles
        for row, role in enumerate(roles):
            for col, value in enumerate(role):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogHis(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un Historique")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_dateH = QLabel("DateH de l'historique:")
        self.champ_dateH = QLineEdit()
        layout.addWidget(label_dateH)
        layout.addWidget(self.champ_dateH)

        label_qte = QLabel("Quantité:")
        self.champ_qte = QLineEdit()
        layout.addWidget(label_qte)
        layout.addWidget(self.champ_qte)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_historique_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_historique_db(self):
        dateH = self.champ_dateH.text()
        qte = self.champ_qte.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'historique existe

        # Requête d'insertion
        insert = "INSERT INTO historique (dateH, qte) VALUES (%s, %s)"
        data = (dateH, qte)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'historique a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogHis(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier l'historique")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour la date de l'historique à modifier
        label_dateH = QLabel("dateH à modifier:")
        self.champ_dateH = QLineEdit()
        layout.addWidget(label_dateH)
        layout.addWidget(self.champ_dateH)

        # Bouton pour afficher les informations de l'historique
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_historique)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'historique
        label_qte = QLabel("Quantité:")
        self.champ_qte = QLineEdit()
        layout.addWidget(label_qte)
        layout.addWidget(self.champ_qte)

        # Bouton pour modifier l'historique
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_historique)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_historique(self):
        dateH = self.champ_dateH.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'historique
        select = "SELECT dateH, qte FROM historique WHERE dateH = %s"
        cursor.execute(select, (dateH,))
        result = cursor.fetchone()

        if result:
            dateH, qte = result
            self.champ_qte.setText(str(qte))
        else:
            QMessageBox.warning(self, "Erreur", "L'historique spécifié n'existe pas dans la table 'historique'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_historique(self):
        dateH = self.champ_dateH.text()
        qte = self.champ_qte.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'historique existe
        check = "SELECT dateH FROM historique WHERE dateH = %s"
        cursor.execute(check, (dateH,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'historique spécifié n'existe pas dans la table 'historique'.")
            return

        # Requête de modification
        update = "UPDATE historique SET qte = %s WHERE dateH = %s"
        data = (qte, dateH)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "L'historique a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class SuppressionDialogHis(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un historique")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie pour la date de l'historique à supprimer
        label_dateH = QLabel("dateH à supprimer:")
        self.champ_dateH = QLineEdit()
        layout.addWidget(label_dateH)
        layout.addWidget(self.champ_dateH)

        # Bouton pour supprimer l'historique
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_historique_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_historique_db(self):
        dateH = self.champ_dateH.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'historique existe
        check = "SELECT dateH FROM historique WHERE dateH = %s"
        cursor.execute(check, (dateH,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'historique spécifié n'existe pas dans la table 'historique'.")
            return

        # Requête de suppression
        delete = "DELETE FROM historique WHERE dateH = %s"
        cursor.execute(delete, (dateH,))
        conn.commit()

        QMessageBox.information(None, "Succès", "L'historique a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ListerDialogHis(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des emplacements")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the emplacements
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["dateH", "qte"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the emplacements
        self.load_historiques()

    def load_historiques(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the emplacements
        select = "SELECT dateH, qte FROM historique"
        cursor.execute(select)
        historiques = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(historiques))

        # Populate the table widget with the emplacements
        for row, historique in enumerate(historiques):
            for col, value in enumerate(historique):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()
#//////////////////////////////////////////////////
class InsertionDialogAl(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une Alerte")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_seuilAl = QLabel("Seuil Al de l'alerte:")
        self.champ_seuilAl = QLineEdit()
        layout.addWidget(label_seuilAl)
        layout.addWidget(self.champ_seuilAl)

        label_dateAl = QLabel("Date Al de l'alerte:")
        self.champ_dateAl = QLineEdit()
        layout.addWidget(label_dateAl)
        layout.addWidget(self.champ_dateAl)

        label_qte = QLabel("Quantité:")
        self.champ_qte = QLineEdit()
        layout.addWidget(label_qte)
        layout.addWidget(self.champ_qte)

        # Bouton pour insérer l'alerte
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_alerte_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_alerte_db(self):
        seuilAl = self.champ_seuilAl.text()
        dateAl = self.champ_dateAl.text()
        qte = self.champ_qte.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'alerte existe

        # Requête d'insertion
        insert = "INSERT INTO alerte (seuilAl, dateAl, qte) VALUES (%s, %s, %s)"
        data = (seuilAl, dateAl, qte)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'alerte a été insérée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogAl(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier une Alerte")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le seuilAl de l'alerte à modifier
        label_seuilAl = QLabel("SeuilAl à modifier:")
        self.champ_seuilAl = QLineEdit()
        layout.addWidget(label_seuilAl)
        layout.addWidget(self.champ_seuilAl)

        # Bouton pour afficher les informations de l'alerte
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_alerte)
        layout.addWidget(bouton_afficher)

        label_dateAl = QLabel("DateAl de l'alerte:")
        self.champ_dateAl = QLineEdit()
        layout.addWidget(label_dateAl)
        layout.addWidget(self.champ_dateAl)

        label_qte = QLabel("Quantité:")
        self.champ_qte = QLineEdit()
        layout.addWidget(label_qte)
        layout.addWidget(self.champ_qte)

        # Bouton pour modifier l'alerte
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_alerte)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_alerte(self):
        seuilAl = self.champ_seuilAl.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'alerte
        select = "SELECT seuilAl, dateAl, qte FROM alerte WHERE seuilAl = %s"
        cursor.execute(select, (seuilAl,))
        result = cursor.fetchone()

        if result:
            seuilAl, dateAl, qte = result
            self.champ_seuilAl.setText(seuilAl)
            self.champ_dateAl.setText(str(dateAl))
            self.champ_qte.setText(str(qte))
        else:
            QMessageBox.warning(self, "Erreur", "L'alerte spécifiée n'existe pas dans la table 'alerte'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_alerte(self):
        seuilAl = self.champ_seuilAl.text()
        dateAl = self.champ_dateAl.text()
        qte = self.champ_qte.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour mettre à jour l'alerte
        update = "UPDATE alerte SET dateAl = %s, qte = %s WHERE seuilAl = %s"
        cursor.execute(update, (dateAl, qte, seuilAl))
        conn.commit()

        QMessageBox.information(self, "Succès", "L'alerte a été modifiée avec succès.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


class SuppressionDialogAl(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une Alerte")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le seuilAl de l'alerte à supprimer
        label_seuilAl = QLabel("SeuilAl à supprimer:")
        self.champ_seuilAl = QLineEdit()
        layout.addWidget(label_seuilAl)
        layout.addWidget(self.champ_seuilAl)

        # Bouton pour supprimer l'alerte
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_alerte_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_alerte_db(self):
        seuilAl = self.champ_seuilAl.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'alerte existe
        check = "SELECT seuilAl FROM alerte WHERE seuilAl = %s"
        cursor.execute(check, (seuilAl,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'alerte spécifiée n'existe pas dans la table 'alerte'.")
            return

        # Requête de suppression
        delete = "DELETE FROM alerte WHERE seuilAl = %s"
        cursor.execute(delete, (seuilAl,))
        conn.commit()

        QMessageBox.information(self, "Succès", "L'alerte a été supprimée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ListerDialogAl(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des alertes")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the emplacements
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["seuilAl","dateAl", "qte"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the alertes
        self.load_historiques()

    def load_historiques(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the emplacements
        select = "SELECT seuilAl ,dateAl, qte FROM alerte"
        cursor.execute(select)
        alertes = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(alertes))

        # Populate the table widget with the emplacements
        for row, alerte in enumerate(alertes):
            for col, value in enumerate(alerte):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogPs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un Paramètre de Stock")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout(self)

        # Labels and input fields
        label_seuilCom = QLabel("Seuil Com:")
        self.champ_seuilCom = QLineEdit()
        layout.addWidget(label_seuilCom)
        layout.addWidget(self.champ_seuilCom)

        label_taux = QLabel("Taux:")
        self.champ_taux = QLineEdit()
        layout.addWidget(label_taux)
        layout.addWidget(self.champ_taux)

        # Button to insert the data
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_parametre_stock)
        layout.addWidget(bouton_insere)

    def insere_parametre_stock(self):
        seuilCom = self.champ_seuilCom.text()
        taux = self.champ_taux.text()

        # Database connection
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Check if the parametre_stock exists

        # Insertion query
        insert = "INSERT INTO parametre_stock (seuilCom, taux) VALUES (%s, %s)"
        data = (seuilCom, taux)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le paramètre de stock a été inséré avec succès!")

        # Close the connection
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogPs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un Paramètre de Stock")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label and input field for the seuilCom of the parametre_stock to modify
        label_seuilCom = QLabel("SeuilCom à modifier:")
        self.champ_seuilCom = QLineEdit()
        layout.addWidget(label_seuilCom)
        layout.addWidget(self.champ_seuilCom)

        # Button to display the information of the parametre_stock
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_parametre_stock)
        layout.addWidget(bouton_afficher)

        label_taux = QLabel("Taux:")
        self.champ_taux = QLineEdit()
        layout.addWidget(label_taux)
        layout.addWidget(self.champ_taux)

        # Button to modify the parametre_stock
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_parametre_stock)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_parametre_stock(self):
        seuilCom = self.champ_seuilCom.text()

        # Database connection
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the information of the parametre_stock
        select = "SELECT seuilCom, taux FROM parametre_stock WHERE seuilCom = %s"
        cursor.execute(select, (seuilCom,))
        result = cursor.fetchone()

        if result:
            seuilCom, taux = result
            self.champ_seuilCom.setText(seuilCom)
            self.champ_taux.setText(str(taux))
        else:
            QMessageBox.warning(self, "Erreur", "Le paramètre de stock spécifié n'existe pas dans la table 'parametre_stock'.")

        # Close the connection
        cursor.close()
        conn.close()

    def modifier_parametre_stock(self):
        seuilCom = self.champ_seuilCom.text()
        taux = self.champ_taux.text()

        # Database connection
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to update the parametre_stock
        update = "UPDATE parametre_stock SET taux = %s WHERE seuilCom = %s"
        cursor.execute(update, (taux, seuilCom))
        conn.commit()

        QMessageBox.information(self, "Succès", "Le paramètre de stock a été modifié avec succès.")

        # Close the connection
        cursor.close()
        conn.close()
        self.accept()

class SuppressionDialogPs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un Paramètre de Stock")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label and input field for the seuilCom of the parametre_stock to delete
        label_seuilCom = QLabel("SeuilCom à supprimer:")
        self.champ_seuilCom = QLineEdit()
        layout.addWidget(label_seuilCom)
        layout.addWidget(self.champ_seuilCom)

        # Button to delete the parametre_stock
        bouton_supprimer = QPushButton("Supprimer")
        bouton_supprimer.clicked.connect(self.supprimer_parametre_stock_db)
        layout.addWidget(bouton_supprimer)

        self.setLayout(layout)

    def supprimer_parametre_stock_db(self):
        seuilCom = self.champ_seuilCom.text()

        # Database connection
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Check if the parametre_stock exists
        check = "SELECT seuilCom FROM parametre_stock WHERE seuilCom = %s"
        cursor.execute(check, (seuilCom,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "Le paramètre de stock spécifié n'existe pas dans la table 'parametre_stock'.")
            return

        # Deletion query
        delete = "DELETE FROM parametre_stock WHERE seuilCom = %s"
        cursor.execute(delete, (seuilCom,))
        conn.commit()

        QMessageBox.information(self, "Succès", "Le paramètre de stock a été supprimé avec succès!")

        # Close the connection
        cursor.close()
        conn.close()
        self.accept()

class ListerDialogPs(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des paramètres de stock")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the parametre_stock
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["seuilCom","taux"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the parametre_stock
        self.load_parametre_stock()

    def load_parametre_stock(self):
        # Database connection
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the parametre_stock
        select = "SELECT seuilCom, taux FROM parametre_stock"
        cursor.execute(select)
        parametre_stock = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(parametre_stock))

        # Populate the table widget with the parametre_stock
        for row, parametre in enumerate(parametre_stock):
            for col, value in enumerate(parametre):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()
#//////////////////////////////////////////////////
class InsertionDialogLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une Livraison")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numLiv = QLabel("numero d'une livraison:")
        self.champ_numLiv = QLineEdit()
        layout.addWidget(label_numLiv)
        layout.addWidget(self.champ_numLiv)

        label_dateLiv = QLabel("Date de la livraison:")
        self.champ_dateLiv = QLineEdit()
        layout.addWidget(label_dateLiv)
        layout.addWidget(self.champ_dateLiv)

        label_numT = QLabel("Numero Transporteur:")
        self.champ_numT = QLineEdit()
        layout.addWidget(label_numT)
        layout.addWidget(self.champ_numT)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_livraison_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_livraison_db(self):
        numLiv = self.champ_numLiv.text()
        dateLiv = self.champ_dateLiv.text()
        numT = self.champ_numT.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête d'insertion
        insert = "INSERT INTO livraison (numLiv, dateLiv, numT) VALUES (%s, %s, %s)"
        data = (numLiv, dateLiv, numT)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "La livraison a été insérée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class SuppressionDialogLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une livraison")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numLiv = QLabel("Numero de livraison à supprimer:")
        self.champ_numLiv = QLineEdit()
        layout.addWidget(label_numLiv)
        layout.addWidget(self.champ_numLiv)

        # Bouton pour supprimer l'article
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_livraison_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_livraison_db(self):
        numLiv = self.champ_numLiv.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête de suppression
        delete = "DELETE FROM livraison WHERE numLiv = %s"
        cursor.execute(delete, (numLiv,))
        conn.commit()

        # Vérifier si la livraison a été supprimée
        if cursor.rowcount > 0:
            QMessageBox.information(None, "Succès", "La livraison a été supprimée avec succès!")
        else:
            QMessageBox.warning(None, "Erreur", "La livraison spécifiée n'existe pas dans la table 'livraison'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier une livraison")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de l'article à modifier
        label_numLiv = QLabel("num de livraison à modifier:")
        self.champ_numLiv = QLineEdit()
        layout.addWidget(label_numLiv)
        layout.addWidget(self.champ_numLiv)

        # Bouton pour afficher les informations de l'article
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_livraison)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'article
        label_dateLiv = QLabel("date de la livraison :")
        self.champ_dateLiv = QLineEdit()
        layout.addWidget(label_dateLiv)
        layout.addWidget(self.champ_dateLiv)


        # Bouton pour modifier l'article
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_livraison)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_livraison(self):
        numLiv = self.champ_numLiv.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'article
        select = "SELECT numLiv, dateLiv FROM livraison WHERE numLiv = %s"
        cursor.execute(select, (numLiv,))
        result = cursor.fetchone()

        if result:
            numLiv, dateLiv  = result
            self.champ_numLiv.setText(str(numLiv))
            self.champ_dateLiv.setText(str(dateLiv))
        else:
            QMessageBox.warning(self, "Erreur", "La livraison spécifiée n'existe pas dans la table 'livraison'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()


    def modifier_livraison(self):
        numLiv = self.champ_numLiv.text()
        dateLiv = self.champ_dateLiv.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la livraison existe
        check = "SELECT numLiv FROM livraison WHERE numLiv = %s"
        cursor.execute(check, (numLiv,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "La livraison spécifiée n'existe pas dans la table 'livraison'.")
            return

        # Requête de modification
        update = "UPDATE livraison SET dateLiv = %s WHERE numLiv = %s"
        data = (dateLiv, numLiv)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "La livraison a été modifiée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class ListerDialogLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des livraisons")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the livraisons
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["numLiv", "dateLiv", "numT"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the livraisons
        self.load_livraisons()

    def load_livraisons(self):
        # Connection to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the livraisons
        select = "SELECT numLiv, dateLiv, numT FROM livraison"
        cursor.execute(select)
        livraisons = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(livraisons))

        # Populate the table widget with the livraisons
        for row, livraison in enumerate(livraisons):
            for col, value in enumerate(livraison):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogTran(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une Transaction")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numTrans = QLabel("Numero d'une Transaction:")
        self.champ_numTrans = QLineEdit()
        layout.addWidget(label_numTrans)
        layout.addWidget(self.champ_numTrans)

        label_produit_sortant = QLabel("produit sortant d'une Transaction:")
        self.champ_produit_sortant = QLineEdit()
        layout.addWidget(label_produit_sortant)
        layout.addWidget(self.champ_produit_sortant)

        label_produit_entrant = QLabel("produit entrant d'une Transaction:")
        self.champ_produit_entrant = QLineEdit()
        layout.addWidget(label_produit_entrant)
        layout.addWidget(self.champ_produit_entrant)

        label_dateH = QLabel("dateH d'une Transaction:")
        self.champ_dateH = QLineEdit()
        layout.addWidget(label_dateH)
        layout.addWidget(self.champ_dateH)

        label_seuilCom = QLabel("seuilCom d'une Transaction:")
        self.champ_seuilCom = QLineEdit()
        layout.addWidget(label_seuilCom)
        layout.addWidget(self.champ_seuilCom)

        # Bouton pour insérer la Transaction
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_transaction_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_transaction_db(self):
        numTrans = self.champ_numTrans.text()
        produit_sortant = self.champ_produit_sortant.text()
        produit_entrant = self.champ_produit_entrant.text()
        dateH = self.champ_dateH.text()
        seuilCom = self.champ_seuilCom.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête d'insertion
        insert = "INSERT INTO transactions (numTrans, produit_sortant, produit_entrant, dateH, seuilCom) VALUES (%s, %s, %s, %s, %s)"
        data = (numTrans, produit_sortant, produit_entrant, dateH, seuilCom)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "La transaction a été insérée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class SuppressionDialogTran(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une transaction")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numTrans = QLabel("Numero de transaction à supprimer:")
        self.champ_numTrans = QLineEdit()
        layout.addWidget(label_numTrans)
        layout.addWidget(self.champ_numTrans)

        # Bouton pour supprimer l'article
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_transaction_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_transaction_db(self):
        numTrans = self.champ_numTrans.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête de suppression
        delete = "DELETE FROM transactions WHERE numTrans = %s"
        cursor.execute(delete, (numTrans,))
        conn.commit()

        # Vérifier si la transaction a été supprimée
        if cursor.rowcount > 0:
            QMessageBox.information(None, "Succès", "La transaction a été supprimée avec succès!")
        else:
            QMessageBox.warning(None, "Erreur", "La transaction spécifiée n'existe pas dans la table 'transactions'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogTran(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier une transaction")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de l'transaction à modifier
        label_numTrans = QLabel("num de transaction à modifier:")
        self.champ_numTrans = QLineEdit()
        layout.addWidget(label_numTrans)
        layout.addWidget(self.champ_numTrans)

        # Bouton pour afficher les informations de l'transaction
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_transaction)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'transaction
        label_produit_sortant = QLabel("produit sortant de la transaction :")
        self.champ_produit_sortant = QLineEdit()
        layout.addWidget(label_produit_sortant)
        layout.addWidget(self.champ_produit_sortant)

        label_produit_entrant = QLabel("produit entrant de la transaction :")
        self.champ_produit_entrant = QLineEdit()
        layout.addWidget(label_produit_entrant)
        layout.addWidget(self.champ_produit_entrant)

        # Bouton pour modifier l'transaction
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_transaction)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_transaction(self):
        numTrans = self.champ_numTrans.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'transaction
        select = "SELECT numTrans, produit_sortant, produit_entrant FROM transactions WHERE numTrans = %s"
        cursor.execute(select, (numTrans,))
        result = cursor.fetchone()

        if result:
            numTrans, produit_sortant, produit_entrant = result
            self.champ_produit_sortant.setText(str(produit_sortant))
            self.champ_produit_entrant.setText(str(produit_entrant))
        else:
            QMessageBox.warning(self, "Erreur", "La transaction spécifiée n'existe pas dans la table 'transactions'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_transaction(self):
        numTrans = self.champ_numTrans.text()
        produit_sortant = self.champ_produit_sortant.text()
        produit_entrant = self.champ_produit_entrant.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si la transaction existe
        check = "SELECT numTrans FROM transactions WHERE numTrans = %s"
        cursor.execute(check, (numTrans,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "La transaction spécifiée n'existe pas dans la table 'transactions'.")
            return

        # Requête de modification
        update = "UPDATE transactions SET produit_sortant = %s, produit_entrant = %s WHERE numTrans = %s"
        data = (produit_sortant, produit_entrant, numTrans)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "La transaction a été modifiée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class ListerDialogTran(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des transactions")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the transactions
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["numTrans", "produit_sortant", "produit_entrant", "dateH" , "seuilCom"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the transactions
        self.load_transactions()

    def load_transactions(self):
        # Connection to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the transactions
        select = "SELECT numTrans, produit_sortant, produit_entrant, dateH , seuilCom FROM transactions"
        cursor.execute(select)
        transactions = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(transactions))

        # Populate the table widget with the transactions
        for row, transaction in enumerate(transactions):
            for col, value in enumerate(transaction):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class InsertionDialogDetailLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un détail de livraison")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_NDL = QLabel("Numéro de livraison:")
        self.champ_NDL = QLineEdit()
        layout.addWidget(label_NDL)
        layout.addWidget(self.champ_NDL)

        label_coutU = QLabel("Coût unitaire:")
        self.champ_coutU = QLineEdit()
        layout.addWidget(label_coutU)
        layout.addWidget(self.champ_coutU)

        label_prixU = QLabel("Prix unitaire:")
        self.champ_prixU = QLineEdit()
        layout.addWidget(label_prixU)
        layout.addWidget(self.champ_prixU)

        # Bouton pour insérer le détail de livraison
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_detailliv_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_detailliv_db(self):
        NDL = self.champ_NDL.text()
        coutU = self.champ_coutU.text()
        prixU = self.champ_prixU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le détail de livraison existe
        check = "SELECT NDL FROM detailLiv WHERE NDL = %s"
        cursor.execute(check, (NDL,))
        if cursor.fetchone() is not None:
            QMessageBox.warning(None, "Erreur", "Le détail de livraison spécifié existe déjà dans la table 'detailLiv'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO detailLiv (NDL, coutU, prixU) VALUES (%s, %s, %s)"
        data = (NDL, coutU, prixU)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "Le détail de livraison a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class ModificationDialogDetailLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un détail de livraison")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le NDL du détail de livraison à modifier
        label_NDL = QLabel("NDL à modifier:")
        self.champ_NDL = QLineEdit()
        layout.addWidget(label_NDL)
        layout.addWidget(self.champ_NDL)

        # Bouton pour afficher les informations du détail de livraison
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_detailliv)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs du détail de livraison
        label_coutU = QLabel("Cout unitaire:")
        self.champ_coutU = QLineEdit()
        layout.addWidget(label_coutU)
        layout.addWidget(self.champ_coutU)

        label_prixU = QLabel("Prix unitaire:")
        self.champ_prixU = QLineEdit()
        layout.addWidget(label_prixU)
        layout.addWidget(self.champ_prixU)

        # Bouton pour modifier le détail de livraison
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_detailliv)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_detailliv(self):
        NDL = self.champ_NDL.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations du détail de livraison
        select = "SELECT NDL, coutU, prixU FROM detailLiv WHERE NDL = %s"
        cursor.execute(select, (NDL,))
        result = cursor.fetchone()

        if result:
            NDL, coutU, prixU = result
            self.champ_NDL.setText(str(NDL))
            self.champ_coutU.setText(str(coutU))
            self.champ_prixU.setText(str(prixU))
        else:
            QMessageBox.warning(self, "Erreur", "Le détail de livraison spécifié n'existe pas dans la table 'detailLiv'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_detailliv(self):
        NDL = self.champ_NDL.text()
        coutU = self.champ_coutU.text()
        prixU = self.champ_prixU.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le détail de livraison existe
        check = "SELECT NDL FROM detailLiv WHERE NDL = %s"
        cursor.execute(check, (NDL,))
        if cursor.fetchone() is None:
            QMessageBox.warning(self, "Erreur", "Le détail de livraison spécifié n'existe pas dans la table 'detailLiv'.")
            return

        # Requête de modification
        update = "UPDATE detailLiv SET coutU = %s, prixU = %s WHERE NDL = %s"
        data = (coutU, prixU, NDL)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le détail de livraison a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class SuppressionDialogDetailLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un détail de livraison")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_NDL = QLabel("Numéro de livraison à supprimer:")
        self.champ_NDL = QLineEdit()
        layout.addWidget(label_NDL)
        layout.addWidget(self.champ_NDL)

        # Bouton pour supprimer le détail de livraison
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_detailLiv_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_detailLiv_db(self):
        NDL = self.champ_NDL.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le détail de livraison existe
        check = "SELECT NDL FROM detailLiv WHERE NDL = %s"
        cursor.execute(check, (NDL,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "Le détail de livraison spécifié n'existe pas dans la table 'detailLiv'.")
            return

        # Requête de suppression
        delete = "DELETE FROM detailLiv WHERE NDL = %s"
        cursor.execute(delete, (NDL,))
        conn.commit()

        QMessageBox.information(None, "Succès", "Le détail de livraison a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class ListerDialogDetailLiv(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des DetailLiv")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the articles
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["NDL", "coutU", "prixU"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the articles
        self.load_detaillivs()

    def load_detaillivs(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the articles
        select = "SELECT NDL, coutU, prixU FROM detailliv"
        cursor.execute(select)
        detaillivs = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(detaillivs))

        # Populate the table widget with the articles
        for row, detailliv in enumerate(detaillivs):
            for col, value in enumerate(detailliv):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////

class InsertionDialogTransp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un transporteur")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numT = QLabel("Numero de transport:")
        self.champ_numT = QLineEdit()
        layout.addWidget(label_numT)
        layout.addWidget(self.champ_numT)

        label_nomT = QLabel("Nom du transporteur:")
        self.champ_nomT = QLineEdit()
        layout.addWidget(label_nomT)
        layout.addWidget(self.champ_nomT)

        label_adresseT = QLabel("Adresse du transporteur:")
        self.champ_adresseT = QLineEdit()
        layout.addWidget(label_adresseT)
        layout.addWidget(self.champ_adresseT)

        label_teleT = QLabel("Téléphone du transporteur:")
        self.champ_teleT = QLineEdit()
        layout.addWidget(label_teleT)
        layout.addWidget(self.champ_teleT)

        label_fraixT = QLabel("Frais du transporteur:")
        self.champ_fraixT = QLineEdit()
        layout.addWidget(label_fraixT)
        layout.addWidget(self.champ_fraixT)

        label_typeT = QLabel("Type du transport:")
        self.champ_typeT = QLineEdit()
        layout.addWidget(label_typeT)
        layout.addWidget(self.champ_typeT)

        # Bouton pour insérer l'article
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_transporteur_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_transporteur_db(self):
        numT = self.champ_numT.text()
        nomT = self.champ_nomT.text()
        adresseT = self.champ_adresseT.text()
        teleT = self.champ_teleT.text()
        fraixT = self.champ_fraixT.text()
        typeT = self.champ_typeT.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le transporteur existe
        check = "SELECT numT FROM transporteur WHERE numT = %s"
        cursor.execute(check, (numT,))
        if cursor.fetchone() is not None:
            QMessageBox.warning(self, "Erreur", "Le transporteur spécifié existe déjà dans la table 'transporteur'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO transporteur (numT, nomT, adresseT, teleT, fraixT, typeT) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (numT, nomT, adresseT, teleT, fraixT, typeT)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le transporteur a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class SuppressionDialogTransp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un transporteur")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout(self)

        # Label et champ de saisie
        label_numT = QLabel("Numéro du transporteur à supprimer:")
        self.champ_numT = QLineEdit()
        layout.addWidget(label_numT)
        layout.addWidget(self.champ_numT)

        # Bouton pour supprimer le transporteur
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_transporteur_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_transporteur_db(self):
        numT = self.champ_numT.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le transporteur existe
        check = "SELECT numT FROM transporteur WHERE numT = %s"
        cursor.execute(check, (numT,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "Le transporteur spécifié n'existe pas dans la table 'transporteur'.")
            return

        # Requête de suppression
        delete = "DELETE FROM transporteur WHERE numT = %s"
        cursor.execute(delete, (numT,))
        conn.commit()

        QMessageBox.information(self, "Succès", "Le transporteur a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogTransp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un transporteur")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout(self)

        label_numT = QLabel("Numéro du transporteur à modifier:")
        self.champ_numT = QLineEdit()
        layout.addWidget(label_numT)
        layout.addWidget(self.champ_numT)

        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_transporteur)
        layout.addWidget(bouton_afficher)

        label_nomT = QLabel("Nom du transporteur:")
        self.champ_nomT = QLineEdit()
        layout.addWidget(label_nomT)
        layout.addWidget(self.champ_nomT)

        label_adresseT = QLabel("Adresse du transporteur:")
        self.champ_adresseT = QLineEdit()
        layout.addWidget(label_adresseT)
        layout.addWidget(self.champ_adresseT)

        label_teleT = QLabel("Téléphone du transporteur:")
        self.champ_teleT = QLineEdit()
        layout.addWidget(label_teleT)
        layout.addWidget(self.champ_teleT)

        label_fraixT = QLabel("Frais du transporteur:")
        self.champ_fraixT = QLineEdit()
        layout.addWidget(label_fraixT)
        layout.addWidget(self.champ_fraixT)

        label_typeT = QLabel("Type:")
        self.champ_typeT = QLineEdit()
        layout.addWidget(label_typeT)
        layout.addWidget(self.champ_typeT)

        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_transporteur)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_transporteur(self):
        numT = self.champ_numT.text()

        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        select = "SELECT numT, nomT, adresseT, teleT, fraixT, typeT FROM transporteur WHERE numT = %s"
        cursor.execute(select, (numT,))
        result = cursor.fetchone()

        if result:
            numT, nomT, adresseT, teleT, fraixT, typeT = result
            self.champ_nomT.setText(str(nomT))
            self.champ_adresseT.setText(str(adresseT))
            self.champ_teleT.setText(str(teleT))
            self.champ_fraixT.setText(str(fraixT))
            self.champ_typeT.setText(str(typeT))
        else:
            QMessageBox.warning(self, "Erreur", "Le transporteur spécifié n'existe pas dans la table 'transporteur'.")

        cursor.close()
        conn.close()

    def modifier_transporteur(self):
        numT = self.champ_numT.text()
        nomT = self.champ_nomT.text()
        adresseT = self.champ_adresseT.text()
        teleT = self.champ_teleT.text()
        fraixT = self.champ_fraixT.text()
        typeT = self.champ_typeT.text()

        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        check = "SELECT numT FROM transporteur WHERE numT = %s"
        cursor.execute(check, (numT,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "Le transporteur spécifié n'existe pas dans la table 'transporteur'.")
            return

        update = "UPDATE transporteur SET nomT = %s, adresseT = %s, teleT = %s, fraixT = %s, typeT = %s WHERE numT = %s"
        data = (nomT, adresseT, teleT, fraixT, typeT, numT)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le transporteur a été modifié avec succès!")

        cursor.close()
        conn.close()

        self.accept()

class ListerDialogTransp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des transporteurs")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout(self)

        # Table widget to display the transporteurs
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["numT", "nomT", "adresseT", "teleT", "fraixT", "typeT"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the transporteurs
        self.load_transporteurs()

    def load_transporteurs(self):
        # Connection to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the transporteurs
        select = "SELECT numT, nomT, adresseT, teleT, fraixT, typeT FROM transporteur"
        cursor.execute(select)
        transporteurs = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(transporteurs))

        # Populate the table widget with the transporteurs
        for row, transporteur in enumerate(transporteurs):
            for col, value in enumerate(transporteur):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////

class InsertionDialogCli(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer un Client")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numCli = QLabel("Numero de Client:")
        self.champ_numCli = QLineEdit()
        layout.addWidget(label_numCli)
        layout.addWidget(self.champ_numCli)

        label_nomCli = QLabel("Nom du Client:")
        self.champ_nomCli = QLineEdit()
        layout.addWidget(label_nomCli)
        layout.addWidget(self.champ_nomCli)

        label_adresseCli = QLabel("Adresse du Client:")
        self.champ_adresseCli = QLineEdit()
        layout.addWidget(label_adresseCli)
        layout.addWidget(self.champ_adresseCli)

        label_teleCli = QLabel("Téléphone du Client:")
        self.champ_teleCli = QLineEdit()
        layout.addWidget(label_teleCli)
        layout.addWidget(self.champ_teleCli)

        # Bouton pour insérer le client
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_client_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_client_db(self):
        numCli = self.champ_numCli.text()
        nomCli = self.champ_nomCli.text()
        adresseCli = self.champ_adresseCli.text()
        teleCli = self.champ_teleCli.text()
        

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le client existe
        check = "SELECT numCli FROM client WHERE numCli = %s"
        cursor.execute(check, (numCli,))
        if cursor.fetchone() is not None:
            QMessageBox.warning(self, "Erreur", "Le client spécifié existe déjà dans la table 'client'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO client (numCli, nomCli, adresseCli, teleCli) VALUES (%s, %s, %s, %s)"
        data = (numCli, nomCli, adresseCli, teleCli)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le client a été inséré avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogCli(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier un Client")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le numCli du client à modifier
        label_NumCli = QLabel("Numero de client  à modifier:")
        self.champ_numCli = QLineEdit()
        layout.addWidget(label_NumCli)
        layout.addWidget(self.champ_numCli)

        # Bouton pour afficher les informations du client
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_client)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs du client
        label_nomCli = QLabel("nom de client:")
        self.champ_nomCli = QLineEdit()
        layout.addWidget(label_nomCli)
        layout.addWidget(self.champ_nomCli)

        label_adresseCli = QLabel("Adresse de client :")
        self.champ_adresseCli = QLineEdit()
        layout.addWidget(label_adresseCli)
        layout.addWidget(self.champ_adresseCli)

        label_teleCli = QLabel("Adresse de client :")
        self.champ_teleCli = QLineEdit()
        layout.addWidget(label_teleCli)
        layout.addWidget(self.champ_teleCli)


        # Bouton pour modifier le client
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_client)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_client(self):
        numCli = self.champ_numCli.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations du client
        select = "SELECT numCli, nomCli, adresseCli , teleCli FROM client WHERE numCli = %s"
        cursor.execute(select, (numCli,))
        result = cursor.fetchone()

        if result:
            numCli, nomCli, adresseCli , teleCli = result
            self.champ_numCli.setText(str(numCli))
            self.champ_nomCli.setText(str(nomCli))
            self.champ_adresseCli.setText(str(adresseCli))
            self.champ_teleCli.setText(str(teleCli))
        else:
            QMessageBox.warning(self, "Erreur", "Le client spécifié n'existe pas dans la table 'client'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

    def modifier_client(self):
        numCli = self.champ_numCli.text()
        nomCli = self.champ_nomCli.text()
        adresseCli = self.champ_adresseCli.text()
        teleCli = self.champ_teleCli.text()
        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le client existe
        check = "SELECT numCli FROM client WHERE numCli = %s"
        cursor.execute(check, (numCli,))
        if cursor.fetchone() is None:
            QMessageBox.warning(self, "Erreur", "Le client spécifié n'existe pas dans la table 'client'.")
            return

        # Requête de modification
        update = "UPDATE client SET nomCli = %s, adresseCli = %s , teleCli =%s WHERE numCli = %s"
        data = (nomCli,adresseCli , teleCli,numCli)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "Le client a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class SuppressionDialogCli(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer un client ")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numCli = QLabel("Numéro de client à supprimer:")
        self.champ_numCli = QLineEdit()
        layout.addWidget(label_numCli)
        layout.addWidget(self.champ_numCli)

        # Bouton pour supprimer le client
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_client_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_client_db(self):
        numCli = self.champ_numCli.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si le client existe
        check = "SELECT numCli FROM client WHERE numCli = %s"
        cursor.execute(check, (numCli,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "Le client spécifié n'existe pas dans la table 'client'.")
            return

        # Requête de suppression
        delete = "DELETE FROM client WHERE numCli = %s"
        cursor.execute(delete, (numCli,))
        conn.commit()

        QMessageBox.information(None, "Succès", "Le client a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()

class ListerDialogDetailCli(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des clients")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the clients
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["numCli", "nomCli", "adresseCli", "teleCli"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the clients
        self.load_clients()

    def load_clients(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the clients
        select = "SELECT numCli, nomCli, adresseCli, teleCli FROM client"
        cursor.execute(select)
        clients = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(clients))

        # Populate the table widget with the clients
        for row, client in enumerate(clients):
            for col, value in enumerate(client):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////

class InsertionDialogExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Insérer une expedition")
        self.setGeometry(100, 100, 300, 300)
        layout = QVBoxLayout()

        # Labels et champs de saisie
        label_numExp = QLabel("Numéro de l'expédition:")
        self.champ_numExp = QLineEdit()
        layout.addWidget(label_numExp)
        layout.addWidget(self.champ_numExp)

        label_dateExp = QLabel("Date de l'expédition:")
        self.champ_dateExp = QLineEdit()
        layout.addWidget(label_dateExp)
        layout.addWidget(self.champ_dateExp)

        label_cout = QLabel("Coût de l'expédition:")
        self.champ_cout = QLineEdit()
        layout.addWidget(label_cout)
        layout.addWidget(self.champ_cout)

        label_statut = QLabel("Statut:")
        self.champ_statut = QLineEdit()
        layout.addWidget(label_statut)
        layout.addWidget(self.champ_statut)

        # Bouton pour insérer l'expédition
        bouton_insere = QPushButton("Insérer")
        bouton_insere.clicked.connect(self.insere_expedition_db)
        layout.addWidget(bouton_insere)

        self.setLayout(layout)

    def insere_expedition_db(self):
        numExp = self.champ_numExp.text()
        dateExp = self.champ_dateExp.text()
        cout = self.champ_cout.text()
        statut = self.champ_statut.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'expédition existe
        check = "SELECT NumExp FROM expedition WHERE NumExp = %s"
        cursor.execute(check, (numExp,))
        if cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "L'expédition spécifiée existe déjà dans la table 'expedition'.")
            return

        # Requête d'insertion
        insert = "INSERT INTO expedition (NumExp, dateExp, cout, statut) VALUES (%s, %s, %s, %s)"
        data = (numExp, dateExp, cout, statut)
        cursor.execute(insert, data)
        conn.commit()

        QMessageBox.information(None, "Succès", "L'expédition a été insérée avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()


class SuppressionDialogExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Supprimer une expedition")
        self.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        # Label et champ de saisie
        label_numExp = QLabel("numero d'expedition à supprimer:")
        self.champ_numExp = QLineEdit()
        layout.addWidget(label_numExp)
        layout.addWidget(self.champ_numExp)

        # Bouton pour supprimer l'article
        bouton_supprime = QPushButton("Supprimer")
        bouton_supprime.clicked.connect(self.supprime_expedition_db)
        layout.addWidget(bouton_supprime)

        self.setLayout(layout)

    def supprime_expedition_db(self):
        numExp = self.champ_numExp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'article existe
        check = "SELECT numExp FROM expedition WHERE numExp = %s"
        cursor.execute(check, (numExp,))
        if not cursor.fetchone():
            QMessageBox.warning(None, "Erreur", "expedition spécifié n'existe pas dans la table 'expedition'.")
            return

        # Requête de suppression
        delete = "DELETE FROM expedition WHERE numExp = %s"
        cursor.execute(delete, (numExp,))
        conn.commit()

        QMessageBox.information(None, "Succès", "expedition a été supprimé avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()
        self.accept()

class ModificationDialogExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modifier une expedition")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        # Label et champ de saisie pour le code de l'article à modifier
        label_numExp = QLabel("numero de l'expediteur à modifier:")
        self.champ_numExp = QLineEdit()
        layout.addWidget(label_numExp)
        layout.addWidget(self.champ_numExp)

        # Bouton pour afficher les informations de l'article
        bouton_afficher = QPushButton("Afficher")
        bouton_afficher.clicked.connect(self.afficher_expedition)
        layout.addWidget(bouton_afficher)

        # Labels et champs de saisie pour les attributs de l'article
        label_dateExp = QLabel("date de l'expedition:")
        self.champ_dateExp = QLineEdit()
        layout.addWidget(label_dateExp)
        layout.addWidget(self.champ_dateExp)

        label_cout = QLabel("cout de l'expedition:")
        self.champ_cout = QLineEdit()
        layout.addWidget(label_cout)
        layout.addWidget(self.champ_cout)

        label_statut = QLabel("statut de l'expedition:")
        self.champ_statut = QLineEdit()
        layout.addWidget(label_statut)
        layout.addWidget(self.champ_statut)

        # Bouton pour modifier l'article
        bouton_modifier = QPushButton("Modifier")
        bouton_modifier.clicked.connect(self.modifier_expedition)
        layout.addWidget(bouton_modifier)

        self.setLayout(layout)

    def afficher_expedition(self):
        numExp = self.champ_numExp.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de l'expedition
        select = "SELECT numExp, dateExp, cout, statut  FROM expedition WHERE numExp = %s"
        cursor.execute(select, (numExp,))
        result = cursor.fetchone()

        if result:
            numExp, dateExp, cout, statut = result
            self.champ_numExp.setText(str(numExp))  # Convert numExp to string
            self.champ_dateExp.setText(str(dateExp))  # Convert dateExp to string
            self.champ_cout.setText(str(cout))  # Convert cout to string
            self.champ_statut.setText(str(statut))  # Convert statut to string
        else:
            QMessageBox.warning(self, "Erreur", "L'expedition spécifié n'existe pas dans la table 'expedition'.")

        # Fermeture de la connexion
        cursor.close()
        conn.close()



    def modifier_expedition(self):
        numExp = self.champ_numExp.text()
        dateExp = self.champ_dateExp.text()
        cout = self.champ_cout.text()
        statut = self.champ_statut.text()

        # Connexion à la base de données
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Vérifier si l'article existe
        check = "SELECT numExp FROM expedition WHERE numExp = %s"
        cursor.execute(check, (numExp,))
        if not cursor.fetchone():
            QMessageBox.warning(self, "Erreur", "L'expedition spécifié n'existe pas dans la table 'expedition'.")
            return

        # Requête de modification
        update = "UPDATE expedition SET dateExp = %s, cout = %s, statut = %s WHERE numExp = %s"
        data = (dateExp, cout, statut, numExp)
        cursor.execute(update, data)
        conn.commit()

        QMessageBox.information(self, "Succès", "L'expedition a été modifié avec succès!")

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        self.accept()


class ListerDialogExp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Liste des expeditions")
        self.setGeometry(100, 100, 900, 500)
        layout = QVBoxLayout()

        # Table widget to display the articles
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["numExp", "dateExp", "cout", "statut"])
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        # Load and display the articles
        self.load_expeditions()

    def load_expeditions(self):
        # Connexion to the database
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="stock"
        )
        cursor = conn.cursor()

        # Query to retrieve the articles
        select = "SELECT numExp, dateExp, cout, statut FROM expedition"
        cursor.execute(select)
        expeditions = cursor.fetchall()

        # Set the number of rows in the table widget
        self.table_widget.setRowCount(len(expeditions))

        # Populate the table widget with the articles
        for row, expedition in enumerate(expeditions):
            for col, value in enumerate(expedition):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        # Close the connection
        cursor.close()
        conn.close()

#//////////////////////////////////////////////////
class Gestion_produit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Produit")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Bouton Gestion Produit
        bouton_gestion_produit = QPushButton("Gestion Produit")
        bouton_gestion_produit.clicked.connect(self.show_table_menu)
        layout.addWidget(bouton_gestion_produit)

        # Bouton supplémentaire
        bouton_supplementaire = QPushButton("RETOUR AU MENU PRINCIPAL")
        bouton_supplementaire.clicked.connect(self.close)
        layout.addWidget(bouton_supplementaire)

        # Configurer le layout dans la fenêtre
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_table_menu(self):
        menu = QMenu()
        table_menu_article = QMenu("Article")
        
        # Options de menu pour la table Article
        action_inserer_article = QAction("Insérer", menu)
        action_inserer_article.triggered.connect(self.insere_article)
        table_menu_article.addAction(action_inserer_article)

        action_modifier_article = QAction("Modifier", menu)
        action_modifier_article.triggered.connect(self.modifier_article)
        table_menu_article.addAction(action_modifier_article)

        action_supprimer_article = QAction("Supprimer", menu)
        action_supprimer_article.triggered.connect(self.supprimer_article)
        table_menu_article.addAction(action_supprimer_article)

        action_lister_article = QAction("Lister", menu)
        action_lister_article.triggered.connect(self.lister_article)
        table_menu_article.addAction(action_lister_article)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_article.addAction(action_quitter)

        # Ajouter le menu de la table Article au menu principal
        menu.addMenu(table_menu_article)


        table_menu_categorie = QMenu("Categorie")
        
        # Options de menu pour la table Categorie
        action_inserer_categorie = QAction("Insérer", menu)
        action_inserer_categorie.triggered.connect(self.insere_categorie)
        table_menu_categorie.addAction(action_inserer_categorie)

        action_modifier_categorie = QAction("Modifier", menu)
        action_modifier_categorie.triggered.connect(self.modifier_categorie)
        table_menu_categorie.addAction(action_modifier_categorie)

        action_supprimer_categorie = QAction("Supprimer", menu)
        action_supprimer_categorie.triggered.connect(self.supprimer_categorie)
        table_menu_categorie.addAction(action_supprimer_categorie)

        action_lister_categorie = QAction("Lister", menu)
        action_lister_categorie.triggered.connect(self.lister_categorie)
        table_menu_categorie.addAction(action_lister_categorie)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_categorie.addAction(action_quitter)

        # Ajouter le menu de la table Categorie au menu principal
        menu.addMenu(table_menu_categorie)

        table_menu_emplacement = QMenu("Emplacement")
        
        # Options de menu pour la table Emplacement
        action_inserer_emplacement = QAction("Insérer", menu)
        action_inserer_emplacement.triggered.connect(self.insere_emplacement)
        table_menu_emplacement.addAction(action_inserer_emplacement)

        action_modifier_emplacement = QAction("Modifier", menu)
        action_modifier_emplacement.triggered.connect(self.modifier_emplacement)
        table_menu_emplacement.addAction(action_modifier_emplacement)
        
        action_supprimer_emplacement = QAction("Supprimer", menu)
        action_supprimer_emplacement.triggered.connect(self.supprimer_emplacement)
        table_menu_emplacement.addAction(action_supprimer_emplacement)

        actionlister_emplacement = QAction("Lister", menu)
        actionlister_emplacement.triggered.connect(self.lister_emplacement)
        table_menu_emplacement.addAction(actionlister_emplacement)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_emplacement.addAction(action_quitter)

        # Ajouter le menu de la table Categorie au menu principal
        menu.addMenu(table_menu_emplacement)

        # Afficher le menu
        menu.exec_()

    def insere_article(self):
        dialog = InsertionDialog()
        dialog.exec_()

    def modifier_article(self):
        # Logique pour modifier un article
        dialog = ModificationDialog()
        dialog.exec_()

    def supprimer_article(self):
        dialog = SuppressionDialog()
        dialog.exec_()

    def lister_article(self):
        # Logique pour lister les articles
        dialog = ListerDialog()
        dialog.exec_()

    def quitter(self):
        sys.exit()

    def action_supplementaire(self):
        sys.exit()

    def insere_categorie(self):
        dialog2 = InsertionDialogCat()
        dialog2.exec_()

    def modifier_categorie(self):
        dialog2 = ModificationDialogCat()
        dialog2.exec_()

    def supprimer_categorie(self):
        dialog2=SuppressionDialogCat()
        dialog2.exec_()

    def lister_categorie(self):
        dialog2 = ListerDialogCat()
        dialog2.exec_()

    def insere_emplacement(self):
        dialog3 = InsertionDialogEmp()
        dialog3.exec_()

    def modifier_emplacement(self):
        dialog3 = ModificationDialogEmp()
        dialog3.exec_()

    def supprimer_emplacement(self):
        dialog3 = SuppressionDialogEmp()
        dialog3.exec_()

    def lister_emplacement(self):
        dialog3 = ListerDialogEmp()
        dialog3.exec_()



#//////////////////////////////////////////////////


class Gestion_commande(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Commande")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Bouton Gestion Commande
        bouton_gestion_commande = QPushButton("Gestion Commande")
        bouton_gestion_commande.clicked.connect(self.show_table_menu)
        layout.addWidget(bouton_gestion_commande)

        # Bouton supplémentaire
        bouton_supplementaire = QPushButton("RETOUR AU MENU PRINCIPAL")
        bouton_supplementaire.clicked.connect(self.close)
        layout.addWidget(bouton_supplementaire)

        # Configurer le layout dans la fenêtre
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_table_menu(self):
        menu = QMenu()
        table_menu_commande = QMenu("Commande")
        
        # Options de menu pour la table Article
        action_inserer_commande = QAction("Insérer", menu)
        action_inserer_commande.triggered.connect(self.insere_commande)
        table_menu_commande.addAction(action_inserer_commande)

        action_modifier_commande = QAction("Modifier", menu)
        action_modifier_commande.triggered.connect(self.modifier_commande)
        table_menu_commande.addAction(action_modifier_commande)

        action_supprimer_commande = QAction("Supprimer", menu)
        action_supprimer_commande.triggered.connect(self.supprimer_commande)
        table_menu_commande.addAction(action_supprimer_commande)

        action_lister_commande = QAction("Lister", menu)
        action_lister_commande.triggered.connect(self.lister_commande)
        table_menu_commande.addAction(action_lister_commande)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_commande.addAction(action_quitter)

        # Ajouter le menu de la table Article au menu principal
        menu.addMenu(table_menu_commande)


        table_menu_detailCom = QMenu("Detail Commande")
        
        # Options de menu pour la table detailCom
        action_inserer_detailCom = QAction("Insérer", menu)
        action_inserer_detailCom.triggered.connect(self.insere_detailCom)
        table_menu_detailCom.addAction(action_inserer_detailCom)

        action_modifier_detailCom = QAction("Modifier", menu)
        action_modifier_detailCom.triggered.connect(self.modifier_detailCom)
        table_menu_detailCom.addAction(action_modifier_detailCom)

        action_supprimer_detailCom = QAction("Supprimer", menu)
        action_supprimer_detailCom.triggered.connect(self.supprimer_detailCom)
        table_menu_detailCom.addAction(action_supprimer_detailCom)

        action_lister_detailCom = QAction("Lister", menu)
        action_lister_detailCom.triggered.connect(self.lister_detailCom)
        table_menu_detailCom.addAction(action_lister_detailCom)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_detailCom.addAction(action_quitter)

        # Ajouter le menu de la table Categorie au menu principal
        menu.addMenu(table_menu_detailCom)

        table_menu_fournisseur = QMenu("Fournisseur")
        
        # Options de menu pour la table fournisseur
        action_inserer_fournisseur = QAction("Insérer", menu)
        action_inserer_fournisseur.triggered.connect(self.insere_fournisseur)
        table_menu_fournisseur.addAction(action_inserer_fournisseur)

        action_modifier_fournisseur = QAction("Modifier", menu)
        action_modifier_fournisseur.triggered.connect(self.modifier_fournisseur)
        table_menu_fournisseur.addAction(action_modifier_fournisseur)
        
        action_supprimer_fournisseur = QAction("Supprimer", menu)
        action_supprimer_fournisseur.triggered.connect(self.supprimer_fournisseur)
        table_menu_fournisseur.addAction(action_supprimer_fournisseur)

        actionlister_fournisseur = QAction("Lister", menu)
        actionlister_fournisseur.triggered.connect(self.lister_fournisseur)
        table_menu_fournisseur.addAction(actionlister_fournisseur)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_fournisseur.addAction(action_quitter)

        # Ajouter le menu de la table fournisseur au menu principal
        menu.addMenu(table_menu_fournisseur)

        # Afficher le menu
        menu.exec_()

    def insere_commande(self):
        dialog4=InsertionDialogCom()
        dialog4.exec_()

    def modifier_commande(self):
        dialog4=ModificationDialogCom()
        dialog4.exec_()

    def supprimer_commande(self):
        dialog4 = SuppressionDialogCom()
        dialog4.exec_()

    def lister_commande(self):
        dialog4 = ListerDialogCom()
        dialog4.exec_()

    def quitter(self):
        sys.exit()

    def action_supplementaire(self):
        sys.exit()

    def insere_detailCom(self):
        dialog5 = InsertionDialogDetCom()
        dialog5.exec_()

    def modifier_detailCom(self):
        dialog5 = ModificationDialogDetCom()
        dialog5.exec_()

    def supprimer_detailCom(self):
        dialog5 = SuppressionDialogDetCom()
        dialog5.exec_()

    def lister_detailCom(self):
        dialog5 = ListerDialogDetCom()
        dialog5.exec_()


    def insere_fournisseur(self):
        dialog6=InsertionDialogFou()
        dialog6.exec_()

    def modifier_fournisseur(self):
        dialog6=ModificationDialogFou()
        dialog6.exec_()

    def supprimer_fournisseur(self):
        dialog6 = SuppressionDialogFou()
        dialog6.exec_()

    def lister_fournisseur(self):
        dialog6 = ListerDialogFou()
        dialog6.exec_()
        
#/////////////


class Gestion_stock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Stock")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Bouton Gestion Stock
        bouton_gestion_stock = QPushButton("Gestion Stock")
        bouton_gestion_stock.clicked.connect(self.show_table_menu)
        layout.addWidget(bouton_gestion_stock)

        # Bouton supplémentaire
        bouton_supplementaire = QPushButton("RETOUR AU MENU PRINCIPAL")
        bouton_supplementaire.clicked.connect(self.close)
        layout.addWidget(bouton_supplementaire)

        # Configurer le layout dans la fenêtre
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_table_menu(self):
        menu = QMenu()
        table_menu_utilisateur = QMenu("Utilisateur")

        # Options de menu pour la table Utilisateur
        action_inserer_utilisateur = QAction("Insérer", menu)
        action_inserer_utilisateur.triggered.connect(self.insere_utilisateur)
        table_menu_utilisateur.addAction(action_inserer_utilisateur)

        action_modifier_utilisateur = QAction("Modifier", menu)
        action_modifier_utilisateur.triggered.connect(self.modifier_utilisateur)
        table_menu_utilisateur.addAction(action_modifier_utilisateur)

        action_supprimer_utilisateur = QAction("Supprimer", menu)
        action_supprimer_utilisateur.triggered.connect(self.supprimer_utilisateur)
        table_menu_utilisateur.addAction(action_supprimer_utilisateur)

        action_lister_utilisateur = QAction("Lister", menu)
        action_lister_utilisateur.triggered.connect(self.lister_utilisateur)
        table_menu_utilisateur.addAction(action_lister_utilisateur)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_utilisateur.addAction(action_quitter)

        # Ajouter le menu de la table Utilisateur au menu principal
        menu.addMenu(table_menu_utilisateur)

        table_menu_role = QMenu("Role")

        # Options de menu pour la table Role
        action_inserer_role = QAction("Insérer", menu)
        action_inserer_role.triggered.connect(self.insere_role)
        table_menu_role.addAction(action_inserer_role)

        action_modifier_role = QAction("Modifier", menu)
        action_modifier_role.triggered.connect(self.modifier_role)
        table_menu_role.addAction(action_modifier_role)

        action_supprimer_role = QAction("Supprimer", menu)
        action_supprimer_role.triggered.connect(self.supprimer_role)
        table_menu_role.addAction(action_supprimer_role)

        action_lister_role = QAction("Lister", menu)
        action_lister_role.triggered.connect(self.lister_role)
        table_menu_role.addAction(action_lister_role)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_role.addAction(action_quitter)

        # Ajouter le menu de la table Role au menu principal
        menu.addMenu(table_menu_role)

        table_menu_historique = QMenu("Historique")

        # Options de menu pour la table Historique
        action_inserer_historique = QAction("Insérer", menu)
        action_inserer_historique.triggered.connect(self.insere_historique)
        table_menu_historique.addAction(action_inserer_historique)

        action_modifier_historique = QAction("Modifier", menu)
        action_modifier_historique.triggered.connect(self.modifier_historique)
        table_menu_historique.addAction(action_modifier_historique)

        action_supprimer_historique = QAction("Supprimer", menu)
        action_supprimer_historique.triggered.connect(self.supprimer_historique)
        table_menu_historique.addAction(action_supprimer_historique)

        action_lister_historique = QAction("Lister", menu)
        action_lister_historique.triggered.connect(self.lister_historique)
        table_menu_historique.addAction(action_lister_historique)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_historique.addAction(action_quitter)

        # Ajouter le menu de la table Historique au menu principal
        menu.addMenu(table_menu_historique)

        table_menu_alerte = QMenu("Alerte")

        # Options de menu pour la table alerte
        action_inserer_alerte = QAction("Insérer", menu)
        action_inserer_alerte.triggered.connect(self.insere_alerte)
        table_menu_alerte.addAction(action_inserer_alerte)

        action_modifier_alerte = QAction("Modifier", menu)
        action_modifier_alerte.triggered.connect(self.modifier_alerte)
        table_menu_alerte.addAction(action_modifier_alerte)

        action_supprimer_alerte = QAction("Supprimer", menu)
        action_supprimer_alerte.triggered.connect(self.supprimer_alerte)
        table_menu_alerte.addAction(action_supprimer_alerte)

        action_lister_alerte = QAction("Lister", menu)
        action_lister_alerte.triggered.connect(self.lister_alerte)
        table_menu_alerte.addAction(action_lister_alerte)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_alerte.addAction(action_quitter)

        # Ajouter le menu de la table Alerte au menu principal
        menu.addMenu(table_menu_alerte)


        table_menu_parametre = QMenu("Patametre_stock")

        # Options de menu pour la table parametre
        action_inserer_parametre = QAction("Insérer", menu)
        action_inserer_parametre.triggered.connect(self.insere_parametre)
        table_menu_parametre.addAction(action_inserer_parametre)

        action_modifier_parametre = QAction("Modifier", menu)
        action_modifier_parametre.triggered.connect(self.modifier_parametre)
        table_menu_parametre.addAction(action_modifier_parametre)

        action_supprimer_parametre = QAction("Supprimer", menu)
        action_supprimer_parametre.triggered.connect(self.supprimer_parametre)
        table_menu_parametre.addAction(action_supprimer_parametre)

        action_lister_parametre = QAction("Lister", menu)
        action_lister_parametre.triggered.connect(self.lister_parametre)
        table_menu_parametre.addAction(action_lister_parametre)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_parametre.addAction(action_quitter)

        # Ajouter le menu de la table parametre au menu principal
        menu.addMenu(table_menu_parametre)


        # Afficher le menu
        menu.exec_()

    def insere_utilisateur(self):
        dialog7 = InsertionDialogUtile()
        dialog7.exec_()

    def supprimer_utilisateur(self):
        dialog7 = SuppressionDialogUtile()
        dialog7.exec_()

    def modifier_utilisateur(self):
        dialog7 = ModificationDialogUtile()
        dialog7.exec_()

    def lister_utilisateur(self):
        dialog7 = ListerDialogUtile()
        dialog7.exec_()

    def insere_role(self):
        dialog8 = InsertionDialogRole()
        dialog8.exec_()

    def supprimer_role(self):
        dialog8 = SuppressionDialogRole()
        dialog8.exec_()

    def modifier_role(self):
        dialog8 = ModificationDialogRole()
        dialog8.exec_()

    def lister_role(self):
        dialog8 = ListerDialogRole()
        dialog8.exec_()

    def insere_historique(self):
        dialog9 = InsertionDialogHis()
        dialog9.exec_()

    def supprimer_historique(self):
        dialog9 = SuppressionDialogHis()
        dialog9.exec_()

    def modifier_historique(self):
        dialog9 = ModificationDialogHis()
        dialog9.exec_()

    def lister_historique(self):
        dialog9 = ListerDialogHis()
        dialog9.exec_()

    def insere_alerte(self):
        dialog10 = InsertionDialogAl()
        dialog10.exec_()

    def supprimer_alerte(self):
        dialog10 = SuppressionDialogAl()
        dialog10.exec_()

    def modifier_alerte(self):
        dialog10 = ModificationDialogAl()
        dialog10.exec_()

    def lister_alerte(self):
        dialog10 = ListerDialogAl()
        dialog10.exec_()

    def insere_parametre(self):
        dialog9 = InsertionDialogPs()
        dialog9.exec_()

    def supprimer_parametre(self):
        dialog9 = SuppressionDialogPs()
        dialog9.exec_()

    def modifier_parametre(self):
        dialog9 = ModificationDialogPs()
        dialog9.exec_()

    def lister_parametre(self):
        dialog9 = ListerDialogPs()
        dialog9.exec_()

    def quitter(self):
        sys.exit()

#///////////

class Gestion_livraison(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion Livraison")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Bouton Gestion Livraison
        bouton_gestion_livraison = QPushButton("Gestion Livraison")
        bouton_gestion_livraison.clicked.connect(self.show_table_menu)
        layout.addWidget(bouton_gestion_livraison)

        # Bouton supplémentaire
        bouton_supplementaire = QPushButton("RETOUR AU MENU PRINCIPAL")
        bouton_supplementaire.clicked.connect(self.close)
        layout.addWidget(bouton_supplementaire)

        # Configurer le layout dans la fenêtre
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_table_menu(self):
        menu = QMenu()
        table_menu_livraison = QMenu("Livraison")

        # Options de menu pour la table livraison
        action_inserer_livraison = QAction("Insérer", menu)
        action_inserer_livraison.triggered.connect(self.insere_livraison)
        table_menu_livraison.addAction(action_inserer_livraison)

        action_modifier_livraison = QAction("Modifier", menu)
        action_modifier_livraison.triggered.connect(self.modifier_livraison)
        table_menu_livraison.addAction(action_modifier_livraison)

        action_supprimer_livraison = QAction("Supprimer", menu)
        action_supprimer_livraison.triggered.connect(self.supprimer_livraison)
        table_menu_livraison.addAction(action_supprimer_livraison)

        action_lister_livraison = QAction("Lister", menu)
        action_lister_livraison.triggered.connect(self.lister_livraison)
        table_menu_livraison.addAction(action_lister_livraison)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_livraison.addAction(action_quitter)
        # Ajouter le menu de la table livraison au menu principal
        menu.addMenu(table_menu_livraison)

        table_menu_transaction = QMenu("Transaction")

        # Options de menu pour la table transaction
        action_inserer_transaction = QAction("Insérer", menu)
        action_inserer_transaction.triggered.connect(self.insere_transaction)
        table_menu_transaction.addAction(action_inserer_transaction)

        action_modifier_transaction = QAction("Modifier", menu)
        action_modifier_transaction.triggered.connect(self.modifier_transaction)
        table_menu_transaction.addAction(action_modifier_transaction)

        action_supprimer_transaction = QAction("Supprimer", menu)
        action_supprimer_transaction.triggered.connect(self.supprimer_transaction)
        table_menu_transaction.addAction(action_supprimer_transaction)

        action_lister_transaction= QAction("Lister", menu)
        action_lister_transaction.triggered.connect(self.lister_transaction)
        table_menu_transaction.addAction(action_lister_transaction)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_transaction.addAction(action_quitter)

        # Ajouter le menu de la table transaction au menu principal
        menu.addMenu(table_menu_transaction)

        table_menu_DetLiv = QMenu("Detail Livraison")

        # Options de menu pour la table DetLiv
        action_inserer_DetLiv = QAction("Insérer", menu)
        action_inserer_DetLiv.triggered.connect(self.insere_DetLiv)
        table_menu_DetLiv.addAction(action_inserer_DetLiv)

        action_modifier_DetLiv = QAction("Modifier", menu)
        action_modifier_DetLiv.triggered.connect(self.modifier_DetLiv)
        table_menu_DetLiv.addAction(action_modifier_DetLiv)

        action_supprimer_DetLiv= QAction("Supprimer", menu)
        action_supprimer_DetLiv.triggered.connect(self.supprimer_DetLiv)
        table_menu_DetLiv.addAction(action_supprimer_DetLiv)

        action_lister_DetLiv= QAction("Lister", menu)
        action_lister_DetLiv.triggered.connect(self.lister_DetLiv)
        table_menu_DetLiv.addAction(action_lister_DetLiv)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_DetLiv.addAction(action_quitter)

        # Ajouter le menu de la table transporteur au menu principal
        menu.addMenu(table_menu_DetLiv)

        table_menu_Transp = QMenu("transporteur")

        # Options de menu pour la table transporteur
        action_inserer_Transp = QAction("Insérer", menu)
        action_inserer_Transp.triggered.connect(self.insere_Transp)
        table_menu_Transp.addAction(action_inserer_Transp)

        action_modifier_Transp = QAction("Modifier", menu)
        action_modifier_Transp.triggered.connect(self.modifier_Transp)
        table_menu_Transp.addAction(action_modifier_Transp)

        action_supprimer_Transp= QAction("Supprimer", menu)
        action_supprimer_Transp.triggered.connect(self.supprimer_Transp)
        table_menu_Transp.addAction(action_supprimer_Transp)

        action_lister_Transp= QAction("Lister", menu)
        action_lister_Transp.triggered.connect(self.lister_Transp)
        table_menu_Transp.addAction(action_lister_Transp)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_Transp.addAction(action_quitter)

        # Ajouter le menu de la table transporteur au menu principal
        menu.addMenu(table_menu_Transp)

        table_menu_Cli = QMenu("Client")

        # Options de menu pour la table client
        action_inserer_Cli = QAction("Insérer", menu)
        action_inserer_Cli.triggered.connect(self.insere_Cli )
        table_menu_Cli.addAction(action_inserer_Cli)

        action_modifier_Cli = QAction("Modifier", menu)
        action_modifier_Cli.triggered.connect(self.modifier_Cli)
        table_menu_Cli.addAction(action_modifier_Cli)

        action_supprimer_Cli= QAction("Supprimer", menu)
        action_supprimer_Cli.triggered.connect(self.supprimer_Cli)
        table_menu_Cli.addAction(action_supprimer_Cli)

        action_lister_Cli= QAction("Lister", menu)
        action_lister_Cli.triggered.connect(self.lister_Cli)
        table_menu_Cli.addAction(action_lister_Cli)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_Cli.addAction(action_quitter)

        # Ajouter le menu de la table transporteur au menu principal
        menu.addMenu(table_menu_Cli)

        table_menu_Exp = QMenu("Expedition")

        # Options de menu pour la table Expedition
        action_inserer_Exp = QAction("Insérer", menu)
        action_inserer_Exp.triggered.connect(self.insere_Exp )
        table_menu_Exp.addAction(action_inserer_Exp)

        action_modifier_Exp = QAction("Modifier", menu)
        action_modifier_Exp.triggered.connect(self.modifier_Exp)
        table_menu_Exp.addAction(action_modifier_Exp)

        action_supprimer_Exp= QAction("Supprimer", menu)
        action_supprimer_Exp.triggered.connect(self.supprimer_Exp)
        table_menu_Exp.addAction(action_supprimer_Exp)

        action_lister_Exp= QAction("Lister", menu)
        action_lister_Exp.triggered.connect(self.lister_Exp)
        table_menu_Exp.addAction(action_lister_Exp)

        action_quitter = QAction("Quitter", menu)
        action_quitter.triggered.connect(self.quitter)
        table_menu_Exp.addAction(action_quitter)

        # Ajouter le menu de la table Expedition au menu principal
        menu.addMenu(table_menu_Exp)
        # Afficher le menu principal
        menu.exec_()

    def insere_livraison(self):
        dialog = InsertionDialogLiv()
        dialog.exec_()

    def supprimer_livraison(self):
        dialog = SuppressionDialogLiv()
        dialog.exec_()

    def modifier_livraison(self):
        dialog = ModificationDialogLiv()
        dialog.exec_()

    def lister_livraison(self):
        dialog = ListerDialogLiv()
        dialog.exec_()

    def insere_transaction(self):
        cc=InsertionDialogTran()
        cc.exec_()

    def supprimer_transaction(self):
        cc=SuppressionDialogTran()
        cc.exec_()

    def modifier_transaction(self):
        cc=ModificationDialogTran()
        cc.exec_()
    
    def lister_transaction(self):
        cc=ListerDialogTran()
        cc.exec_()

    def insere_DetLiv(self):
        yy=InsertionDialogDetailLiv()
        yy.exec_()

    def modifier_DetLiv(self):
        yy=ModificationDialogDetailLiv()
        yy.exec_()

    def supprimer_DetLiv(self):
        yy=SuppressionDialogDetailLiv()
        yy.exec_()

    def lister_DetLiv(self):
        yy=ListerDialogDetailLiv()
        yy.exec_()
    
    def insere_Transp(self):
        tt=InsertionDialogTransp()
        tt.exec_()

    def modifier_Transp(self):
        tt=ModificationDialogTransp()
        tt.exec_()

    def supprimer_Transp(self):
        tt=SuppressionDialogTransp()
        tt.exec_()

    def lister_Transp(self):
        tt=ListerDialogTransp()
        tt.exec_()

    def insere_Cli(self):
        lll=InsertionDialogCli()
        lll.exec_()

    def modifier_Cli(self):
        lll=ModificationDialogCli()
        lll.exec_()

    def supprimer_Cli(self):
        lll=SuppressionDialogCli()
        lll.exec_()

    def lister_Cli(self):
        lll=ListerDialogDetailCli()
        lll.exec_()

    def insere_Exp(self):
        ee=InsertionDialogExp()
        ee.exec_()

    def modifier_Exp(self):
        ee=ModificationDialogExp()
        ee.exec_()

    def supprimer_Exp(self):
        ee=SuppressionDialogExp()
        ee.exec_()

    def lister_Exp(self):
        ee=ListerDialogExp()
        ee.exec_()

    def quitter(self):
        sys.exit()


#///////////       
class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Bouton Gestion Produit
        bouton_gestion_produit = QPushButton("Gestion Produit")
        bouton_gestion_produit.clicked.connect(self.show_gestion_produit)
        layout.addWidget(bouton_gestion_produit)

        # Bouton Gestion Commande
        bouton_gestion_commande = QPushButton("Gestion Commande")
        bouton_gestion_commande.clicked.connect(self.show_gestion_commande)
        layout.addWidget(bouton_gestion_commande)

        # Bouton Gestion Stock
        bouton_gestion_stock = QPushButton("Gestion Stock")
        bouton_gestion_stock.clicked.connect(self.show_gestion_stock)
        layout.addWidget(bouton_gestion_stock)

        # Bouton Gestion Livraison
        bouton_gestion_livraison = QPushButton("Gestion Livraison")
        bouton_gestion_livraison.clicked.connect(self.show_gestion_livraison)
        layout.addWidget(bouton_gestion_livraison)


        # Bouton supplémentaire
        bouton_supplementaire = QPushButton("QUITTER LE PROGRAMME")
        bouton_supplementaire.clicked.connect(self.close)
        layout.addWidget(bouton_supplementaire)

        # Configurer le layout dans la fenêtre
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_gestion_produit(self):
        self.fenetre_produit = Gestion_produit()
        self.fenetre_produit.show()

    def show_gestion_commande(self):
        self.fenetre_commande = Gestion_commande()
        self.fenetre_commande.show()

    def show_gestion_stock(self):
        self.fenetre_stock = Gestion_stock()
        self.fenetre_stock.show()
    
    def show_gestion_livraison(self):
        self.fenetre_livraison = Gestion_livraison()
        self.fenetre_livraison.show()


def main():
    app = QApplication(sys.argv)
    fenetre = MenuPrincipal()
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
