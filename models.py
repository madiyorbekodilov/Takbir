from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:194853@localhost:5432/salom"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    tg_id = Column(Integer)
    total_count = Column(Integer)
    share_link = Column(String)

class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    url = Column(String)

class Friend(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    friend_tg_id = Column(Integer)

class Daraja(Base):
    __tablename__ = "daraja"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    daraja = Column(Integer)
    started_at = Column(Integer)
    limit = Column(Integer)

