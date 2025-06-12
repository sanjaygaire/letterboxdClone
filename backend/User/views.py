from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Profile, Movie, Review, Comment, Watchlist
from .serializers import ProfileSerializer, MovieSerializer, ReviewSerializer, CommentSerializer, WatchlistSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        profile_serializer = ProfileSerializer(data=request.data, context={'request': request})
        if profile_serializer.is_valid():
            profile_serializer.save(user=user)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        user.delete()
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def current_user_profile(request):
    profile = request.user.profile
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_public=True)
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def toggle_like(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    like_dislike, created = ReviewLikeDislike.objects.get_or_create(
        user=request.user, review=review, defaults={'like': True}
    )
    if not created:
        if like_dislike.like:
            like_dislike.delete()
        else:
            like_dislike.like = True
            like_dislike.save()
    return Response({'status': 'like toggled'})

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(review_id=self.kwargs['review_id'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, review_id=self.kwargs['review_id'])

class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)