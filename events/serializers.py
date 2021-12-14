from rest_framework import serializers

from events.models import Event, EventKind, Location
from forzaboard.serializers import UUIDRelatedField, UUIDModelSerializer


class EventKindSerializer(UUIDModelSerializer):
    class Meta:
        model = EventKind


class EventSerializer(UUIDModelSerializer):

    kind = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ['location', 'kind', 'active']


class LocationSerializer(UUIDModelSerializer):
    serializer_related_field = UUIDRelatedField

    class Meta:
        model = Location
        fields = ['x', 'y', 'main_event']
