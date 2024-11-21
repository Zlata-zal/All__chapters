from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from main import create_hero, read_heroes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wacanda Heroes")

        layout = QVBoxLayout()

        # Поля ввода
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя героя")
        self.power_input = QLineEdit()
        self.power_input.setPlaceholderText("Сила героя")
        self.rank_input = QLineEdit()
        self.rank_input.setPlaceholderText("Ранг героя")

        # Кнопки
        self.add_button = QPushButton("Добавить героя")
        self.add_button.clicked.connect(self.add_hero)

        self.show_button = QPushButton("Показать всех героев")
        self.show_button.clicked.connect(self.show_heroes)

        # Вывод
        self.result_label = QLabel()

        layout.addWidget(self.name_input)
        layout.addWidget(self.power_input)
        layout.addWidget(self.rank_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.show_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_hero(self):
        name = self.name_input.text()
        power = self.power_input.text()
        rank = int(self.rank_input.text())
        hero = create_hero(name, power, rank)
        self.result_label.setText(f"Герой {hero.name} добавлен!")

    def show_heroes(self):
        heroes = read_heroes()
        self.result_label.setText("\n".join([f"{hero.id}: {hero.name} - {hero.power}" for hero in heroes]))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
