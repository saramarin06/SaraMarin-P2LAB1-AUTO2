from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construir la ruta al archivo JSON
        # Nota: la consola está ubicada en la carpeta base del proyecto
        json_file_path = 'movie/management/commands/movies.json'

        # Cargar datos desde el archivo JSON con utf-8
        with open(json_file_path, 'r', encoding='utf-8') as file:
            movies = json.load(file)

        # Agregar películas a la base de datos
        for i in range(102):  # Se asume que hay 100 películas en el JSON
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()  # Evita duplicados
            if not exist:
                Movie.objects.create(
                    title=movie.get('title', 'Title is null'),
                    image='movie/images/default.png',  # Imagen por defecto
                    genre=movie.get('genre', 'Genre is null'),
                    year=movie.get('year', 'Year is null'),
                    description=movie.get('plot', 'No description available.'),
                )






               