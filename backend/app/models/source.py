from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    source_type = Column(String(100), nullable=False)
    base_url = Column(String(512), nullable=True)

    evidence = relationship("Evidence", back_populates="source", cascade="all, delete-orphan")
