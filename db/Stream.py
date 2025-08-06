from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from db import Base


class Stream(Base):
    __tablename__ = 'streams'
    uid = Column(String, primary_key=True)
    timestamp = Column(Integer)
    track = Column(ForeignKey('tracks.uid'))
    extra_metadata = Column(String)


