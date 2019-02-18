from django.views import generic
from django.contrib import auth
from django.contrib.auth import get_user_model, authenticate, views
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import User


class PasswordResetView (generic.TemplateView):
    template_name = 'password-reset.html'


class ConfirmPasswordResetView (generic.TemplateView):
    template_name = 'confirm-password-reset.html'


class LogoutView(views.LogoutView):
    next_page = 'login'


class LoginView(views.LoginView):
    success_url = 'common:test'
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:home'))
        return super(LoginView, self).get(request)

