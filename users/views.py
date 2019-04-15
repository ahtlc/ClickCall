from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import User
from .forms import SignupForm
from django.views.generic import TemplateView



class SignupView(generic.FormView):
    form_class = SignupForm
    success_url = 'users:login'
    template_name = 'users/signup.html'
    redirect_authenticated_user = True

    model = get_user_model()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy(self.success_url))
        return super(SignupView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        return redirect('users:login')


class LogoutView(auth_views.LogoutView):
    next_page = 'users:login'


class LoginView(auth_views.LoginView):
    """
    View that handles the login process
    """
    success_url = reverse_lazy('users:profile')
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    redirect_field_name = success_url


class ProfileView(generic.TemplateView):
    template_name = 'users/profile.html'
    model = User

class CollaboratorProfileView(TemplateView):
    template_name = 'users/collaborator-profile.html'
    model = User

class CollaboratorListView(generic.TemplateView):
    template_name = 'users/collaborator-list.html'
