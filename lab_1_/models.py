from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine, extract

Base = declarative_base()

class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    uid = Column(String, unique=True)
    department = Column(String)

    movies = relationship("Movie", back_populates="director")

    def __repr__(self):
        return f"<Director(id={self.id}, name={self.name}, department={self.department})>"

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

    director = relationship("Director", back_populates="movies")

    def __repr__(self):
        return f"<Movie(id={self.id}, title={self.title}, director_id={self.director_id})>"

DATABASE_PATH = "movies.sqlite"
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)



if session.query(Director).count() == 0 and session.query(Movie).count() == 0:

    director1 = Director(name="Christopher Nolan", gender="Male", uid="d1", department="Directing")
    director2 = Director(name="Patty Jenkins", gender="Female", uid="d2", department="Directing")
    movie1 = Movie(original_title="Inception", budget=160000000, popularity=82.0,
                   release_date="2010-07-16", revenue=829895144, title="Inception",
                   vote_average=8.8, vote_count=22186, overview="A mind-bending thriller",
                   tagline="Your mind is the scene of the crime", uid="m1", director=director1)
    movie2 = Movie(original_title="Wonder Woman", budget=149000000, popularity=75.0,
                   release_date="2017-06-02", revenue=821847012, title="Wonder Woman",
                   vote_average=7.4, vote_count=17045, overview="The story of Diana Prince",
                   tagline="Power. Grace. Wisdom. Wonder.", uid="m2", director=director2)


    session.add_all([director1, director2, movie1, movie2])
    session.commit()

director_name = input("Введите имя режиссера: ")
director = session.query(Director).filter(Director.name == director_name).first()
quantity = 0
if director:
    for movie in director.movies:
        quantity += 1
    print(f"Режиссер {director_name} снял фильмов: {quantity}")


movies_2014 = session.query(Movie).filter(extract('year', Movie.release_date) == 2014).all()
for movie in movies_2014:
    print(movie.title, movie.release_date.year)


movies = session.query(Movie).filter(Movie.vote_average >= 8.0).all()
for movie in movies:
    print(f"Фильм {movie.title} имеет рейтинг {movie.vote_average}")



print("\nСписок всех фильмов и их режиссеров:")
movies = session.query(Movie).all()
for movie in movies:
    print(f"{movie.title} - Режиссер: {movie.director.name}")

print("\nСписок всех режиссеров и их фильмов:")
directors = session.query(Director).all()
for director in directors:
    print(f"{director.name}: {[movie.title for movie in director.movies]}")
