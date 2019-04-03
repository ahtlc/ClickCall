from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.RedirectView):
    url = reverse_lazy('users:login')
