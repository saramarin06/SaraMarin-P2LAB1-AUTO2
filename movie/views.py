from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies= Movie.objects.filter(title__icontains= searchTerm)
    else: 
        movies= Movie.objects.all()
    return render(request, "home.html", {"searchTerm": searchTerm, "movies": movies} )
def about(request): 
    #return HttpResponse("<h1>This is the About Page<h1>")
    return render(request, "about.html")
    

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

def statistics_view(request):
    matplotlib.use('Agg')
    # Obtener todas las películas
    all_movies = Movie.objects.all()
    # Crear un diccionario para almacenar la cantidad de películas por año
    movie_counts_by_year = {}
    # Filtrar las películas por año y contar la cantidad de películas por año
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1
    # Ancho de las barras
    bar_width = 0.5
    # Posiciones de las barras
    bar_positions = range(len(movie_counts_by_year))
    # Crear la gráfica de barras
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    # Personalizar la gráfica
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    # Ajustar el espaciado entre las barras
    plt.subplots_adjust(bottom=0.3)
    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    # Convertir la gráfica a base64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    # Ahora crear gráfica por género (usar sólo el primer género si hay varios separados por comas)
    genre_counts = {}
    for movie in all_movies:
        genre_field = movie.genre or ''
        # tomar primer género antes de una coma
        first_genre = genre_field.split(',')[0].strip() if genre_field else 'Unknown'
        if first_genre:
            genre_counts[first_genre] = genre_counts.get(first_genre, 0) + 1

    # Crear figura para género
    plt.figure()
    bar_positions = range(len(genre_counts))
    plt.bar(bar_positions, genre_counts.values(), align='center')
    plt.title('Movies per genre (first genre)')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, genre_counts.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.35)

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.close()
    image_png2 = buffer2.getvalue()
    buffer2.close()
    graphic_genre = base64.b64encode(image_png2).decode('utf-8')

    # Renderizar la plantilla statistics.html con ambas gráficas
    return render(request, 'statistics.html', {'graphic': graphic, 'graphic_genre': graphic_genre})

def signup(request):
    email = request.GET.get("email")
    if email:
        # Aquí podrías agregar lógica para guardar el email en una base de datos o enviarlo a un servicio de mailing
        message = f"Thank you for signing up with the email: {email}"
    else:
        message = "Please provide a valid email address."
    return render(request, "signup.html", {"message": message})


