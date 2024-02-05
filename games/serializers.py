from rest_framework import serializers

from games.models import Game, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'games')


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = '__all__'


class GameSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    games = GameSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'games')
