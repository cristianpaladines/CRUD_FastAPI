from models.movie_direction import MovieDirection as MovieDirectionModel


class MovieDirectionService():
    
    def __init__(self, db) -> None:
        self.db = db
    
    # def get_movie_direction(self, id_)