from django.contrib import admin
from events.models import Event, EventKind, Location

admin.site.register(Event)
admin.site.register(EventKind)
admin.site.register(Location)
