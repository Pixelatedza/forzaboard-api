from django.db import models
from forzaboard.models import UUIDModel


class Brand(UUIDModel):
    pass


class Car(UUIDModel):
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        related_name='cars',
    )
