from sqlalchemy import Column, ForeignKey, Integer, String, Float

from config.database import Base


class Rating(Base):

    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    #reviewer_id = Column(Integer, ForeignKey("reviewer.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    rev_starts = Column(Integer)
    num_o_rating = Column(Integer)

