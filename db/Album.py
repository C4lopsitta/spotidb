from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, select, func
from sqlalchemy.orm import relationship
from db import Base

class Album(Base):
    __tablename__ = 'albums'
    uid = Column(String(32), primary_key=True)
    title = Column(String(256))
    artist_id = Column(ForeignKey('artists.uid'))
    extra_metadata = Column(Text)

    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")

    def __eq__(self, other):
        return (self.title.lower() == other.title.lower()) and (self.artist_id == other.artist_id)

    def __hash__(self):
        return hash((self.title.lower(), self.artist_id))

    @staticmethod
    def get_album(session, name: str, artist_uid: str):
        query = select(Album).where(func.lower(Album.title) == name.lower()).where(Album.artist_id == artist_uid)
        result = session.execute(query).scalar()
        return result

