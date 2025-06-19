from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie.views import MovieViewSet, ReviewDetail

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('api/register/', user_views.RegisterView.as_view(), name='register'),
    path('api/verify-email/', user_views.VerifyEmailView.as_view(), name='verify_email'),
    path('api/logout/', user_views.LogoutView.as_view(), name='logout'),
]