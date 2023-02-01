from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class MovieDirector(Base):

    __tablename__ = "movie_director"
    
    director_id = Column(Integer, ForeignKey("director.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
