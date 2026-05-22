from dataclasses import fields
from django.contrib import messages
from urllib import request

from django.contrib import admin
from .models import Band, Event


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display=("name", "country_name")

class EventAdmin(admin.ModelAdmin):
    list_display=("name", "date_time")

    def __str__(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator=request.user

        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if obj.creator != request.user:
            return False
        if obj.bands.exists():
            return False
        return True

    def has_changed_permission(self,obj=None):
        if obj is None:
            return True
        if obj.creator != request.user:
            return False
        if obj.bands.exists():
            return False
        return True

    def get_fields(self, request, obj=None):
        fields=super().get_fields(request,obj)
        if 'creator' in fields:
            fields=[f for f in fields if f!='creator']
        return fields

admin.site.register(Event, EventAdmin)

