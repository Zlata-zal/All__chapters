from PyQt5 import QtWidgets
import sqlite3
import sys

class MovieApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MovieApp, self).__init__()
        self.setWindowTitle("Movie Management App")

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QGridLayout(self.central_widget)

        # Поля ввода
        self.title_input = QtWidgets.QLineEdit()
        self.title_input.setPlaceholderText("Title")
        layout.addWidget(self.title_input, 0, 0)

        self.budget_input = QtWidgets.QLineEdit()
        self.budget_input.setPlaceholderText("Budget")
        layout.addWidget(self.budget_input, 0, 1)

        self.director_id_input = QtWidgets.QLineEdit()
        self.director_id_input.setPlaceholderText("Director ID")
        layout.addWidget(self.director_id_input, 0, 2)

        # Кнопка создания фильма
        self.create_movie_btn = QtWidgets.QPushButton("Create Movie")
        self.create_movie_btn.clicked.connect(self.create_movie)
        layout.addWidget(self.create_movie_btn, 0, 3)

        # Список фильмов
        self.movie_list = QtWidgets.QListWidget()
        layout.addWidget(self.movie_list, 1, 0, 1, 4)

        # Кнопка обновления списка
        self.update_list_btn = QtWidgets.QPushButton("Refresh Movie List")
        self.update_list_btn.clicked.connect(self.load_movies)
        layout.addWidget(self.update_list_btn, 2, 0, 1, 4)

        # Подключение к базе данных
        self.conn = sqlite3.connect("movies.sqlite")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.load_movies()

    def create_table(self):
        """Создает таблицу в базе данных, если её нет"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                budget INTEGER NOT NULL,
                director_id INTEGER NOT NULL
            )
        """)
        self.conn.commit()
    def create_movie(self):
        """Создает новый фильм и добавляет его в базу данных"""
        title = self.title_input.text()
        budget = self.budget_input.text()
        director_id = self.director_id_input.text()

        try:
            budget = int(budget)
            director_id = int(director_id)

            self.cursor.execute("""
                INSERT INTO movies (title, budget, director_id)
                VALUES (?, ?, ?)
            """, (title, budget, director_id))
            self.conn.commit()

            QtWidgets.QMessageBox.information(self, "Success", f"Movie '{title}' created successfully!")
            self.load_movies()
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Error", "Budget and Director ID must be integers!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def load_movies(self):
        """Загружает список фильмов из базы данных"""
        self.movie_list.clear()
        self.cursor.execute("SELECT title, budget, director_id FROM movies")
        movies = self.cursor.fetchall()

        for movie in movies:
            title, budget, director_id = movie
            self.movie_list.addItem(f"{title} - ${budget} - Director ID: {director_id}")

    def closeEvent(self, event):
        """Закрываем соединение с базой данных при выходе"""
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())






