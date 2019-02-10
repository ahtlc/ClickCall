from django.urls import path
from .views import NewContactView

app_name='clients'

urlpatterns = [
    path('new_contact', NewContactView.as_view(), name='new_contact'),
]