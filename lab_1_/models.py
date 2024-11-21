from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    power = Column(String)
    rank = Column(Integer)

    def __repr__(self):
        return f"<Hero(id={self.id}, name={self.name}, power={self.power}, rank={self.rank})>"

DATABASE_PATH = "./data/wacanda.sqlite"
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблиц, если их ещё нет
Base.metadata.create_all(engine)