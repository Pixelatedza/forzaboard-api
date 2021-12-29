from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from leaderboards.models import Record
from leaderboards.serializers import RecordGETSerializer, RecordPOSTSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and records.
    """
    queryset = Record.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RecordGETSerializer
        return RecordPOSTSerializer
