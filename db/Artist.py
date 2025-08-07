from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, func, select
from sqlalchemy.orm import relationship

from db import Base

class Artist(Base):
    __tablename__ = 'artists'
    uid = Column(String(32), primary_key=True)
    name = Column(String(128), unique=True)
    extra_metadata = Column(Text)

    albums = relationship("Album", back_populates="artist")

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name.lower())

    @staticmethod
    def get_artist_by_name(session, name: str):
        query = select(Artist).where(func.lower(Artist.name) == name.lower())
        result = session.execute(query).scalar()
        return result

