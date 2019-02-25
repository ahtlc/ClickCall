from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class SignupForm(forms.Form):
    pass


class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
           "placeholder": "exemplo@clickcall.org.br",
        }
    ), help_text="Insira um e-mail válido")

    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "id": "pwd",
                "placeholder": "senha",
            }
        )
    )

    class Meta:
        model = User

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.',
                                        code='invalid_login')

    #  def __init__(self, request, *args, **kwargs):
        #  simply do not pass 'request' to the parent
        #  super().__init__(*args, **kwargs)
#
