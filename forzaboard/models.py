import uuid
from django.db import models


class UUIDModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
