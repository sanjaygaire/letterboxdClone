from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    watched= models.BooleanField(default=False)


    def __str__(self):
        return self.name
