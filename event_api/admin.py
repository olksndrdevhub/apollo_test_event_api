from typing import TYPE_CHECKING
from django.contrib import admin

from .models import Event, EventType


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_filter = ['event_type', 'timestamp',]


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, admin.ModelAdmin)