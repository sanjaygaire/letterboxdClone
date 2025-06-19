import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr='lte')
    title = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'min_rating', 'max_rating']