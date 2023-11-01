import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QComboBox
from PyQt5.QtGui import QFont  # Import QFont

from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1080, 400)
        self.setWindowTitle("Project Gurukul--Language Translator")

        # Create labels
        self.label1 = QLabel("LANGUAGE TRANSLATOR", self)
        self.label1.setFont(QFont("Arial", 20))  # Set the font using QFont
        self.label1.setStyleSheet('background-color: white smoke')
        self.label1.setGeometry(10, 10, 400, 40)

        self.label2 = QLabel("Project Gurukul", self)
        self.label2.setFont(QFont("Arial", 20))  # Set the font using QFont
        self.label2.setStyleSheet('background-color: white smoke')
        self.label2.setGeometry(900, 340, 200, 40)

        self.label3 = QLabel("Enter Text", self)
        self.label3.setFont(QFont("Arial", 13))  # Set the font using QFont
        self.label3.setStyleSheet('background-color: white smoke')
        self.label3.setGeometry(20, 60, 100, 30)

        self.label4 = QLabel("Output", self)
        self.label4.setFont(QFont("Arial", 13))  # Set the font using QFont
        self.label4.setStyleSheet('background-color: white smoke')
        self.label4.setGeometry(780, 60, 100, 30)

        # Create input and output text widgets
        self.input_text = QTextEdit(self)
        self.input_text.setFont(QFont("Arial", 10))  # Set the font using QFont
        self.input_text.setGeometry(30, 100, 540, 240)

        self.output_text = QTextEdit(self)
        self.output_text.setFont(QFont("Arial", 10))  # Set the font using QFont
        self.output_text.setGeometry(600, 100, 540, 240)

        # Create comboboxes for language selection
        self.src_lang = QComboBox(self)
        self.src_lang.addItems(list(LANGUAGES.values()))
        self.src_lang.setGeometry(20, 60, 200, 30)
        self.src_lang.setCurrentText('choose input language')

        self.dest_lang = QComboBox(self)
        self.dest_lang.addItems(list(LANGUAGES.values()))
        self.dest_lang.setGeometry(890, 60, 200, 30)
        self.dest_lang.setCurrentText('choose output language')

        # Create translate button
        self.trans_btn = QPushButton('Translate', self)
        self.trans_btn.setFont(QFont("Arial", 12))  # Set the font using QFont
        self.trans_btn.setGeometry(490, 180, 100, 30)
        self.trans_btn.setStyleSheet('background-color: royalblue')
        self.trans_btn.clicked.connect(self.Translate)

    def Translate(self):
        translator = Translator()
        translated = translator.translate(
            text=self.input_text.toPlainText(),
            src=self.src_lang.currentText(),
            dest=self.dest_lang.currentText()
        )
        self.output_text.setPlainText(translated.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = LanguageTranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
