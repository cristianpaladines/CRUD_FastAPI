from typing import Optional
from pydantic import BaseModel, Field


class MovieGenre(BaseModel):
        movie_id: int = Field(ge=1)
        gen_id: int = Field(ge=1,le=100)

        class Config:
            schema_extra = {
                "example":{
                    "movie_id": 2,
                    "gen_id":1
                }
            }
