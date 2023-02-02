from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class MovieDirection (Base):
    
    __tablename__ = "movie_direction"
    
    dir_id = Column(Integer, ForeignKey("director.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    
