from django.urls import path
from .views import (
        ClientsView,
        HistoryActivitiesView,
        GetTotalCallsView,
        ScheduleView,
        PopulateView,
        SystemMetricsView,
)

app_name = 'activities'

urlpatterns = [
    path('clients/', ClientsView.as_view(), name="clients"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
    path('schedule/', ScheduleView.as_view(), name="schedule"),
    path('populate_db/', PopulateView.as_view(), name="populate_db"),
    path('system_metrics', SystemMetricsView.as_view(), name="system_metrics")
]

from django.conf import settings

if(settings.DEBUG):
  urlpatterns+=[
    path('populate_db/', PopulateView.as_view(), name="populate_db")
    ]
