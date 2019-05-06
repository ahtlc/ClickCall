from django.urls import path
from . import views
from .views import (
        ClientsView,
        HistoryActivitiesView,
        GetTotalCallsView,
        ContactRegisterView,
)
from .views import TestView, GetTotalCallsView, PopulateView
app_name = 'activities'

urlpatterns = [
    path('clients/', ClientsView.as_view(), name="clients"),
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
    path('populate-db/',PopulateView.as_view(), name="populate-db")
    path('contact_new/', ContactRegisterView.as_view(), name="contact_new")
]
