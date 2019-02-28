from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'avatar',
            'function',
            'phone',
            'ramal',
            'sector',
            ]

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Erro: as senhas não são iguais'
            )
        return cleaned_data

    def save(self, commit=True):
        raw_password = self.cleaned_data.get('password')
        self.instance.username = self.cleaned_data.get('username')
        self.instance.set_password(raw_password)
        if commit:
            self.instance.save()
        return self.instance


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
