from celery import shared_task
from .models import Movie

@shared_task
def print_movie_count():
    print(f"Total movies: {Movie.objects.count()}")
