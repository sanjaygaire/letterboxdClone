# user/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import CustomUser, Movie, Review, LikeDislike, Comment, Watchlist, Watched
from .serializers import UserSerializer, ReviewSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class AddToWatchlist(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        movie_id = request.data.get('movie_id')

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        Watchlist.objects.get_or_create(user=user, movie=movie)
        return Response(status=status.HTTP_201_CREATED)


class MarkAsWatched(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        movie_id = request.data.get('movie_id')

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        Watched.objects.get_or_create(user=user, movie=movie)
        return Response(status=status.HTTP_201_CREATED)


class CreateReview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        movie_id = request.data.get('movie_id')
        content = request.data.get('content')
        rating = request.data.get('rating')
        public = request.data.get('public', False)

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

        review = Review.objects.create(
            user=user,
            movie=movie,
            content=content,
            rating=rating,
            public=public
        )
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)