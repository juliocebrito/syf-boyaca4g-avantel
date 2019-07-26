from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
TemplateView,
ListView,
DetailView,
UpdateView,
CreateView,
DeleteView,
FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Hardware, HardwareControl
from .forms import FilterHardwareForm, FilterHardwareControlForm
from .resources import HardwareResource, HardwareControlResource
from django.http import HttpResponse
import operator
from django.db.models import Q
from functools import reduce


class HardwareList(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Hardware
    template_name = 'hardware/hardware_list.html'
    paginate_by = 15
    form_class = FilterHardwareForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(HardwareList, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Hardware.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context


class HardwareSearch(HardwareList):

    def get_queryset(self):
        queryset = super(HardwareSearch, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                       (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(hardware_category__name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(cs_code__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(supervendor_code__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(material_description__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HardwareSearch, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context


class HardwareFilter(HardwareList):
    query_dict = {}

    def get_queryset(self):
        queryset = super(HardwareFilter, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = {k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by'}
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HardwareFilter, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context


def export_hardware(request):
    hardware_resource = HardwareResource()
    query_dict = request.GET.dict()
    queryset = Hardware.objects.filter(**query_dict)
    dataset = hardware_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Hardware.xlsx"'
    return response


class HardwareControlList(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = HardwareControl
    template_name = 'hardware_control/hardware_control_list.html'
    paginate_by = 15
    form_class = FilterHardwareControlForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(HardwareControlList, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(HardwareControl.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context


class HardwareControlSearch(HardwareControlList):

    def get_queryset(self):
        queryset = super(HardwareControlSearch, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                       (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(hardware__cs_code__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(serial__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(site__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(hardware_state__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HardwareControlSearch, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context


class HardwareControlFilter(HardwareControlList):
    query_dict = {}

    def get_queryset(self):
        queryset = super(HardwareControlFilter, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = {k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by'}
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HardwareControlFilter, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context


def export_hardware_control(request):
    hardware_control_resource = HardwareControlResource()
    query_dict = request.GET.dict()
    queryset = HardwareControl.objects.filter(**query_dict)
    dataset = hardware_control_resource.export(queryset)
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Hardware.xlsx"'
    return response
