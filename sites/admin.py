from django.contrib import admin
from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    resource_class = Site
    list_display = (
        'id',
        'site_name',
        'file1',
        'file2',
        'file3',
        'file4',
        'file5',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'site_name']
