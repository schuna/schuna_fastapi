from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class InBody(Base):
    __tablename__ = "inbodies"
    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    fat_rate = Column(Float)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates='inbodies', lazy="joined")

