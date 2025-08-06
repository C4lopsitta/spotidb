from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base

class Artist(Base):
    __tablename__ = 'artists'
    uid = Column(String(32), primary_key=True)
    name = Column(String(128))
    extra_metadata = Column(Text)

    albums = relationship("Album", back_populates="artist")

