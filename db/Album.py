from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class Album(Base):
    __tablename__ = 'albums'
    uid = Column(String(32), primary_key=True)
    title = Column(String)
    duration = Column(Integer)
    artist_id = Column(ForeignKey('artists.uid'))
    extra_metadata = Column(String)

    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")


