from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (
TemplateView,
FormView,
RedirectView,
CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, SigninForm
from django.contrib.auth.models import User
from . import choices


class HomeView(TemplateView):
    template_name = 'user/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile:
            if request.user.profile.role == choices.ADMIN:
                return redirect('hardware:hardware_control_list')
        if request.user.is_authenticated and request.user.profile:
            if request.user.profile.role == choices.CUSTOMER:
                return redirect('hardware:hardware_control_list')
        return super(HomeView, self).get(request, *args, **kwargs)


class Login(FormView):
    form_class = LoginForm
    template_name = 'user/includes/partials/login.html'
    success_url = reverse_lazy('user:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(Login, self).form_valid(form)
        else:
            return self.form_invalid(form)


class Logout(RedirectView):
    url = reverse_lazy('user:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class Signin(CreateView):
    form_class = SigninForm
    model = User
    template_name = 'user/includes/partials/signin.html'
    success_url = reverse_lazy('user:home')
