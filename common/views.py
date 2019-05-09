from django.views import generic
from django.urls import reverse_lazy

from calls.models import Contact, Tag
from django.views.generic import ListView


class IndexView(generic.RedirectView):
    url = reverse_lazy('users:login')


class ClientListView(ListView):
    model = Contact
    template_name='client_list.html'
    queryset = Contact.objects.all()
    paginate_by=5
    
    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context.update({
            'need-to-update':'update'
        })
        return context
    
    def get_queryset(self):
        context_queryset = super(ClientListView, self).get_queryset()
        request = self.request
        if 'filter-by' in request.GET:
            filter_by = request.GET.get('filter-by')
            search = request.GET.get('search')
            if search == '':
                return context_queryset
            if filter_by == 'name':
                context_queryset = context_queryset.filter(name__icontains = search)
            elif filter_by == 'tag':
                tags_to_find = Tag.objects.all().filter(name__icontains = search)
                context_queryset = context_queryset.filter(tag__in = tags_to_find)
        return context_queryset