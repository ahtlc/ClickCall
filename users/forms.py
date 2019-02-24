from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(help_text="Insira um e-mail válido")
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "id": "pwd",
            }
        )
    )

    class Meta:
        model = User
