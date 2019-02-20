from django.urls import path
from .views import (ConfirmPasswordResetView, PasswordResetView,
                    LoginView, LogoutView, ProfileView)

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password-reset/', PasswordResetView.as_view(),
         name='password-reset'),
    path('password-reset-confirmation/', ConfirmPasswordResetView.as_view(),
         name='password-reset-confirmation'),
    path('<int:pk>/', ProfileView.as_view(), name='user-profile'),
]
