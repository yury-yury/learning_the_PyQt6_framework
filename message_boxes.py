import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit, QPushButton
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("Пример QMessageBox")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создайте и расположите виджеты в главном окне."""
        catalog_label = QLabel("Каталог авторов", self)
        catalog_label.move(100, 10)
        catalog_label.setFont(QFont("Arial", 18))

        search_label = QLabel("Поиск автора в индексе:", self)
        search_label.move(20, 40)

        # Создайте виджеты QLabel и QLineEdit автора
        author_label = QLabel("Имя:", self)
        author_label.move(20, 74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText("Введите имя как: Имя Фамилия")

        # Создание поисковой кнопки QPushButton
        search_button = QPushButton("Поиск", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

    def searchAuthors(self):
        """Поиск по каталогу имен.
        Если имя найдено, выведите диалог "Автор найден".
        В противном случае выведите диалог "Автор не найден"."""

        file = "files/authors.txt"
        try:
            with open(file, "r") as f:
                authors = [line.rstrip("\n") for line in f]
        # Проверка наличия имени в списке авторов
            if self.author_edit.text() in authors:
                QMessageBox.information(self, "Автор найден", "Автор найден в каталоге!", QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self,
                                      "Автор не найден",
                                      """<p>Автор не найден в каталоге.</p>
                                      <p>Вы хотите продолжить? </p>""",
                                      QMessageBox.StandardButton.Yes | \
                                      QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
                if answer == QMessageBox.StandardButton.No:
                    print("Закрытие приложения.")
                    self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Ошибка",
                            f"""<p>Файл не найден.</p>
        <p>Error: {error}</p>
        Закрытие приложения.""",
                QMessageBox.StandardButton.Ok)
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
