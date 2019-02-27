from django.urls import path
from .views import (TestView,
                    HistoryView)

app_name='activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('test-history/', HistoryView.as_view(),name="test-history")
]
