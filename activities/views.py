from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


class TestView(generic.TemplateView):
    template_name = "call-history.html"

class SystemMetrics(TemplateView):
    template_name = "system-metrics.html"
