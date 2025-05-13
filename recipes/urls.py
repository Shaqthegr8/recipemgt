from django.urls import path
from . import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to the Recipe API!"})

urlpatterns = [
    path('', api_root),
    path('recipes/', api_root),  # placeholder for future recipe list
]
