from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)  # texto corto
    body = models.TextField()  # texto largo
    date = models.DateField()  # fecha de la noticia

    def __str__(self):
        return self.headline
