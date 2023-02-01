from models.rating import Rating as RatingModel

class RatingService():

    def __init__(self,db) -> None:
        self.db = db

    def get_ratings(self):
        return self.db.query(RatingModel).all()

    def create_rating(self,rating:RatingModel):
        new_rating = RatingModel(
            #reviewer_id = rating.reviewer_id,
            movie_id = rating.movie_id,
            rev_starts = rating.rev_starts,
            num_o_rating = rating.num_o_rating
        )
        self.db.add(new_rating)
        self.db.commit()
        return