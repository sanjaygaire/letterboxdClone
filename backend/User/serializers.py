from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Movie, Review, ReviewLikeDislike, Comment, Watchlist, Watched

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    favorite_movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)

    class Meta:
        model = Profile
        fields = ['user', 'name', 'favorite_movies']

    def validate_favorite_movies(self, value):
        if len(value) > 4:
            raise serializers.ValidationError("Maximum 4 favorite movies allowed.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'movie_title', 'content', 'rating', 'is_public', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

class WatchlistSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Watchlist
        fields = ['id', 'movie', 'added_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)