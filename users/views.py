from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import User
from .forms import LoginForm, SignupForm


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
        user = authenticate(username=self.object.email,
                            password=form.cleaned_data['password'])
        login(self.request, user)

        return redirect('users:profile')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'password-reset.html'


class ConfirmPasswordResetView (auth_views.PasswordResetConfirmView):
    template_name = 'confirm-password-reset.html'


class LogoutView(auth_views.LogoutView):
    next_page = 'users:login'


class LoginView(auth_views.LoginView):
    """
    For POST requests, tests the user credentials and return: a) the user
    object if it exists or b) None on the other case.
    For GET request, renders the authentication form.
    """
    success_url = 'users:profile'
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm

    def post(self, request):
        user = authenticate(email=request.POST.get('email'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy(self.success_url,
                                                     kwargs={'pk': user.pk}))
        else:
            return HttpResponseRedirect(reverse_lazy('users:login'))


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
    model = User
