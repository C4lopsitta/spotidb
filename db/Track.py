from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Track(Base):
    __tablename__ = 'tracks'
    uid = Column(String(32), primary_key=True)
    title = Column(String)
    duration = Column(Integer)
    album_id = Column(ForeignKey('albums.uid'))
    spotify_track_uri = Column(String)
    extra_metadata = Column(String)

    album = relationship("Album", back_populates="tracks")
    streams = relationship("Stream", back_populates="track")
