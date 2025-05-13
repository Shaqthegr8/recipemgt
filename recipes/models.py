from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField()  # Later you can split this by comma or JSON
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    prep_time = models.PositiveIntegerField(help_text="Time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Time in minutes")
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
