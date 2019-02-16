from django.urls import path
from .views import TestView, PasswordTestView, ConfirmPasswordView


app_name = 'users'

urlpatterns = [
    # path('test/', )
    path('test/', TestView.as_view(), name = "test"),
    path('test-password/', PasswordTestView.as_view(), name = "test-password"),
    path('test-confirm-password/', ConfirmPasswordView.as_view(), name = "test-confirm-password"),
]
