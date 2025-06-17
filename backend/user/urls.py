# user/urls.py

from django.urls import path
from .views import RegisterView, LoginView, AddToWatchlist, MarkAsWatched, CreateReview

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('watchlist/add/', AddToWatchlist.as_view(), name='add_watchlist'),
    path('watched/add/', MarkAsWatched.as_view(), name='mark_watched'),
    path('review/create/', CreateReview.as_view(), name='create_review'),
]