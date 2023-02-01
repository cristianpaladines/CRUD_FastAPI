from typing import Optional
from pydantic import BaseModel, Field


class Rating(BaseModel):
        movie_id = int
        rev_starts = int
        num_o_rating = int

        class Config:
            schema_extra = {
                "example":{
                    "movie_id ":1,
                    "rev_starts":4,
                    "num_o_rating":9
                }
            }
