from rest_framework import viewsets, generics
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .filters import MovieFilter
from .permissions import IsReviewOwner

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_class = MovieFilter
    filterset_fields = []

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewOwner]

    def get_queryset(self):
        return Review.objects.filter(profile__user=self.request.user)