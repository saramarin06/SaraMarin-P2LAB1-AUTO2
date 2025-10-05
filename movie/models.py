from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250, null=True)
    # store images under MEDIA_ROOT/movie/images/ and use the existing default image filename
    image = models.ImageField(upload_to = "movie/images/", default='movie/images/default.png')
    url = models.URLField(blank= True, null= True)
    genre= models.CharField(blank= True, max_length=250, null= True)
    year= models.IntegerField(blank= True, null=True)

    def __str__(self):
        return self.title