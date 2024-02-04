from rest_framework import serializers

from games.models import Category
from games.serializers import GameSerializer


class CategorySerializer(serializers.ModelSerializer):
    games = GameSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
