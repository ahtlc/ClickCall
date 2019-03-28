from django.views import generic
from django.urls import reverse_lazy


class TestView(generic.TemplateView):
    template_name = 'profile.html'


class IndexView(generic.RedirectView):
    url = reverse_lazy('users:login')
