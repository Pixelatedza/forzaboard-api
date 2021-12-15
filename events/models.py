from django.db import models
from forzaboard.models import UUIDModel


class EventKind(UUIDModel):
    pass


class Event(UUIDModel):
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(
        default=True,
        help_text='Delete an event by marking it inactive.'
    )
    open = models.BooleanField(
        default=True,
        help_text='Whether records can still be added to an event or not.'
    )
    description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    series = models.IntegerField(
        null=True,
        blank=True,
    )

    class Seasons(models.IntegerChoices):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4

    season = models.IntegerField(
        choices=Seasons.choices,
        null=True,
        blank=True,
    )

    class PerformanceClasses(models.IntegerChoices):
        D = 1
        C = 2
        B = 3
        A = 4
        S1 = 5
        S2 = 6
        X = 7

    performance_class = models.IntegerField(
        choices=PerformanceClasses.choices,
        null=True,
        blank=True,
    )


class Location(UUIDModel):
    x = models.IntegerField()
    y = models.IntegerField()
    kind = models.ForeignKey(
        'EventKind',
        on_delete=models.CASCADE,
    )
    seasonal = models.BooleanField(
        default=False,
        help_text='Is this a seasonal event or not'
    )
    active = models.BooleanField(default=True)
