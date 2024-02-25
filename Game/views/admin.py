from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from Game.models import Game, Category
from Game.serializer.admin import GameSerializer, CategorySerializer


# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    search_fields = (
        "title", "game_play", "story")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
