from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from events.models import Event, EventKind, Location
from events.serializers import EventSerializer, EventKindSerializer, LocationGETSerializer, LocationPOSTSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'


class EventKindViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing event kinds.
    """
    queryset = EventKind.objects.all()
    serializer_class = EventKindSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'


class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing event kinds.
    """
    queryset = Location.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return LocationGETSerializer
        return LocationPOSTSerializer
