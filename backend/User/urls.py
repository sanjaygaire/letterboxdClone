from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, toggle_like, current_user_profile
from .views import MovieViewSet, ReviewViewSet, CommentViewSet, WatchlistViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'watchlist', WatchlistViewSet)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('profile/', current_user_profile, name='profile'),
    path('reviews/<int:review_id>/like/', toggle_like, name='toggle-like'),
    path('reviews/<int:review_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('', include(router.urls)),
]