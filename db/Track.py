from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base


class Track(Base):
    __tablename__ = 'tracks'
    uid = Column(String(32), primary_key=True)
    title = Column(String(128))
    duration = Column(Integer)
    album_id = Column(ForeignKey('albums.uid'))
    spotify_track_uri = Column(String(128))
    extra_metadata = Column(Text)

    album = relationship("Album", back_populates="tracks")
    streams = relationship("Stream", back_populates="track")
