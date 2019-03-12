from django.urls import path
from .views import (TestView,
                    HistoryActivitiesView,
                    HistoryCollaboratorView
                    )

app_name='activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('agenda/', HistoryActivitiesView.as_view(),name="test-history"),
    path('test-collaborator/', HistoryCollaboratorView.as_view(),name="test-history")
]
