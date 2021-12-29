from rest_framework import serializers
from forzaboard.serializers import UUIDModelSerializer
from leaderboards.models import Record


class RecordPOSTSerializer(UUIDModelSerializer):

    class Meta:
        model = Record
        exclude = ['id']


class RecordGETSerializer(RecordPOSTSerializer):
    user = serializers.StringRelatedField(read_only=True)
    car = serializers.StringRelatedField(read_only=True)


