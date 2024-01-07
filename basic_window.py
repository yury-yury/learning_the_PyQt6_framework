# Код для создания пустого окна написанный в парадигме ООП
import sys

from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка приложения"""
        self.setGeometry(200, 100, 400, 300)  # Задание расположения окна по x и y и размера по ширине и высоте
        self.setWindowTitle('Пустое окно в PyQt')  # Установка заголовка окна
        self.show()  # Отображение окна на экране


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создание приложения
    window = EmptyWindow()  # Создание экземпляра окна
    sys.exit(app.exec())  # Запуск цикла событий с безопасным выходом.
