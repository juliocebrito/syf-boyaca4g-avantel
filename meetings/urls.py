from django.urls import path
from .views import (
    PointList,
    PointSearch,
    PointFilter,
    # point_export,
)

app_name = 'meetings'

urlpatterns = [
    path('point/list/', PointList.as_view(), name='point_list'),
    path('point/search/', PointSearch.as_view(), name='point_search'),
    path('point/filter/', PointFilter.as_view(), name='point_filter'),
    # path('point/export/', point_export, name='point_export'),
]
