from rest_framework import serializers
from forzaboard.serializers import UUIDModelSerializer
from forza_cars.models import Brand, Car


class BrandSerializer(UUIDModelSerializer):

    class Meta:
        model = Brand


class CarSerializer(UUIDModelSerializer):

    brand = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = ['brand']
