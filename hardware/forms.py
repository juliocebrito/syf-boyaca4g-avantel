from django import forms
from django.forms import ModelForm
from .models import HardwareCategory, Hardware, HardwareControl
from . import choices


class FilterHardwareForm(ModelForm):
    hardware_category = forms.ModelChoiceField(queryset=HardwareCategory.objects.all(), required=False)
    cs_code = forms.CharField(required=False)
    supervendor_code = forms.CharField(required=False)

    class Meta:
        model = Hardware
        fields = (
            'hardware_category',
            'cs_code',
            'supervendor_code',
            'material_description',)


class FilterHardwareControlForm(ModelForm):
    hardware = forms.ModelChoiceField(queryset=Hardware.objects.all(), required=False)
    serial = forms.CharField(required=False)

    class Meta:
        model = HardwareControl
        fields = '__all__'
