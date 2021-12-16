from django.contrib import admin
from events.models import Event, EventKind, Location

admin.site.register(Event)
admin.site.register(EventKind)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'x', 'y')
    list_filter = ('kind__name',)
    search_fields = ('name',)


admin.site.register(Location, LocationAdmin)
