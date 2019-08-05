from django import forms
from django.forms import ModelForm
from .models import Site
# from . import choices


class FilterSiteForm(ModelForm):
    # cs_code = forms.CharField(required=False)
    # supervendor_code = forms.CharField(required=False)

    class Meta:
        model = Site
        fields = '__all__'