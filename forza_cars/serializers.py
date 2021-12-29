from forzaboard.serializers import UUIDModelSerializer
from forza_cars.models import Brand, Car


class BrandSerializer(UUIDModelSerializer):

    class Meta:
        model = Brand
        exclude = ['id']


class CarSerializer(UUIDModelSerializer):

    class Meta:
        model = Car
        exclude = ['id']
