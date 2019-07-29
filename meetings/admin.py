from django.contrib import admin
from .models import Meeting, Point


class PointInline(admin.TabularInline):
    model = Point


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    resource_class = Meeting
    list_display = (
        'id',
        'date',
        'type_meeting',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'date', 'type_meeting']
    inlines = [PointInline]


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    resource_class = Point
    list_display = (
        'id',
        'meeting',
        'name',
        'description',
        'comments',
        'point_state',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'meeting', 'name', 'point_state']
