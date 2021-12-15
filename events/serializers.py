from rest_framework import serializers

from events.models import Event, EventKind, Location
from forzaboard.serializers import UUIDModelSerializer


class EventKindSerializer(UUIDModelSerializer):

    class Meta:
        model = EventKind
        exclude = ['id']


class EventSerializer(UUIDModelSerializer):

    class Meta:
        model = Event
        exclude = ['id']


class LocationSerializer(UUIDModelSerializer):

    kind = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Location
        exclude = ['id']
