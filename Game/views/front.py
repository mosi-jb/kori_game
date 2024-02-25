from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from Game.models import Game, Category
from Game.serializer.front import GameFrontSerializer, CategoryFrontSerializer


# Create your views here.

class GameFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameFrontSerializer
    search_fields = (
        "title", "game_play", "story")


class CategoryFrontViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryFrontSerializer
