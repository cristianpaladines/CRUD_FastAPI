from typing import Optional
from pydantic import BaseModel, Field


class Genre(BaseModel):
        id_movie: Optional[int] = None
        gen_title: str = Field(max_length=30,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "gen_title": "Action"
                }
            }
