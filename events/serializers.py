from events.models import Event, EventKind, Location
from forzaboard.serializers import UUIDRelatedField, UUIDModelSerializer


class EventKindSerializer(UUIDModelSerializer):
    class Meta:
        model = EventKind


class EventSerializer(UUIDModelSerializer):

    class Meta:
        model = Event
        fields = ['location', 'kind', 'active']


class LocationSerializer(UUIDModelSerializer):
    serializer_related_field = UUIDRelatedField

    class Meta:
        model = Location
        fields = ['x', 'y', 'main_event']
