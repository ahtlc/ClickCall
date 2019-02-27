from django.shortcuts import render
from django.views import generic


class TestView(generic.TemplateView):
    template_name = "tests.html"

class HistoryView(generic.TemplateView):
    template_name = "history-test.html"
