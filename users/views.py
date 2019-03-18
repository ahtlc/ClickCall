from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import User
from .forms import SignupForm
from django import forms


class SignupView(generic.FormView):
    form_class = SignupForm
    success_url = 'users:login'
    template_name = 'signup.html'
    redirect_authenticated_user = True

    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy(self.success_url))
        return super(SignupView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        return redirect('users:login')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password-reset.html'
    form_class = forms.PasswordChangeForm


class ConfirmPasswordResetView (generic.TemplateView):
    template_name = 'confirm-password-reset.html'


class LogoutView(auth_views.LogoutView):
    next_page = 'users:login'


class LoginView(auth_views.LoginView):
    """
    View that handles the login process
    """
    success_url = 'users:profile'
    template_name = 'login.html'
    redirect_authenticated_user = False

    def get(self, request, *arg, **kwargs):
        if(request.user.is_authenticated):
            return HttpResponseRedirect(reverse_lazy('users:profile'))
        return super(LoginView, self).get(request)


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
    model = User
