from django.urls import path
from .views import (
    SiteList,
    SiteSearch,
    SiteFilter,
    # site_export,
)

app_name = 'sites'

urlpatterns = [
    path('site/list/', SiteList.as_view(), name='site_list'),
    path('site/search/', SiteSearch.as_view(), name='site_search'),
    path('site/filter/', SiteFilter.as_view(), name='site_filter'),
    # path('site/export/', site_export, name='site_export'),
]