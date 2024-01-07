import sys

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("Пример QCheckBox")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создаем и располагаем виджеты в главном окне."""
        header_label = QLabel("В какие смены вы можете работать? \
        (Пожалуйста, отметьте все, что применимо)", self)
        header_label.setWordWrap(True)
        header_label.move(20, 10)

        # Установите флажки
        morning_cb = QCheckBox("Утро [8 утра-14 дня]", self)
        morning_cb.move(40, 60)
        # morning_cb.toggle() # Удалите комментарий, чтобы начать проверять
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox("День [13 дня - 20 вечера]", self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox("Ночь [19 вечера-3 утра]", self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        """Печатать текст объекта QCheckBox, когда он выбран
        или отменен. Используйте sender(), чтобы определить, какой виджет
        посылает сигнал."""
        sender = self.sender()
        if checked:
            print(f"{sender.text()} Выбран.")
        else:
            print(f"{sender.text()} Не выбран.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())