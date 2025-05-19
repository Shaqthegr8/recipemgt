from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, RegisterUserView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
