from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from service.director import DirectorService
from schemas.director import Director
director_router = APIRouter()

@director_router.get('/directors',tags=['directors'])
def get_directors():
    db = Session()
    result = DirectorService(db).get_directors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@director_router.post('/director',tags=['directors'],status_code=201)
def create_director(director:Director):
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'message':'director save in data base'})