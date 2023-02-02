from typing import Optional
from pydantic import BaseModel, Field


class Rating(BaseModel):
    movie_id: int
    rev_id: int
    rev_stars: float
    num_o_ratings: int
    
    
    class Config:
        schema_extra = {
            "example":{
                "movie_id": "901",
                "rev_id": "9001",
                "rev_stars": "8.40",
                "num_o_ratings": "263575"
            }
        }
