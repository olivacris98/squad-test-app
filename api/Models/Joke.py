from ..Databases.db import Base
from sqlalchemy import Column, Integer, String


class JokeModel(Base):
    __tablename__ = 'joke'

    number = Column(Integer, primary_key=True)
    joke = Column(String(155))
    active = Column(Integer, default=str(1))

    def __init__(self, **kwargs):
        self.joke = kwargs["joke"]
