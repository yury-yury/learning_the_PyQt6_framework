import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 200, 250, 250)
        self.setWindowTitle('Пример QLabel')

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте QLabel для отображения в главном окне."""
        hello_label = QLabel(self)
        hello_label.setText("Прювет!")
        hello_label.move(105, 15)  # размещаем виджет в окне с абс координатами
        image = "images/world.png"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)  # размещаем виджет в окне с абс координатами
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
