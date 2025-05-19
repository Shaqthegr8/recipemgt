from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
        ('Main Course', 'Main Course'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.JSONField()  # stores a list of ingredients
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    preparation_time = models.PositiveIntegerField(default=10, help_text="In minutes")
    cooking_time = models.PositiveIntegerField(default=10, help_text="In minutes")
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title
