# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Routes
    path('api/user/', include('user.urls')),     # /api/user/register, /api/user/logout
    path('api/movie/', include('movie.urls')),   # /api/movie/movies/, /api/movie/reviews/<id>
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)