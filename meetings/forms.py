from django import forms
from django.forms import ModelForm
from .models import Meeting, Point
from . import choices


class FilterMeetingForm(ModelForm):
    # cs_code = forms.CharField(required=False)
    # supervendor_code = forms.CharField(required=False)

    class Meta:
        model = Meeting
        fields = '__all__'


class FilterPointForm(ModelForm):
    # hardware = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=False)
    # serial = forms.CharField(required=False)

    class Meta:
        model = Point
        fields = '__all__'