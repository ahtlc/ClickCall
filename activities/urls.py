from django.urls import path
from .views import SystemMetrics

app_name='activities'

urlpatterns = [
    path('metrics/', SystemMetrics.as_view(), name="metrics"),
]
