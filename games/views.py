from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from games.models import Game, Category
from games.serializers import GameSerializer, CategorySerializer, GameSerializer2, CategorySerializer2


# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Game.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return GameSerializer
            case 'create':
                return GameSerializer2
            case 'retrieve':
                return GameSerializer2
            case 'update':
                return GameSerializer2
            case 'partial_update':
                return GameSerializer2
            case 'destroy':
                return GameSerializer2

            case _:
                raise NotAcceptable()


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategorySerializer2
            case 'create':
                return CategorySerializer
            case 'retrieve':
                return CategorySerializer
            case 'update':
                return CategorySerializer
            case 'partial_update':
                return CategorySerializer
            case 'destroy':
                return CategorySerializer

            case _:
                raise NotAcceptable()
