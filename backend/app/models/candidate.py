from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

def utc_now():
    return datetime.now(timezone.utc)

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    investigation_id = Column(Integer, ForeignKey("investigations.id"), nullable=False)
    display_name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=True)
    organization = Column(String(255), nullable=True)
    profile_url = Column(String(512), nullable=True)
    created_at = Column(DateTime, default=utc_now, nullable=False)

    investigation = relationship("Investigation", back_populates="candidates")
    evidence = relationship("Evidence", back_populates="candidate", cascade="all, delete-orphan")
