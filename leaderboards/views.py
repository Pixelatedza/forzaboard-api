from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from leaderboards.models import Record
from leaderboards.serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and records.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'
