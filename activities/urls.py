from django.urls import path
<<<<<<< HEAD
from .views import (
        TestView,
        HistoryActivitiesView,
        GetTotalCallsView
)
=======
from .views import TestView, GetTotalCallsView
>>>>>>> feature(sys-metrcis-view)daily,monthly and yearly metrics view finished

app_name = 'activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
<<<<<<< HEAD
    path('test-history/', HistoryActivitiesView.as_view(), name="test-history"),
=======
>>>>>>> feature(sys-metrcis-view)daily,monthly and yearly metrics view finished
    path('getdata/', GetTotalCallsView.as_view(), name="getdata"),
]
