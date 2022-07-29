from app.dao.directors import DirectorsDAO
from app.dao.genres import GenresDAO
from app.dao.movies import MoviesDAO
from app.service.directors import DirectorsService
from app.service.genres import GenresService
from app.service.movies import MoviesService
from app.setup_db import db

directors_dao = DirectorsDAO(db.session)  # Создаём объект доступа к данным режиссёров
directors_service = DirectorsService(dao=directors_dao)  # Создаём сервис режиссёров

genres_dao = GenresDAO(db.session)  # Создаём объект доступа к данным жанров
genres_service = GenresService(dao=genres_dao)  # Создаём сервис жанров

movies_dao = MoviesDAO(db.session)  # Создаём объект доступа к данным фильмов
movies_service = MoviesService(dao=movies_dao)  # Создаём сервис фильмов
