from django.urls import path
from .views import (
        ClientsView,
        HistoryActivitiesView,
        GetTotalCallsView,
        ScheduleView,
        CallSchedulingRegisterView,
        CallPopUpView,
        PopulateView,
        SystemMetricsView,
)

app_name = 'activities'

urlpatterns = [
    path('clients/', ClientsView.as_view(), name="clients"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
    path('schedule/', ScheduleView.as_view(), name="schedule"),
    path('system_metrics/', SystemMetricsView.as_view(), name="system_metrics"),
    path('call_popup/', CallPopUpView.as_view(), name= "call_popup"),
    path('call_scheduling/', CallSchedulingRegisterView.as_view(), name="call_scheduling"),
    path('populate-db/', PopulateView.as_view(), name="populate-db"),
]

from django.conf import settings

if(settings.DEBUG):
    urlpatterns += [
        path('populate_db/', PopulateView.as_view(), name="populate_db")
    ]
