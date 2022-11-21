from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:admin@db/squad_test")

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()