import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base

class Album(Base):
    __tablename__ = 'albums'
    uid = Column(String(32), primary_key=True)
    title = Column(String(128))
    duration = Column(Integer)
    artist_id = Column(ForeignKey('artists.uid'))
    extra_metadata = Column(Text)

    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")


