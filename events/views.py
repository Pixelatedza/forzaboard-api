from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from events.models import Event, EventKind, Location
from events.serializers import EventSerializer, EventKindSerializer, LocationSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EventKindViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing event kinds.
    """
    queryset = EventKind.objects.all()
    serializer_class = EventKindSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing event kinds.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
