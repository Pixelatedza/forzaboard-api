from django.contrib import admin
from leaderboards.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('car', 'event', 'user')
    search_fields = ('event__name', 'user__username')


admin.site.register(Record, RecordAdmin)

