from rest_framework.serializers import ModelSerializer
from .models import Category, Game

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')
