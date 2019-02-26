from django.urls import path
from . import views
from .views import (
        TestView,
        HistoryActivitiesView,
        GetTotalCallsView,
        contactRegisterView,
)

app_name = 'activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
    path('contact_new/', contactRegisterView.as_view(), name="contact_new")
]
