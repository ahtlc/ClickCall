from django.urls import path
from .views import (TestView,
                    HistoryCollaboratorView
                    )

app_name='activities'

urlpatterns = [
    path('test/', TestView.as_view(), name="test"),
    path('test-collaborator/', HistoryCollaboratorView.as_view(),name="test-history")
]
