from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from config.database import Base

class Reviewer(Base):
    
    __tablename__ = "reviewer"
    
    id = Column(Integer, primary_key=True, index=True)
    rev_name = Column(String)
    
