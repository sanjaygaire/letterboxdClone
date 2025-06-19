from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/')
    rating = models.FloatField(default=1.0)

    def save(self, *args, **kwargs):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    review = models.TextField()
    likes = models.IntegerField(default=0)

class Like(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

class List(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    profile = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    is_public = models.BooleanField(default=False)

class WatchList(models.Model):
    profile = models.ForeignKey('user.Profile', on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
