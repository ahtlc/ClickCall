from django.shortcuts import render
from django.views import generic


class TestView(generic.TemplateView):
    template_name = "call-history.html"
