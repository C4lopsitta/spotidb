from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Stream(Base):
    __tablename__ = 'streams'
    uid = Column(String(32), primary_key=True)
    timestamp = Column(Integer)
    streamed_ms = Column(Integer)
    reason_stream_start = Column(String)
    reason_stream_end = Column(String)
    shuffle = Column(Boolean)
    skipped = Column(Boolean)
    offline = Column(Boolean)
    offline_ts = Column(Integer)
    streamed_in_incognito = Column(Boolean)
    track_id = Column(ForeignKey('tracks.uid'))
    extra_metadata = Column(String)

    track = relationship("Track", back_populates="streams")


