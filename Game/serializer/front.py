from rest_framework import serializers

from Game.models import Category, Game


class CategoryFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GameFrontSerializer(serializers.ModelSerializer):
    category = CategoryFrontSerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = '__all__'
