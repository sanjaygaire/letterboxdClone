from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LogoutSerializer, RegisterSerializer, VerifyEmailSerializer
from django.core.mail import send_mail
import random
from .models import EmailVerification, User

class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        otp = str(random.randint(100000, 999999))
        EmailVerification.objects.create(user=user, otp=otp)

        send_mail(
            'Verify Your Email',
            f'Your OTP is {otp}',
            'noreply@example.com',
            [user.email],
            fail_silently=False,
        )

        return Response({"detail": "Registration successful. Check email for OTP."}, status=status.HTTP_201_CREATED)

class VerifyEmailView(APIView):
    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        try:
            user = User.objects.get(email=email)
            verification = EmailVerification.objects.get(user=user, otp=otp)
            if not verification.is_verified:
                verification.is_verified = True
                verification.save()
                return Response({"detail": "Email verified successfully!"})
            else:
                return Response({"detail": "Already verified"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"detail": "Invalid OTP or email"}, status=status.HTTP_400_BAD_REQUEST)