
from django.urls import path
app_name = 'users'

urlpatterns = [
    # path('test/', )
    path('test', TestView.as_view(), name = "test"),
]
