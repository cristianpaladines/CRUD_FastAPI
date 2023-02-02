from typing import Optional
from pydantic import BaseModel, Field

class MovieDrirection(BaseModel):
    dir_id: int
    movie_id: int
    
    
    class Config:
        schema_extra = {
            "example":{
                "dir_id": "201",
                "movie_id": "901"
            }
        }
