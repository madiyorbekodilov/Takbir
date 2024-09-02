from sqlalchemy import create_engine, Column, Integer, String, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://takbir_owner:hBNHsClP34TZ@ep-billowing-resonance-a10xp96h.ap-southeast-1.aws.neon.tech/takbir?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    tg_id = Column(BIGINT)
    total_count = Column(Integer)
    total_coin = Column(Integer)
    channels = Column(Text)
    share_link = Column(String)


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    url = Column(String)
    chat_id = Column(BIGINT)


class Friend(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BIGINT)
    friend_tg_id = Column(BIGINT)


class Daraja(Base):
    __tablename__ = "daraja"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    daraja = Column(Integer)
    started_at = Column(Integer)
    limit = Column(Integer)
