from sqlalchemy import create_engine # Connects to the databse

# SQLAlchemy is ORM which is what our FastAPI application is going to used to be able to create database and be able to create a connection to database and being able to use all database records withing our application.
from sqlalchemy.orm import sessionmaker # Creates Session 
from sqlalchemy.ext.declarative import declarative_base # Used to define models(Tables)

SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'

engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

