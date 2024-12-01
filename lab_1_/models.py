from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine

# Создание базового класса для моделей
Base = declarative_base()

# Модель для таблицы directors
class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    uid = Column(String, unique=True)
    department = Column(String)

    # Связь с таблицей movies
    movies = relationship("Movie", back_populates="director")

    def __repr__(self):
        return f"<Director(id={self.id}, name={self.name}, department={self.department})>"

# Модель для таблицы movies
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    original_title = Column(String, nullable=False)
    budget = Column(Integer)
    popularity = Column(Float)
    release_date = Column(Date)
    revenue = Column(Integer)
    title = Column(String)
    vote_average = Column(Float)
    vote_count = Column(Integer)
    overview = Column(String)
    tagline = Column(String)
    uid = Column(String, unique=True)
    director_id = Column(Integer, ForeignKey("directors.id"))

    # Связь с таблицей directors
    director = relationship("Director", back_populates="movies")

    def __repr__(self):
        return f"<Movie(id={self.id}, title={self.title}, director_id={self.director_id})>"

# Настройка базы данных
DATABASE_PATH = "movies.sqlite"
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Добавление данных в базу (только если база пуста)
if session.query(Director).count() == 0 and session.query(Movie).count() == 0:
    # Пример данных для directors
    director1 = Director(name="Christopher Nolan", gender="Male", uid="d1", department="Directing")
    director2 = Director(name="Patty Jenkins", gender="Female", uid="d2", department="Directing")

    # Пример данных для movies
    movie1 = Movie(original_title="Inception", budget=160000000, popularity=82.0,
                   release_date="2010-07-16", revenue=829895144, title="Inception",
                   vote_average=8.8, vote_count=22186, overview="A mind-bending thriller",
                   tagline="Your mind is the scene of the crime", uid="m1", director=director1)
    movie2 = Movie(original_title="Wonder Woman", budget=149000000, popularity=75.0,
                   release_date="2017-06-02", revenue=821847012, title="Wonder Woman",
                   vote_average=7.4, vote_count=17045, overview="The story of Diana Prince",
                   tagline="Power. Grace. Wisdom. Wonder.", uid="m2", director=director2)

    # Добавление в сессию и сохранение
    session.add_all([director1, director2, movie1, movie2])
    session.commit()

# Запрос данных из базы
print("\nСписок всех фильмов и их режиссеров:")
movies = session.query(Movie).all()
for movie in movies:
    print(f"{movie.title} - Режиссер: {movie.director.name}")

print("\nСписок всех режиссеров и их фильмов:")
directors = session.query(Director).all()
for director in directors:
    print(f"{director.name}: {[movie.title for movie in director.movies]}")
