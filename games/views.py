from rest_framework import viewsets

from games.models import Game, Category
from games.serializers import GameSerializer, CategorySerializer


# Create your views here.

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
