from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Fix movie image paths that point to movie/images/default.jpg to default.png'

    def handle(self, *args, **kwargs):
        qs = Movie.objects.filter(image='movie/images/default.jpg')
        updated = qs.update(image='movie/images/default.png')
        self.stdout.write(self.style.SUCCESS(f'Updated {updated} movie records'))
