from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Track(Base):
    __tablename__ = 'tracks'
    uid = Column(String, primary_key=True)
    title = Column(String)
    artist = Column(String)
    album = Column(String)
    extra_metadata = Column(String)

