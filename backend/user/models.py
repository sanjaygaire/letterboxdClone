from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
import random

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    fav_movies = models.ManyToManyField('movie.Movie', related_name='favored_by', blank=True)
    reviewed_movies = models.ManyToManyField('movie.Movie', related_name='reviewed_by_profiles', blank=True)
    watchlisted_movies = models.ManyToManyField('movie.Movie', related_name='watchlisted_by_profiles', blank=True)

    def __str__(self):
        return self.user.username

class BlacklistedToken(models.Model):
    token = models.TextField()
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token[:20] + "..."

class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)