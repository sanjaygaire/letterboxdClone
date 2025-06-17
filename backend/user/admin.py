# user/admin.py

from django.contrib import admin
from .models import CustomUser, Movie, Review, LikeDislike, Comment, Watchlist, Watched

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(LikeDislike)
admin.site.register(Comment)
admin.site.register(Watchlist)
admin.site.register(Watched)