from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'  # Include all fields from the model
        read_only_fields = ['id', 'created_at', 'owner']
        
        