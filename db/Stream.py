import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Text, select
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
    offline_ts = Column(sqlalchemy.BigInteger)
    streamed_in_incognito = Column(Boolean)
    track_id = Column(ForeignKey('tracks.uid'))
    extra_metadata = Column(Text)

    track = relationship("Track", back_populates="streams")

    def __eq__(self, other):
        return (self.track_id == other.track_id) and (self.timestamp == other.timestamp)

    def __hash__(self):
        return hash((self.track_id, self.timestamp))

    @staticmethod
    def get_stream_by_ts(session, ts: int):
        query = select(Stream).where(Stream.timestamp == ts)
        result = session.execute(query).scalar()
        return result


