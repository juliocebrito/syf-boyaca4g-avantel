from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile


class LoginForm(AuthenticationForm):
    pass


class SigninForm(UserCreationForm):
    email = forms.EmailField(label='Dirección de correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super(SigninForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False
        if commit:
            user.save()
        return user