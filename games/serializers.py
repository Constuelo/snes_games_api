# games/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from games.models import Game, Publisher, Developer


class GameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    publisher = serializers.SlugRelatedField(queryset=Publisher.objects.all(), slug_field='publisher')
    developer = serializers.SlugRelatedField(queryset=Developer.objects.all(), slug_field='developer')

    class Meta:
        model = Game
        depth = 1
        fields = ('url', 'id', 'title', 'owner', 'publisher', 'developer',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True, view_name='game-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'games')