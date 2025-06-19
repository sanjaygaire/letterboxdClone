# movie/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewDetail

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]