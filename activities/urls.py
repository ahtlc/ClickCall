from django.urls import path
from .views import TestView, SystemMetrics

app_name='activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('metricas/', SystemMetrics.as_view(), name="metricas"),
]
