from models import session, Movie, Director
from datetime import datetime

# CRUD-функции для таблицы Movie

def create_movie(original_title, budget, popularity, release_date, revenue, title, vote_average, vote_count, overview, tagline, director_id):
    if isinstance(release_date, str):
        release_date = datetime.strptime(release_date, "%Y-%m-%d").date()
    new_movie = Movie(
        original_title=original_title,
        budget=budget,
        popularity=popularity,
        release_date=release_date,
        revenue=revenue,
        title=title,
        vote_average=vote_average,
        vote_count=vote_count,
        overview=overview,
        tagline=tagline,
        director_id=director_id
    )
    session.add(new_movie)
    session.commit()
    return new_movie

def read_movies():
    return session.query(Movie).all()

def update_movie(movie_id, **kwargs):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        for key, value in kwargs.items():
            if hasattr(movie, key):
                setattr(movie, key, value)
        session.commit()
        return movie
    return None

def delete_movie(movie_id):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        return True
    return False

# CRUD-функции для таблицы Director (опционально)
def create_director(name, gender, uid, department):
    new_director = Director(
        name=name,
        gender=gender,
        uid=uid,
        department=department
    )
    session.add(new_director)
    session.commit()
    return new_director

def read_directors():
    return session.query(Director).all()


if __name__ == "__main__":
    # Пример создания режиссера
    director = create_director(name="Ryan Coogler", gender="Male", uid="d3", department="Directing")
    print(f"Создан режиссер: {director}")

    # Пример создания фильма
    movie = create_movie(
        original_title="Black Panther",
        budget=200000000,
        popularity=85.0,
        release_date="2018-02-16",
        revenue=1346913161,
        title="Black Panther",
        vote_average=7.3,
        vote_count=16000,
        overview="King T'Challa returns home to Wakanda to take his place as king.",
        tagline="Long live the king.",
        director_id=director.id
    )
    print(f"Создан фильм: {movie}")

    # Чтение всех фильмов
    movies = read_movies()
    print(f"Все фильмы: {movies}")

    # Обновление фильма
    updated_movie = update_movie(movie_id=movie.id, budget=210000000, tagline="Wakanda Forever.")
    print(f"Обновлён фильм: {updated_movie}")

    # Удаление фильма
    if delete_movie(movie_id=movie.id):
        print("Фильм удалён.")
    else:
        print("Фильм не найден.")

