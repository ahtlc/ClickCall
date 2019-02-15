from django.shortcuts import render
from django.views import generic

class PasswordTestView (generic.TemplateView):
    template_name = "password-reset.html"

class TestView (generic.TemplateView):
    template_name = "login.html"

# Create your views here.
