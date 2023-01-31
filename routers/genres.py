from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from models.genres import Genres as GenresModel

from config.database import Session
from schemas.genre import Genre
from service.genres import GenresService


genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'],status_code=200)
def get_genres():
    db = Session()
    result = db.query(GenresModel).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.get('/genre_for_id',tags=['genres'],status_code=200)
def get_genre_for_id(id:int):
    db = Session()
    result = GenresService(db).get_genre_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.get('/genre_for_title',tags=['genres'],status_code=200)
def get_genre_for_title(genre:str):
    db = Session()
    result = GenresService(db).get_genre_for_title(genre)
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.post('/genre',tags=['genres'],status_code=200)
def post_genre(genre:Genre):
    db = Session()
    GenresService(db).create_genres(genre)
    return JSONResponse(content={'message':'Register genrer correctly','status_code':'200'})


