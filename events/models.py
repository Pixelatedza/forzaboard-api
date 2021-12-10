import uuid

from django.db import models

class EventKind(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    kind = models.ForeignKey(
        'EventKind',
        on_delete=models.CASCADE,
    )
    active = models.BooleanField()

class Location(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    x = models.IntegerField()
    y = models.IntegerField()
    main_event = models.ForeignKey(
        'Event',
        on_delete=models.SET_NULL,
        related_name='main_locations',
        null=True,
        blank=True
    )
