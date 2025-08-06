from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base


class Stream(Base):
    __tablename__ = 'streams'
    uid = Column(String(32), primary_key=True)
    timestamp = Column(Integer)
    streamed_ms = Column(Integer)
    reason_stream_start = Column(String(32))
    reason_stream_end = Column(String(32))
    shuffle = Column(Boolean)
    skipped = Column(Boolean)
    offline = Column(Boolean)
    offline_ts = Column(Integer)
    streamed_in_incognito = Column(Boolean)
    track_id = Column(ForeignKey('tracks.uid'))
    extra_metadata = Column(Text)

    track = relationship("Track", back_populates="streams")


