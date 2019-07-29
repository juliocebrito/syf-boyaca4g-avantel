from django.contrib import admin
from .models import HardwareCategory, Hardware, HardwareControl, HardwareControlLog
from import_export.admin import ImportExportModelAdmin
from .resources import HardwareResource, HardwareControlResource
from import_export.formats import base_formats


@admin.register(HardwareCategory)
class HardwareCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'name']


@admin.register(Hardware)
class HardwareAdmin(ImportExportModelAdmin):
    resource_class = HardwareResource
    list_display = (
        'id',
        'hardware_category',
        'cs_code',
        'supervendor_code',
        'material_description',
        'unity',
        'total_quantity',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'hardware_category__name', 'cs_code', 'supervendor_code']

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


@admin.register(HardwareControl)
class HardwareControlAdmin(ImportExportModelAdmin):
    resource_class = HardwareControlResource
    list_display = (
        'id',
        'hardware',
        'serial',
        'site',
        'quantity',
        'hardware_state',
        'active_avantel',
        'state_avantel',
        'state',
        'sub_state',
        'created_at',
        'updated_at',
    )
    list_filter = ('state', 'sub_state', 'created_at', 'updated_at')
    search_fields = ['id', 'hardware__cs_code', 'serial', 'site', 'hardware_state', 'active_avantel', 'state_avante',]

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


# @admin.register(HardwareControlLog)
# class HardwareControlLogAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'hardware_control',
#         'hardware',
#         'serial',
#         'site',
#         'quantity',
#         'hardware_state',
#         'created_at',
#         'updated_at',
#     )
