import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 350, 150)
        self.setWindowTitle("QPushButton Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создание и расположение виджетов в главном окне."""
        self.times_pressed = 0

        self.name_label = QLabel("        Не нажимайте кнопку.        ", self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30)

        self.button = QPushButton("Нажми меня", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """Обработка нажатия на кнопку. Демонстрирует, как изменить текст для виджетов,
        обновлять их размеры и расположение, а также как закрывать окно в результате
        событий."""
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Почему ты надавил на меня?")
        if self.times_pressed == 2:
            self.name_label.setText("Я предупреждаю вас.")
            self.button.setText("Почувствовал себя счастливчиком?")
            self.button.adjustSize()
            self.button.move(60, 70)
        if self.times_pressed == 3:
            print("Окно было закрыто.")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
