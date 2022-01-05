from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QComboBox, QTextEdit, QMessageBox
from PyQt6 import uic
import sys
import googletrans
import textblob


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("translate.ui", self)
        self.setWindowTitle("Translator App")

        # Define our widgets
        self.t_button = self.findChild(QPushButton, "pushButton")
        self.c_button = self.findChild(QPushButton, "pushButton_2")

        self.combo_1 = self.findChild(QComboBox, "comboBox")
        self.combo_2 = self.findChild(QComboBox, "comboBox_2")

        self.text_1 = self.findChild(QTextEdit, "textEdit")
        self.text_2 = self.findChild(QTextEdit, "textEdit_2")

        # Click the buttons
        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)



        # Show The App
        self.show()

    def clear(self):
        pass

    def translate(self):
        pass

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()

