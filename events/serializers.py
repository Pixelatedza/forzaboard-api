from rest_framework import serializers
from events.models import Event, EventKind, Location


class EventKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventKind
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
