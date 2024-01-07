# Код для создания пустого окна написанный в процедурном стиле
import sys

from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)  # Создание экземпляра приложения
window = QWidget()  # Создание окна как экземпляра QWidget
window.setWindowTitle('Пустое окно в PyQt6')
window.setGeometry(400, 400, 400, 300)
window.show()

sys.exit(app.exec())  # Запуск цикла событий
