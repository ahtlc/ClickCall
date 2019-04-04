from django.urls import path
from .views import (
        TestView,
        HistoryActivitiesView,
        GetTotalCallsView
        TestScheduleView
)

app_name = 'activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
    path('test-schedule/', TestScheduleView.as_view(), name="test-schedule"),
]
