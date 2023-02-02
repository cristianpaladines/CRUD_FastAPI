from models.genres import Genres as GenresModel

class GenresService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_genres(self) -> GenresModel:
        result = self.db.query(GenresModel).all()
        return result
    
    def create_genre(self, genre:GenresModel):
        new_genre = GenresModel(
            gen_title = genre.gen_title
        )
        self.db.add(new_genre)
        self.db.commit()
        return
    