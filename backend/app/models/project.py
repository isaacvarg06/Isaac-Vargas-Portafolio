from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title_es = Column(String(200), nullable=False)
    title_en = Column(String(200), nullable=False)
    description_es = Column(Text, nullable=False)
    description_en = Column(Text, nullable=False)
    github_url = Column(String(500), nullable=False)
    demo_url = Column(String(500), nullable=True)
    technologies = Column(JSON, nullable=False)
    image_url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())