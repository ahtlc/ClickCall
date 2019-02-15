from django.urls import path
from .views import TestView

app_name = 'users'

urlpatterns = [
    # path('test/', )
    path('test/', TestView.as_view(), name = "test"),
]
