from PyQt5 import QtWidgets, uic
from models import session, Movie, Director
from datetime import datetime
from main import create_movie, read_movies, update_movie, delete_movie, create_director, read_directors
class MovieApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MovieApp, self).__init__()
        self.setWindowTitle("Movie Management App")

        self.central_widget = QtWidgets.QWidget
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QGridLayout(self.central_widget)

        self.title_input = QtWidgets.QLineEdit
        self.title_input.setPlaceholderText("Title")
        layout.addWidget(self.title_input, 0, 0)

        self.budget_input = QtWidgets.QLineEdit
        self.budget_input.setPlaceholderText("Budget")
        layout.addWidget(self.budget_input, 0, 1)

        self.director_id_input = QtWidgets.QLineEdit
        self.director_id_input.setPlaceholderText("Director")
        layout.addWidget(self.director_id_input, 0, 2)

        self.create_movie_btn = QtWidgets.QPushButton("Create movie", self)
        self.create_movie_btn.clicked.connect(self.create_movie)
        layout.addWidget(self.create_movie_btn, 0, 3)

        self.movie_list = QtWidgets.QListWidget(self)
        layout.addWidget(self.movie_list, 1, 0, 1, 4)

        self.update_list_btn = QtWidgets.QPushButton("Refresh Movie List", self)
        self.update_list_btn.clicked.connect(self.movie_list)
        layout.addWidget(self.update_list_btn, 2, 0, 1, 4)

        self.load_movies()
    def create_movie(self):
        title = self.title_input.text()
        budget = self.budget_input.text()
        director_id = self.director_id_input.text()
        try:
            budget = int(budget)
            director_id = int(director_id)
            movie = create_movie(
                original_title=title,
                budget=budget,
                popularity=0.0,
                release_date=datetime.now().date(),
                revenue=0,
                title=title,
                vote_average=0.0,
                vote_count=0,
                overview="",
                tagline="",
                director_id=director_id
            )
            QtWidgets.QMessageBox.information(self, "Success", f"Movie '{movie.title}' created successfully!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

            self.load_movies()

        def load_movies(self):
            self.movie_list.clear()
            movies = read_movies()
            for movie in movies:
                self.movie_list.addItem(f"{movie.id}: {movie.title} - {movie.budget}$")
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())




