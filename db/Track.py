from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from db import Base


class Track(Base):
    __tablename__ = 'tracks'
    uid = Column(String, primary_key=True)
    title = Column(String)
    duration = Column(Integer)
    album = Column(ForeignKey('albums.uid'))
    extra_metadata = Column(String)

