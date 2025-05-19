from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from recipes.views_auth import RegisterUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
    path('api/', include('recipes.urls')),
]
