from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class Artist(Base):
    __tablename__ = 'artists'
    uid = Column(String(32), primary_key=True)
    name = Column(String)
    extra_metadata = Column(String)

    albums = relationship("Album", back_populates="artist")

