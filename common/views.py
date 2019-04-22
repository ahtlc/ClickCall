from django.views import generic
from django.urls import reverse_lazy

from calls.models import Contact
from django.views.generic import ListView


class IndexView(generic.RedirectView):
    url = reverse_lazy('users:login')


class ClientListView(ListView):
    model = Contact
    template_name='client_list.html'
    paginate_by=5