from django.urls import path
from .views import TestView, IndexView

app_name = 'common'

urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('', IndexView.as_view(), name='index'),
]
