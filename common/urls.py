from django.urls import path
from .views import (IndexView, 
                    ClientListView)

app_name = 'common'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='clients'),
]
