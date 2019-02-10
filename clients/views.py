from django.shortcuts import render
from django.views import generic


class NewContactView(generic.TemplateView):
    template_name='tests.html'