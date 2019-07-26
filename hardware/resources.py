from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, DateTimeWidget, IntegerWidget, ManyToManyWidget
from .models import HardwareCategory, Hardware, HardwareControl


class HardwareResource(resources.ModelResource):
    hardware_category = fields.Field(
        column_name='hardware category',
        attribute='hardware_category',
        widget=ForeignKeyWidget(HardwareCategory, field='name'))
    cs_code = fields.Field(
        column_name='cs code',
        attribute='cs_code',)
    supervendor_code = fields.Field(
        column_name='supervendor code',
        attribute='supervendor_code',)
    material_description = fields.Field(
        column_name='material description',
        attribute='material_description',)
    total_quantity = fields.Field(
        column_name='total quantity',
        attribute='total_quantity',)

    class Meta:
        model = Hardware
        exclude = ('state', 'sub_state', 'created_at', 'updated_at',)
        export_order = (
            'id',
            'hardware_category',
            'cs_code',
            'supervendor_code',
            'material_description',
            'unity',
            'total_quantity',
            # 'estate',
            # 'sub_state',
            # 'create_at',
            # 'updated_',
        )


class HardwareControlResource(resources.ModelResource):
    hardware_category = fields.Field(column_name='hardware category')
    hardware = fields.Field(
        column_name='cs code',
        attribute='hardware',
        widget=ForeignKeyWidget(Hardware, field='cs_code'))
    supervendor_code = fields.Field(column_name='supervendor code')
    material_description = fields.Field(column_name='material description')
    unity = fields.Field()
    total_quantity = fields.Field(column_name='total quantity')
    serial = fields.Field(
        column_name='serial',
        attribute='serial',)
    site = fields.Field(
        column_name='site',
        attribute='site',)
    hardware_state = fields.Field(
        column_name='hardware state',
        attribute='hardware_state',)

    class Meta:
        model = HardwareControl
        exclude = ('state', 'sub_state', 'created_at', 'updated_at',)
        export_order = (
            'id',
            'hardware_category',
            'hardware',
            'supervendor_code',
            'material_description',
            'unity',
            'total_quantity',
            'serial',
            'site',
            'hardware_state',
            # 'estate',
            # 'sub_state',
            # 'create_at',
            # 'updated_',
        )

    def dehydrate_hardware_category(self, obj):
        return obj.hardware.hardware_category

    def dehydrate_supervendor_code(self, obj):
        return obj.hardware.supervendor_code

    def dehydrate_material_description(self, obj):
        return obj.hardware.material_description

    def dehydrate_unity(self, obj):
        return obj.hardware.unity

    def dehydrate_total_quantity(self, obj):
        return obj.hardware.total_quantity
