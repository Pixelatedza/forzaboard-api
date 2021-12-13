from django.db import models
from forzaboard.models import UUIDModel


class EventKind(UUIDModel):
    pass


class Event(UUIDModel):
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    kind = models.ForeignKey(
        'EventKind',
        on_delete=models.CASCADE,
    )
    active = models.BooleanField()


class Location(UUIDModel):
    x = models.IntegerField()
    y = models.IntegerField()
    main_event = models.ForeignKey(
        'Event',
        on_delete=models.SET_NULL,
        related_name='main_locations',
        null=True,
        blank=True
    )
