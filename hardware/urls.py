from django.urls import path
from .views import (
    HardwareList,
    export_hardware,
    HardwareSearch,
    HardwareFilter,

    HardwareControlList,
    export_hardware_control,
    HardwareControlSearch,
    HardwareControlFilter,
)

app_name = 'hardware'

urlpatterns = [
    path('hardware/list/', HardwareList.as_view(), name='hardware_list'),
    path('export/hardware/', export_hardware, name='export_hardware'),
    path('hardware/search/', HardwareSearch.as_view(), name='hardware_search'),
    path('hardware/filter/', HardwareFilter.as_view(), name='hardware_filter'),

    path('hardware/control/list/', HardwareControlList.as_view(), name='hardware_control_list'),
    path('export/hardware/control', export_hardware_control, name='export_hardware_control'),
    path('hardware/control/search/', HardwareControlSearch.as_view(), name='hardware_control_search'),
    path('hardware/control/filter/', HardwareControlFilter.as_view(), name='hardware_control_filter'),
]