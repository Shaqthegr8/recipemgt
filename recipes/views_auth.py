from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class RegisterUser(APIView):
    permission_classes = [AllowAny]  # Anyone can access this endpoint

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not email or not password:
            return Response({"error": "All fields are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)

        return Response({
            "message": "User registered successfully.",
            "token": token.key
        }, status=201)
