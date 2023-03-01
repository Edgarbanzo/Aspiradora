# QT Imports
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer, QCoreApplication

# UI Imports
from view.ui_mainwindow import Ui_MainWindow as MainWindow


class MainForm(QMainWindow, MainWindow):

    # Constructor
    def __init__(self):
        # Init UI
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Practica 1 - Aspiradora")
