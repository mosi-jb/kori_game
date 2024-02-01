from rest_framework import serializers

from games.models import Game, Category


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    games = GameSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
