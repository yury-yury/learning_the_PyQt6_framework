import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(150, 150, 250, 450)
        self.setWindowTitle('User profile')
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = ["images/skyblue.png", "images/profile_image.png"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/profile_image.png":
                        label.move(80, 20)
            except FileNotFoundError as error:
                    print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Иван Драго")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(50, 140)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText("Я инженер-программист\nс 10-летним опытом создания\n потрясающего кода.")
        about_label.setWordWrap(True)
        about_label.move(15, 195)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 250)

        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 275)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 300)

        developer_label = QLabel(self)
        developer_label.setText("Python Разработчик")
        developer_label.move(15, 325)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2011 - настоящее время")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 340)

        driver_label = QLabel(self)
        driver_label.setText("Водитель доставки пиццы")
        driver_label.move(15, 365)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 380)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
