from rest_framework.viewsets import ModelViewSet

from .models import Category, Game
from .serializers import CategorySerializer, GameSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


