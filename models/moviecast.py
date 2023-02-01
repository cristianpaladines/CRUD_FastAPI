from sqlalchemy import Column, ForeignKey, Integer, String

from config.database import Base


class MovieCast(Base):

    __tablename__ = "movie_cast"

    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("actor.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    role = Column(String)


