from rest_framework import serializers
from forzaboard.serializers import UUIDModelSerializer
from leaderboards.models import Leaderboard, Record


class LeaderboardSerializer(UUIDModelSerializer):

    class Meta:
        model = Leaderboard
        fields = ['event']


class RecordSerializer(UUIDModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Record
        fields = [
            'leaderboard',
            'value',
            'user',
            'video',
            'platform',
            'created',
        ]

