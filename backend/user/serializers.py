from rest_framework import serializers
from .models import BlacklistedToken, EmailVerification
from django.contrib.auth import get_user_model

User = get_user_model()

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate_refresh(self, value):
        from rest_framework_simplejwt.exceptions import TokenError
        from rest_framework_simplejwt.tokens import RefreshToken

        try:
            RefreshToken(value)
        except TokenError:
            raise serializers.ValidationError("Invalid token")
        return value

    def save(self, **kwargs):
        token = self.validated_data['refresh']
        BlacklistedToken.objects.create(token=token)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)