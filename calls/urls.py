from django.urls import path
from .views import CallModalView

app_name='calls'

urlpatterns = [
    path('modal/', CallModalView.as_view(), name="modal"),
]
