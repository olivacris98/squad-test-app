import json
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

connect_url = sqlalchemy.engine.url.URL(
    'mysql+pymysql',
    username="root",
    password="admin",
    host="",
    port=3306,
    database="squad_test")

engine = sqlalchemy.create_engine(connect_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    return Session()


def get_engine():
    return engine
