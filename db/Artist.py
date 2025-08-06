from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from db import Base

class Artist(Base):
    __tablename__ = 'artists'
    uid = Column(String, primary_key=True)
    name = Column(String)
    extra_metadata = Column(String)

