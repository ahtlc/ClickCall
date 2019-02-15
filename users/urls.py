from django.urls import path
from .views import TestView, PasswordTestView


app_name = 'users'

urlpatterns = [
    # path('test/', )
    path('test/', TestView.as_view(), name = "test"),
    path('test-password/', PasswordTestView.as_view(), name = "test-password"),
]
