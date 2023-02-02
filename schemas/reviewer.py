from typing import Optional
from pydantic import BaseModel, Field


class Reviewer(BaseModel):
    id: Optional[int] = None
    rev_name: str = Field(max_length=20,min_length=3)
    
    class Config:
        schema_extra = {
            "example":{
                "rev_name": "Flagrant Baronessa"
            }
        }
