import sys

from PyQt5 import QtWidgets


class AddWords:
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

        self.window.setGeometry(50, 50, 1000, 500)
        self.window.setWindowTitle("Добавление слов")

        self.button = QtWidgets.QPushButton(self.window)
        self.button.setText("Hello")

        self.button.move(20, 20)

    def show(self):
        self.window.show()


class MainApp:
    def __init__(self):
        self.main_application = QtWidgets.QApplication(sys.argv)

        self.add_words = AddWords()

    def show_addwords(self):
        self.add_words.show()


def start():
    app = MainApp()
    app.show_addwords()

    sys.exit(app.main_application.exec_())

if __name__ == '__main__':
    start()