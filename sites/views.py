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
from .models import Site
from .forms import FilterSiteForm
# from .resources import SiteResource, SiteControlResource
from django.http import HttpResponse
import operator
from django.db.models import Q
from functools import reduce


class SiteList(LoginRequiredMixin, ListView, FormView):
    login_url = 'users:home'
    model = Site
    template_name = 'site/site_list.html'
    paginate_by = 15
    form_class = FilterSiteForm

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super(SiteList, self).get_context_data(**kwargs)
        context['items'] = self.get_queryset
        context['all_items'] = str(Site.objects.all().count())
        context['paginate_by'] = self.request.GET.get('paginate_by', self.paginate_by)
        context['query'] = self.request.GET.get('qs')
        return context


class SiteSearch(SiteList):

    def get_queryset(self):
        queryset = super(SiteSearch, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            queryset = queryset.filter(
                reduce(operator.and_,
                       (Q(id__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(site_sname__icontains=q) for q in query_list))
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SiteSearch, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset().count()
        return context


class SiteFilter(SiteList):
    query_dict = {}

    def get_queryset(self):
        queryset = super(SiteFilter, self).get_queryset()
        request_dict = self.request.GET.dict()
        query_dict = {k: v for k, v in request_dict.items() if v if k != 'page' if k != 'paginate_by'}
        self.query_dict = query_dict
        queryset = queryset.filter(**query_dict)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SiteFilter, self).get_context_data(**kwargs)
        context['query_dict'] = self.query_dict
        context['result'] = self.get_queryset().count()
        return context


# def export_hardware(request):
#     site_resource = SiteResource()
#     query_dict = request.GET.dict()
#     queryset = Site.objects.filter(**query_dict)
#     dataset = site_resource.export(queryset)
#     response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="Site.xlsx"'
#     return response
