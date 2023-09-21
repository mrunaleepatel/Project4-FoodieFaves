from .models import Recipe
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]