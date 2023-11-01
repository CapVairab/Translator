import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QComboBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont,QPixmap,QColor
from PyQt5.QtCore import Qt
from gtts import gTTS
import os

from googletrans import Translator, LANGUAGES

class LanguageTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Techno Builders")
        
        # Load and set the background image
        background_image = QPixmap("V:\melanie-hughes-r5hrXLG_6Ho-unsplash.jpg")  # Replace with your image file
        background_label = QLabel(self)
        background_label.setPixmap(background_image.scaled(1920, 1080))
        background_label.setGeometry(0,0,1920,1080)

        


        # Create labels
        self.label1 = QLabel("Translify", self)
        self.label1.setFont(QFont("Arial", 20))  # Set the font using QFont
        self.label1.setStyleSheet('background-color: steelblue; color: yellow')
        self.label1.setGeometry(10, 10, 400, 40)

        self.label2 = QLabel("Indian Railways", self)
        self.label2.setFont(QFont("Arial", 17))  # Set the font using QFont
        self.label2.setStyleSheet('background-color: steelblue; color: white')
        self.label2.setGeometry(900, 340, 200, 40)

        self.label3 = QLabel("Enter Text", self)
        self.label3.setFont(QFont("Arial", 13))  # Set the font using QFont
        self.label1.setStyleSheet('background-color: steelblue; colour:white')
        self.label3.setGeometry(20, 60, 100, 30)

        self.label4 = QLabel("Output", self)
        self.label4.setFont(QFont("Arial", 20))  # Set the font using QFont
        self.label1.setStyleSheet('background-color: yellow; colour:white')
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
        self.trans_btn.setGeometry(490, 490, 100, 30)
        self.trans_btn.setStyleSheet('background-color: red')
        self.trans_btn.clicked.connect(self.Translate)





    def Translate(self):
        translator = Translator()
        translated = translator.translate(
            text=self.input_text.toPlainText(),
            src=self.src_lang.currentText(),
            dest=self.dest_lang.currentText()
        )
        self.output_text.setPlainText(translated.text)

        # Speak the translated text
        self.speak(translated.text, dest_lang_code="hi")  # Use "bn" for Bengali

    def speak(self, text, dest_lang_code):
        # Create a temporary file to store the voice output
        tts = gTTS(text=text, lang=dest_lang_code.lower())
        tts.save("temp.mp3")

        # Play the voice output
        os.system("start temp.mp3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator_app = LanguageTranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())
