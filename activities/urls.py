from django.urls import path
from .views import (
        TestView,
        HistoryActivitiesView
)

app_name = 'activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history")
]
