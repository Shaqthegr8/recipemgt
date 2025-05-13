from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # Root URL now handled by your app
]
# This will allow you to access the admin interface at /admin/ and your API at /recipes/