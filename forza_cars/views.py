from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from forza_cars.models import Brand, Car
from forza_cars.serializers import BrandSerializer, CarSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing brands.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'


class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing cars.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    lookup_field = 'uuid'
