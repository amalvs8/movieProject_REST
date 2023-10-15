from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " | " + self.director
