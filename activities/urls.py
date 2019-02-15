from django.urls import path
from .views import TestView

app_name='activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
]
