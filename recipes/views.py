from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
    # Allow users to only update/delete their own recipes
        if self.request.user.is_authenticated:
            return Recipe.objects.all()
        return Recipe.objects.none()

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("You cannot edit someone else’s recipe.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You cannot delete someone else’s recipe.")
        instance.delete()

class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Automatically create token
        return user


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
