from rest_framework import serializers
from events.models import Event, EventKind, Location


class EventKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventKind
        fields = ['uuid', 'name']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['uuid', 'name', 'location', 'kind', 'active']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['uuid', 'name', 'x', 'y', 'main_event']
