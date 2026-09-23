from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

def utc_now():
    return datetime.now(timezone.utc)

class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    url = Column(String(512), nullable=True)
    evidence_strength = Column(String(50), nullable=True)
    verification_status = Column(String(50), default="unverified", nullable=False)
    created_at = Column(DateTime, default=utc_now, nullable=False)

    candidate = relationship("Candidate", back_populates="evidence")
    source = relationship("Source", back_populates="evidence")
