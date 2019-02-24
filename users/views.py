from django.views import generic
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate, views
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

from .models import User


class PasswordResetView (generic.TemplateView):
    template_name = 'password-reset.html'


class ConfirmPasswordResetView (generic.TemplateView):
    template_name = 'confirm-password-reset.html'


class LogoutView(views.LogoutView):
    next_page = 'users:login'


class UserLoginView(views.LoginView):
    success_url = 'users:profile'
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:profile'))
        return super(LoginView, self).get(request)


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
    model = User
