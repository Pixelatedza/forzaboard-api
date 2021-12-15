from rest_framework import serializers
from forzaboard.serializers import UUIDModelSerializer
from leaderboards.models import Record


class RecordSerializer(UUIDModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    car = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Record
        exclude = 'id',

