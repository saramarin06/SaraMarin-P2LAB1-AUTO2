from django.shortcuts import render

# Create your views here.
from .models import News

def news(request):
    # Consulta todas las noticias, ordenadas por fecha descendente
    newss = News.objects.all().order_by('-date')
    
    # Renderiza(crear imagen final) el template 'news.html' y le pasa la lista de noticias
    return render(request, 'news.html', {'newss': newss})
