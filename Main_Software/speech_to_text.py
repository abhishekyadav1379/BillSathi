import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
import speech_recognition as sr
import pyttsx3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech to Text")
        self.setGeometry(100, 100, 400, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 20, 360, 200)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(20, 240, 160, 40)
        self.start_button.clicked.connect(self.start_listening)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(220, 240, 160, 40)
        self.stop_button.clicked.connect(self.stop_listening)

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.engine = pyttsx3.init()

    def start_listening(self):
        self.text_edit.clear()
        self.text_edit.setPlaceholderText("Listening...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            recognized_text = self.recognizer.recognize_google(audio)
            self.text_edit.setPlainText(recognized_text)
        except sr.UnknownValueError:
            self.text_edit.setPlainText("Unable to recognize speech")
        except sr.RequestError as e:
            self.text_edit.setPlainText(f"Error: {str(e)}")

    def stop_listening(self):
        self.recognizer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())