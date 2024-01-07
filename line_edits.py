import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setMaximumSize(310, 130)
        self.setWindowTitle("Пример QLineEdit")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте и расположите виджеты в главном окне."""
        QLabel("Пожалуйста, введите ваше имя ниже.", self).move(70, 10)

        name_label = QLabel("Имя:", self)
        name_label.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50)

        clear_button = QPushButton("Clear", self)
        clear_button.move(140, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton("OK", self)
        accept_button.move(210, 90)
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        """Очистить поле ввода QLineEdit."""
        self.name_edit.clear()

    def acceptText(self):
        """Принять ввод пользователя в виджете QLineEdit и закрыть программу."""
        print(self.name_edit.text())
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
