from django.contrib.auth import get_user_model
from rest_framework import serializers
from forzaboard.serializers import UUIDModelSerializer
from leaderboards.models import Record


class RecordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['uuid', 'username']


class RecordPOSTSerializer(UUIDModelSerializer):

    class Meta:
        model = Record
        exclude = ['id']


class RecordGETSerializer(RecordPOSTSerializer):
    user = RecordUserSerializer(read_only=True)
    car = serializers.StringRelatedField(read_only=True)


