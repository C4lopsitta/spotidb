from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, select, func
from sqlalchemy.orm import relationship

from db import Base


class Track(Base):
    __tablename__ = 'tracks'
    uid = Column(String(32), primary_key=True)
    title = Column(String(2048))
    duration = Column(Integer)
    album_id = Column(ForeignKey('albums.uid'))
    spotify_track_uri = Column(String(64))
    extra_metadata = Column(Text)

    album = relationship("Album", back_populates="tracks")
    streams = relationship("Stream", back_populates="track")

    def __eq__(self, other):
        return (self.title.lower() == other.title.lower()) and (self.album_id == other.album_id)

    def __hash__(self):
        return hash((self.title.lower(), self.album_id))

    @staticmethod
    def get_track(session, name: str, album_uid: str):
        query = select(Track).where(func.lower(Track.title) == name.lower()).where(Track.album_id == album_uid)
        result = session.execute(query).scalar()
        return result
