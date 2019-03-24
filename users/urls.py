from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    ProfileView,
    SignupView,
)

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from django.urls import reverse_lazy

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-reset/', PasswordResetView.as_view(
            template_name='users/password-reset.html',
            success_url=reverse_lazy('users:password-reset-done'),
            email_template_name='users/password-reset-email.html',
            subject_template_name='users/password-reset-subject.txt',
            from_email='Suporte Clickcall <templatedmailtest@gmail.com>'
        ),
        name='password-reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
            template_name='users/password-reset-done.html'
        ),
        name='password-reset-done'),

    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(
            template_name='users/password-reset-confirm.html',
            success_url=reverse_lazy('users:password-reset-complete'),
        ),
        name="password-reset-confirm"),

    path('reset/done/', PasswordResetCompleteView.as_view(
            template_name='users/password-reset-complete.html'
        ),
        name="password-reset-complete"),
]
