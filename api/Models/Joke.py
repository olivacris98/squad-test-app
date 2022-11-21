from ..Databases.db import Base, engine
from sqlalchemy import Column, Integer, String


class JokeModel(Base):
    __tablename__ = 'joke'

    number = Column(Integer, primary_key=True)
    joke = Column(String(155))
    active = Column(Integer, default=str(1))

    def __init__(self, **kwargs):
        self.joke = kwargs["joke"]


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
