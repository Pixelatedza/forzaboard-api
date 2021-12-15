from django.contrib.auth import get_user_model
from django.db import models
from events.models import Event
from forza_cars.models import Car
from forzaboard.models import UUIDModel


class Record(UUIDModel):

    # Record does not need a name
    name = None

    # TODO: Consider making this it's own model.
    class Platforms(models.IntegerChoices):
        PC = 1
        XBOX = 2

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='leaderboards',
    )
    value = models.PositiveIntegerField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='records',
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='records'
    )
    pi = models.IntegerField(
        null=True,
        blank=True,
    )
    video = models.URLField(
        null=True,
        blank=True,
    )
    platform = models.IntegerField(
        choices=Platforms.choices,
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.name + ' ' + self.user.username
