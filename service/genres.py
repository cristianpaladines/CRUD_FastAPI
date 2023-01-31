from models.genres import Genres as GenresModel

class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(GenresModel).all()
        return result

    def get_genre_for_id(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result

    def get_genre_for_title(self,title):
        result = self.db.query(GenresModel).filter(GenresModel.gen_title == title.upper()).all()
        return result

    def create_genres(self,genre:GenresModel):
        new_genre = GenresModel(
            gen_title = genre.gen_title.upper()
        )
        self.db.add(new_genre)
        self.db.commit()
        return



    # def create_actor(self,actor:ActorMoldel):
    #     new_actor = ActorMoldel(
    #     actor_first_name = actor.actor_first_name ,
    #     actor_last_name = actor.actor_last_name,
    #     actor_gender = actor.actor_gender,    
    #     )
    #     self.db.add(new_actor)
    #     self.db.commit()
    #     return