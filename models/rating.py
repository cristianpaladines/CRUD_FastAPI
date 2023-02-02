from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from config.database import Base

class Rating(Base):
    
    __tablename__ = "rating"
    
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.id"))
    rev_stars = Column(Float)
    num_o_ratings = Column(Integer)

