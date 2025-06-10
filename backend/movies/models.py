from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
class Movie(models.Mode):

    title = models.CharField(max_length=200)
    description= models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', height_field=None,width_field=None,max_length=None)
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    watched = models.BooleanField(default=False)
    def __str__(self):
        return self.title