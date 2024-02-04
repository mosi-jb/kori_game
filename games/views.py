from rest_framework import viewsets

from games.models import Game, Category
from games.serializer2 import CategorySerializer
from games.serializers import GameSerializer


# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
