from django.views import generic


class TestView(generic.TemplateView):
    template_name = 'login.html'


class IndexView(generic.RedirectView):
    url = 'u/login/'
