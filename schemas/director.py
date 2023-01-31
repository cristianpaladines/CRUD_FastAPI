from typing import Optional
from pydantic import BaseModel, Field


class Director(BaseModel):
        id: Optional[int] = None
        dir_fname: str = Field(max_length=25,min_length=3)
        dir_lname : str = Field(max_length=25,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "dir_fname": "Nombre Director",
                    "dir_lname":"Apellido Director"
                }
            }
